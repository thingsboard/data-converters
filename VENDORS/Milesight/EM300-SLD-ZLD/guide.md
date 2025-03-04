# Spot Leak Detection Sensor / Zone Leak Detection Sensor - Milesight IoT

The payload decoder function is applicable to EM300-SLD and EM300-ZLD.

## Payload Definition

|     CHANNEL     |  ID  | TYPE | LENGTH | DESCRIPTION                                                         |
| :-------------: | :--: | :--: | :----: | ------------------------------------------------------------------- |
|     Battery     | 0x01 | 0x75 |   1    | battery(1B)<br/>battery, unit: %                                    |
|   Temperature   | 0x03 | 0x67 |   2    | temperature(2B)<br/>temperature, unit: ℃                            |
|    Humidity     | 0x04 | 0x68 |   1    | humidity(1B)<br/>humidity, unit: %RH                                |
| Leakage Status  | 0x05 | 0x00 |   1    | leakage_status(1B)<br/>leakage_status, values: (0: normal, 1: leak) |
| Historical Data | 0x20 | 0XCE |   8    | timestamp(4B) + temperature(2B) + humidity(1B) + leakage_status(1B) |