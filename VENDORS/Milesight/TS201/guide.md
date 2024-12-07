# Temperature Sensor - Milesight IoT

The payload decoder function is applicable to TS201.

## Payload Definition

|           CHANNEL           |  ID  | TYPE | LENGTH | DESCRIPTION                                                                                                        |
| :-------------------------: | :--: | :--: | :----: | ------------------------------------------------------------------------------------------------------------------ |
|        IPSO Version         | 0xFF | 0x01 |   1    | ipso_version(1B)                                                                                                   |
|        Device Status        | 0xFF | 0x0B |   1    | device_status(1B)                                                                                                  |
|        Serial Number        | 0xFF | 0x16 |   8    | sn(8B)                                                                                                             |
|      Hardware Version       | 0xFF | 0x09 |   2    | hardware_version(2B)                                                                                               |
|      Firmware Version       | 0xFF | 0x0A |   2    | firmware_version(2B)                                                                                               |
|         TSL Version         | 0xFF | 0xFF |   2    | tsl_version(2B)                                                                                                    |
|           Battery           | 0x01 | 0x75 |   1    | battery(1B)<br/>battery, unit: %                                                                                   |
|         Temperature         | 0x03 | 0x67 |   2    | temperature(2B)<br/>temperature, unit: ℃                                                                           |
| Temperature Threshold Alarm | 0x83 | 0x67 |   3    | temperature(2B) + temperature_alarm(1B)<br/>temperature, unit: ℃                                                   |
| Temperature Mutation Alarm  | 0x93 | 0x67 |   5    | temperature(2B) + temperature_mutation(2B) + temperature_alarm(1B)<br/>temperature, unit: ℃                        |
|   Temperature Error Alarm   | 0xB3 | 0x67 |   1    | temperature_error(1B)<br/>                                                                                         |
|        History Data         | 0x20 | 0xCE |   7    | timestamp(4B) + type(1B) + temperature(2B)<br/>type, event_type(0..3) + read_status(4..7)<br/>temperature, unit: ℃ |