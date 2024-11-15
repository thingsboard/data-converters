# Nwave Car Counter FM Sensor Guide

## 4.2 Uplink Messages

| Message Type           | Port | Description                                                                                                                               |
|------------------------|------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Counter Update         | 1    | Sends the current car count data.                                                                                                         |
| Heartbeat              | 2    | Sends health monitoring data, including battery level and error status.                                                                   |
| Startup                | 3    | Sent after every startup, reboot, or re-join event to indicate the version and reset cause.                                               |
| Debug Messages         | 6    | Provides debug information, including errors in configuration or commands.                                                                |

---

## 4.2.1 Counter Update

| Byte | Name                      | Description                                                                                        |
|------|----------------------------|----------------------------------------------------------------------------------------------------|
| 0    | Counter value - bits 15..8 | The higher 8 bits of the 16-bit car count value                                                   |
| 1    | Counter value - bits 7..0  | The lower 8 bits of the 16-bit car count value                                                    |

- **Note**: Only the 16 least significant bits of the counter are sent in this message. The counter resets to zero on a reboot since it is not stored in nonvolatile memory. To detect a reboot, the server should process the Startup message (if `Reset cause` is not equal to 0, there was a reboot and the counter was reset to 0).

---

## 4.2.2 Heartbeat

| Byte | Bits | Name                     | Description                                                                                        |
|------|------|---------------------------|----------------------------------------------------------------------------------------------------|
| 0    | 4.0  | Error Mask                | Indicates any errors detected by the sensor                                                        |
| 0    | 7.5  | Reserved                  | Reserved bits                                                                                      |
| 1    | 7.0  | Battery voltage - last    | Last measured battery voltage value                                                                |
| 2    | 7.0  | Battery voltage - mean    | Average battery voltage over the last 24 hours                                                     |

- **Note**: Heartbeat messages monitor the device's health. A re-join procedure may be initiated if multiple heartbeat messages go unacknowledged, indicating potential connection issues.

To convert the transmitted battery voltage values to mV, use the formula:
```plaintext
Vbat = (2400 + value * 5) mV
```

where `value` is the transmitted battery voltage byte.

## 4.2.3 Startup

| Byte | Name                  | Description                  |
|------|------------------------|------------------------------|
| 0    | Major part of version | Major version number         |
| 1    | Minor part of version | Minor version number         |
| 2    | Micro part of version | Micro version number         |
| 3    | Reset cause           | Indicates the cause of reset |

- Reset cause codes:
    - `0x00`: No reset (re-joining LoRaWAN network)
    - `0x01`: Watchdog reset
    - `0x02`: Power On Reset
    - `0x03`: User Request Reset
    - `0x06`: Brownout Reset
    - `0x07`: Others

---

## 4.2.4 Debug Messages

| Byte | Debug Code    | Meaning                                                 | Additional Parameters |
|------|---------------|---------------------------------------------------------|------------------------|
| 899 (0x383) | Invalid user request | The downlink command has not been recognized or the provided configuration cannot be used | None                  |
| 805 (0x325) | No change in config  | Provided configuration matches the current configuration    | None                  |
