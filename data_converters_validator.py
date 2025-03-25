import os
import json
import base64
import time
from tb_rest_client.rest_client_pe import RestClientPE
import re

ENDPOINT = os.getenv("ENDPOINT")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

client = RestClientPE(base_url=ENDPOINT)
client.login(username=USERNAME, password=PASSWORD)

ALLOWED_INTEGRATION_DIRECTORIES = {'SIGFOX', 'THINGPARK', 'TPE', 'CHIRPSTACK', 'PARTICLE', 'HTTP', 'MQTT', 'PUB_SUB',
                                   'AWS_IOT', 'AWS_SQS', 'AWS_KINESIS', 'IBM_WATSON_IOT', 'TTN', 'TTI',
                                   'AZURE_EVENT_HUB', 'OPC_UA', 'CUSTOM', 'UDP', 'TCP', 'KAFKA', 'AZURE_IOT_HUB',
                                   'APACHE_PULSAR', 'RABBITMQ', 'LORIOT', 'COAP', 'TUYA', 'AZURE_SERVICE_BUS', 'KPN'}

def find_payload_and_result_pairs(directory):
    payloads = sorted([f for f in os.listdir(directory) if re.match(r'payload(_\d+)?\.(json|base64)$', f)])
    results = sorted([f for f in os.listdir(directory) if re.match(r'result(_\d+)?\.json$', f)])

    pairs = []

    payload_main = next((f for f in payloads if re.match(r'payload\.(json|base64)$', f)), None)
    result_main = 'result.json'
    if payload_main and result_main in results:
        pairs.append((payload_main, result_main))
    elif payload_main and result_main not in results:
        print(f"Validation failed for {directory}: {payload_main} is present, but {result_main} is missing.")
    elif result_main in results and not payload_main:
        print(f"Validation failed for {directory}: {result_main} is present, but payload file is missing.")

    for payload_file in payloads:
        match = re.match(r'payload_(\d+)\.(json|base64)$', payload_file)
        if match:
            suffix = match.group(1)
            result_file = f"result_{suffix}.json"
            if result_file in results:
                pairs.append((payload_file, result_file))
            else:
                print(f"Validation failed for {directory}: {payload_file} is present, but {result_file} is missing.")

    for result_file in results:
        match = re.match(r'result_(\d+)\.json$', result_file)
        if match:
            suffix = match.group(1)
            payload_file_json = f"payload_{suffix}.json"
            payload_file_base64 = f"payload_{suffix}.base64"
            if payload_file_json not in payloads and payload_file_base64 not in payloads:
                print(
                    f"Validation failed for {directory}: {result_file} is present, but neither {payload_file_json} nor {payload_file_base64} is present.")

    return pairs

def validate_uplink_downlink(directory):
    converter_file = os.path.join(directory, 'converter.json')
    metadata_file = os.path.join(directory, 'metadata.json')

    if not os.path.exists(converter_file):
        print(f"Validation failed for {directory}: converter.json is missing.")
        return False
    if os.path.getsize(converter_file) == 0:
        print(f"Validation failed for {directory}: converter.json is empty.")
        return False

    if not os.path.exists(metadata_file):
        print(f"Validation failed for {directory}: metadata.json is missing.")
        return False
    if os.path.getsize(metadata_file) == 0:
        print(f"Validation failed for {directory}: metadata.json is empty.")
        return False

    with open(converter_file) as f:
        converter = json.load(f)
    with open(metadata_file) as f:
        metadata = json.load(f)

    configuration = converter.get('configuration')
    version = converter.get('converterVersion')
    script_lang = configuration.get('scriptLang')

    request = {
        "metadata": metadata,
    }

    payload_result_pairs = find_payload_and_result_pairs(directory)

    if not payload_result_pairs:
        print(f"Validation failed for {directory}: No valid payload-result pairs found.")
        return False

    success = True

    for payload_file, result_file in payload_result_pairs:
        if not os.path.exists(os.path.join(directory, payload_file)):
            print(f"Validation failed for {directory}: {payload_file} is missing.")
            success = False
            continue
        if os.path.getsize(os.path.join(directory, payload_file)) == 0:
            print(f"Validation failed for {directory}: {payload_file} is empty.")
            success = False
            continue

        if not os.path.exists(os.path.join(directory, result_file)):
            print(f"Validation failed for {directory}: {result_file} is missing.")
            success = False
            continue
        if os.path.getsize(os.path.join(directory, result_file)) == 0:
            print(f"Validation failed for {directory}: {result_file} is empty.")
            success = False
            continue

        with open(os.path.join(directory, payload_file)) as pf:
            if payload_file.endswith('.json'):
                payload_data = json.load(pf)
                if 'uplink' in directory:
                    processed_payload = base64.b64encode(json.dumps(payload_data).encode('utf-8')).decode('utf-8')
                else:
                    processed_payload = json.dumps(payload_data)
            elif payload_file.endswith('.base64'):
                processed_payload = pf.read().strip()
        with open(os.path.join(directory, result_file)) as rf:
            expected_result = json.load(rf)

        if 'uplink' in directory:
            decoder = configuration.get("decoder") if script_lang == "JS" else configuration.get("tbelDecoder")
            request["converter"] = converter
            request["decoder"] = decoder
            request["payload"] = processed_payload
            actual_result = client.converter_controller.test_up_link_converter_using_post(
                async_req='false', body=request, script_lang=script_lang)
        elif 'downlink' in directory:
            encoder = configuration.get("encoder") if script_lang == "JS" else configuration.get("tbelEncoder")
            request["encoder"] = encoder
            request["msg"] = processed_payload
            request["msgType"] = "POST_TELEMETRY_REQUEST"
            request["integrationMetadata"] = {}
            actual_result = client.converter_controller.test_down_link_converter_using_post(
                async_req='false', body=request, script_lang=script_lang)
        else:
            raise ValueError(f"Directory '{directory}' is not recognized as 'uplink' or 'downlink'.")

        result_value = actual_result.get()
        if version == 2:
            output = result_value.get('outputMsg')
        else:
            output = result_value.get('output')
        error = result_value.get('error')

        if error != '':
            success = False
            result_message = f"Validation failed for {directory} with payload {payload_file} and result {result_file} with error: {error}\n"
        else:
            parsed_output = json.loads(output) if version != 2 else output
            if parsed_output == expected_result:
                result_message = f"Validation passed for {directory} with payload {payload_file} and result {result_file}\n"
            else:
                success = False
                result_message = f"Validation failed for {directory} with payload {payload_file} and result {result_file}. Expected output does not match.\n"

        print(result_message)

        time.sleep(1)

    return success


