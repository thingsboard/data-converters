# Industrial Temperature Sensor - Milesight IoT

The payload decoder function is applicable to EM500-PT100.

## Payload Definition

|      CHANNEL      |  ID  | TYPE | LENGTH | DESCRIPTION                                                                               |
| :---------------: | :--: | :--: | :----: | ----------------------------------------------------------------------------------------- |
|      Battery      | 0x01 | 0x75 |   1    | battery(1B)<br/>battery, unit: %                                                          |
|    Temperature    | 0x03 | 0x67 |   2    | temperature(2B)<br/>temperature, unit: ℃                                                  |
| Temperature Alarm | 0x83 | 0xD7 |   5    | temperature(2B) + temperature_change(2B) + temperature_alarm(1B)<br/>temperature, unit: ℃ |
|  Historical Data  | 0x20 | 0XCE |   6    | timestamp(4B) + temperature(2B)                                                           |