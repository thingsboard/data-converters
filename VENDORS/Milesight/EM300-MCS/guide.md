# Magnetic Contact Switch - Milesight IoT

The payload decoder function is applicable to EM300-MCS.

## Payload Definition

|     CHANNEL     |  ID  | TYPE | LENGTH | DESCRIPTION                                                        |
| :-------------: | :--: | :--: | :----: | ------------------------------------------------------------------ |
|     Battery     | 0x01 | 0x75 |   1    | battery(1B)<br/>battery: unit: %                                   |
|   Temperature   | 0x03 | 0x67 |   2    | temperature(2B)<br/>temperature, unit: ℃                           |
|    Humidity     | 0x04 | 0x68 |   1    | humidity(1B)<br/>humidity, unit: %RH                               |
|  Magnet Status  | 0x06 | 0x00 |   1    | magnet_status(1B)<br/>magnet_status, values: (0: close, 1: open)   |
| Historical Data | 0x20 | 0XCE |   8    | timestamp(4B) + temperature(2B) + humidity(1B) + magnet_status(1B) |