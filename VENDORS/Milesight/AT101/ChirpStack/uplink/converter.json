var data = decodeToJson(payload);
var deviceName = data.deviceInfo.deviceName;
var deviceType = data.deviceInfo.deviceProfileName;



function decodePayload(input) {
    var output = { attributes:{}, telemetry: {} };
    // --- Decoding code --- //

    output.telemetry.HEX_bytes = bytesToHex(input);

    var decoded = {};

    for (var i = 0; i < input.length; ) {
        var channel_id = input[i++] & 0xff;
        var channel_type = input[i++] & 0xff;

        // BATTERY
        if (channel_id === 0x01 && channel_type === 0x75) {
            decoded.battery = input[i];
            i += 1;
        }
        // TEMPERATURE
        else if (channel_id === 0x03 && channel_type === 0x67) {
            decoded.temperature = parseBytesToInt(input, i, 2, false) / 10;
            i += 2;
        }
        // LOCATION
        else if ((channel_id === 0x04 || channel_id == 0x84) && channel_type === 0x88) {
            decoded.latitude = parseBytesToInt(input, i, 4, false) / 1000000;
            decoded.longitude = parseBytesToInt(input, i + 4, 4, false) / 1000000;
            var status = input[i + 8];
            decoded.motion_status = readMotionStatus(status & 0x0f);
            decoded.geofence_status = readGeofenceStatus(status >> 4);
            i += 9;
        }
        // DEVICE POSITION
        else if (channel_id === 0x05 && channel_type === 0x00) {
            decoded.position = readDevicePosition(input[i]);
            i += 1;
        }
        // Wi-Fi SCAN RESULT
        else if (channel_id === 0x06 && channel_type === 0xd9) {
            var wifi = {};
            wifi.group = input[i];
            wifi.mac = readMAC(input.slice(i + 1, i + 7));
            wifi.rssi = input[i + 7];
            wifi.motion_status = readMotionStatus(input[i + 8] & 0x0f);
            i += 9;

            decoded.wifi_scan_result = "finish";
            if (wifi.mac === "ff:ff:ff:ff:ff:ff") {
                decoded.wifi_scan_result = "timeout";
                continue;
            }
            decoded.motion_status = wifi.motion_status;

            if (decoded.wifi === null) {
                decoded.wifi = [];
            }
            decoded.wifi.push(wifi);
        }
        // TAMPER STATUS
        else if (channel_id === 0x07 && channel_type === 0x00) {
            decoded.tamper_status = readTamperStatus(input[i]);
            i += 1;
        }
        // TEMPERATURE WITH ABNORMAL
        else if (channel_id === 0x83 && channel_type === 0x67) {
            decoded.temperature = parseBytesToInt(input, i, 2, false) / 10;
            decoded.temperature_abnormal = input[i + 2] == 0 ? false : true;
            i += 3;
        }
        // HISTORICAL DATA
        else if (channel_id === 0x20 && channel_type === 0xce) {
            var location = {};
            location.timestamp = parseBytesToInt(input, i, 4, false);
            location.longitude = parseBytesToInt(input, i + 4, 4, false) / 1000000;
            location.latitude = parseBytesToInt(input, i + 8, 4, false) / 1000000;
            i += 12;

            if (decoded.history === null) {
                decoded.history = [];
            }
            decoded.history.push(location);
        }
        else {
            break;
        }
    }

    output.telemetry = decoded;

    // --- Decoding code --- //
    return output;
}

function readMAC(bytes) {
    var temp = [];
    for (var idx = 0; idx < bytes.length; idx++) {
        // var mac = ("0" + (bytes[idx] & 0xff).toString(16)).slice(-2);
        var mac = intToHex(bytes[idx] & 0xff);
        temp.push(mac);
    }
    return temp.join(":");
}

function readMotionStatus(type) {
    switch (type) {
        case 1:
            return "start";
        case 2:
            return "moving";
        case 3:
            return "stop";
        default:
            return "unknown";
    }
}

function readGeofenceStatus(type) {
    switch (type) {
        case 0:
            return "inside";
        case 1:
            return "outside";
        case 2:
            return "unset";
        default:
            return "unknown";
    }
}

function readDevicePosition(type) {
    switch (type) {
        case 0:
            return "normal";
        case 1:
            return "tilt";
        default:
            return "unknown";
    }
}

function readTamperStatus(type) {
    switch (type) {
        case 0:
            return "install";
        case 1:
            return "uninstall";
        default:
            return "unknown";
    }
}

// --- attributes and telemetry objects ---
var telemetry = {};
var attributes = {};
// --- attributes and telemetry objects ---

// --- Timestamp parsing
var dateString = data.time;
var timestamp = -1;
if (dateString != null) {
    timestamp = new Date(dateString).getTime();
    if (timestamp == -1) {
        var secondsSeparatorIndex = dateString.lastIndexOf('.') + 1;
        var millisecondsEndIndex = dateString.lastIndexOf('+');
        if (millisecondsEndIndex == -1) {
            millisecondsEndIndex = dateString.lastIndexOf('Z');
        }
        if (millisecondsEndIndex == -1) {
            millisecondsEndIndex = dateString.lastIndexOf('-');
        }
        if (millisecondsEndIndex == -1) {
            if (dateString.length >= secondsSeparatorIndex + 3) {
                dateString = dateString.substring(0, secondsSeparatorIndex + 3);
            }
        } else {
            dateString = dateString.substring(0, secondsSeparatorIndex + 3) +
                dateString.substring(millisecondsEndIndex, dateString.length);
        }
        timestamp = new Date(dateString).getTime();
    }
}
// If we cannot parse timestamp - we will use the current timestamp
if (timestamp == -1) {
    timestamp = Date.now();
}
// --- Timestamp parsing

// You can add some keys manually to attributes or telemetry
attributes.deduplicationId = data.deduplicationId;

// You can exclude some keys from the result
var excludeFromAttributesList = ["deviceName", "rxInfo", "confirmed", "data", "deduplicationId","time", "adr", "dr", "fCnt"];
var excludeFromTelemetryList = ["data", "deviceInfo", "txInfo", "devAddr", "adr", "time", "fPort", "region_common_name", "region_config_id", "deduplicationId"];

// Message parsing
// To avoid paths in the decoded objects we passing false value to function as "pathInKey" argument.
// Warning: pathInKey can cause already found fields to be overwritten with the last value found.

var telemetryData = toFlatMap(data, excludeFromTelemetryList, false);
var attributesData = toFlatMap(data, excludeFromAttributesList, false);

var uplinkDataList = [];

// Passing incoming bytes to decodePayload function, to get custom decoding
// var bas64 = base64ToBytes(data.data);
var hexB = hexToBytes(data.data);
var customDecoding = decodePayload(hexB);

// Collecting data to result
if (customDecoding.?telemetry.size() > 0) {
    telemetry.putAll(customDecoding.telemetry);
}

if (customDecoding.?attributes.size() > 0) {
    attributes.putAll(customDecoding.attributes);
}

telemetry.putAll(telemetryData);
attributes.putAll(attributesData);

var result = {
    deviceName: deviceName,
    deviceType: deviceType,
    attributes: attributes,
    telemetry: {
        ts: timestamp,
        values: telemetry
    }
};

return result;