def get_converter_version(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        converter_data = json.load(f)
    return converter_data.get('converterVersion')

def validate_device_files(device_path):
    required_files = {'info.json', 'photo.png'}
    found_files = set(file for file in os.listdir(device_path) if os.path.isfile(os.path.join(device_path, file)))
    missing_files = required_files - found_files

    if missing_files:
        print(f"Validation failed: Missing required files {', '.join(missing_files)} in {device_path}")
        return False

    info_path = os.path.join(device_path, 'info.json')
    if os.path.getsize(info_path) == 0:
        print(f"Validation failed: {info_path} is empty.")
        return False

    with open(info_path, 'r', encoding='utf-8') as info_file:
        info_data = json.load(info_file)

    required_keys = {'url', 'label', 'description'}
    missing_keys = required_keys - info_data.keys()
    if missing_keys:
        print(f"Validation failed: Missing keys {', '.join(missing_keys)} in {info_path}")
        return False

    empty_keys = [
        key for key in required_keys
        if not isinstance(info_data[key], str) or not info_data[key].strip()
    ]
    if empty_keys:
        print(f"Validation failed: Keys {', '.join(empty_keys)} in {info_path} have empty or invalid values.")
        return False

    if empty_keys:
        print(f"Validation failed: Keys {', '.join(empty_keys)} in {info_path} have empty values.")
        return False

    return True


def validate_company_files(company_path):
    required_files = ['logo.svg', 'info.json']
    all_present = True

    for file in required_files:
        file_path = os.path.join(company_path, file)
        if not os.path.exists(file_path):
            print(f"Validation failed: Missing '{file}' in {company_path}")
            all_present = False

    if "info.json" in required_files:
        info_path = os.path.join(company_path, "info.json")
        if os.path.exists(info_path):
            with open(info_path, 'r') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    print(f"Validation failed: 'info.json' in {company_path} is not valid JSON")
                    return False

            allowed_keys = {"description", "url"}
            if set(data.keys()) != allowed_keys:
                print(f"Validation failed: 'info.json' in {company_path} contains invalid keys. Allowed keys are {allowed_keys}.")
                return False

            for key in allowed_keys:
                if not data[key] or not isinstance(data[key], str):
                    print(f"Validation failed: '{key}' in 'info.json' in {company_path} is missing or empty.")
                    return False

    return all_present

def walk_vendors_directory(root_dir):
    all_success = True

    for company in os.listdir(root_dir):
        company_path = os.path.join(root_dir, company)

        if not os.path.isdir(company_path):
            continue

        if not validate_company_files(company_path):
            all_success = False
            continue

        for device in os.listdir(company_path):
            device_path = os.path.join(company_path, device)

            if not os.path.isdir(device_path):
                continue

            if not validate_device_files(device_path):
                all_success = False
                continue

            integrations = [item for item in os.listdir(device_path) if os.path.isdir(os.path.join(device_path, item))]
            if not integrations:
                print(f"Validation failed: No integration directories found in {device_path}")
                all_success = False
                continue

            for integration in integrations:
                if integration not in ALLOWED_INTEGRATION_DIRECTORIES:
                    print(f"Validation failed: Integration directory '{integration}' is not recognized.")
                    all_success = False
                    continue

                integration_path = os.path.join(device_path, integration)

                if not os.path.isdir(integration_path):
                    continue

                uplink_path = os.path.join(integration_path, 'uplink')
                downlink_path = os.path.join(integration_path, 'downlink')

                if not os.path.exists(uplink_path) and not os.path.exists(downlink_path):
                    print(f"Validation failed: Both 'uplink' and 'downlink' are missing in {integration_path}")
                    all_success = False

                if os.path.exists(uplink_path):
                    success = validate_uplink_downlink(uplink_path)
                    if not success:
                        all_success = False

                if os.path.exists(downlink_path):
                    success = validate_uplink_downlink(downlink_path)
                    if not success:
                        all_success = False

    return all_success



if __name__ == "__main__":
    root_directory = "VENDORS"
    all_success = walk_vendors_directory(root_directory)

    if all_success:
        print("All converters data validated successfully.")
    else:
        exit(1)
