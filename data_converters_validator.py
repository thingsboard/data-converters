import os
import json
import base64
from tb_rest_client.rest_client_pe import RestClientPE
import re

ENDPOINT = os.getenv("ENDPOINT")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

client = RestClientPE(base_url=ENDPOINT)
client.login(username=USERNAME, password=PASSWORD)


def find_payload_and_result_pairs(directory):
    payloads = sorted([f for f in os.listdir(directory) if re.match(r'payload_\d+\.json', f)])
    results = sorted([f for f in os.listdir(directory) if re.match(r'result_\d+\.json', f)])

    pairs = []

    for payload_file in payloads:
        suffix = re.search(r'_(\d+)\.json', payload_file).group(1)  # Extract the number from the filename
        result_file = f"result_{suffix}.json"
        if result_file in results:
            pairs.append((payload_file, result_file))

    return pairs


def validate_uplink_downlink(directory, client):
    converter_file = os.path.join(directory, 'converter.json')
    metadata_file = os.path.join(directory, 'metadata.json')

    with open(converter_file) as f:
        converter = json.load(f)
    with open(metadata_file) as f:
        metadata = json.load(f)

    configuration = converter.get('configuration')
    script_lang = configuration.get('scriptLang')

    request = {
        "metadata": metadata,
    }

    payload_result_pairs = find_payload_and_result_pairs(directory)
    success = True  # Boolean flag to track if all validations are successful

    for payload_file, result_file in payload_result_pairs:
        with open(os.path.join(directory, payload_file)) as pf:
            payload = json.load(pf)
        with open(os.path.join(directory, result_file)) as rf:
            expected_result = json.load(rf)

        if 'uplink' in directory:
            decoder = configuration.get("decoder") if script_lang == "JS" else configuration.get("tbelDecoder")
            encoded_payload = base64.b64encode(json.dumps(payload).encode('utf-8')).decode('utf-8')
            request["decoder"] = decoder
            request["payload"] = encoded_payload
            actual_result = client.converter_controller.test_up_link_converter_using_post(async_req='false',
                                                                                          body=request,
                                                                                          script_lang=script_lang)
        elif 'downlink' in directory:
            encoder = configuration.get("encoder") if script_lang == "JS" else configuration.get("tbelEncoder")
            request["encoder"] = encoder
            request["msg"] = json.dumps(payload)
            request["msgType"] = "POST_TELEMETRY_REQUEST"
            request["integrationMetadata"] = {}
            actual_result = client.converter_controller.test_down_link_converter_using_post(async_req='false',
                                                                                            body=request,
                                                                                            script_lang=script_lang)
        else:
            raise ValueError(f"Directory '{directory}' is not recognized as 'uplink' or 'downlink'.")

        result_value = actual_result.get()
        output = result_value.get('output')
        error = result_value.get('error')

        if error != '':
            success = False  # Set the flag to False if any validation fails
            result_message = f"Validation failed for {directory} with payload {payload_file} and result {result_file} with error: {error}\n"
        elif json.loads(output) == expected_result:
            result_message = f"Validation passed for {directory} with payload {payload_file} and result {result_file}\n"
        else:
            success = False  # Set the flag to False if output does not match expected result
            result_message = f"Validation failed for {directory} with payload {payload_file} and result {result_file}. Expected output does not match.\n"

        print(result_message)

    return success  # Return whether this directory's validation was successful


def walk_vendors_directory(root_dir, client):
    all_success = True  # Overall success flag

    for root, dirs, files in os.walk(root_dir):
        if 'converter.json' in files and 'metadata.json' in files:
            success = validate_uplink_downlink(root, client)
            if not success:
                all_success = False  # Set overall flag to False if any validation fails

    return all_success


if __name__ == "__main__":
    root_directory = "VENDORS"
    all_success = walk_vendors_directory(root_directory, client)

    if all_success:
        print("All converters data validated successfully.")
    else:
        exit(1)
