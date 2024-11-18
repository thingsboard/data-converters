# Bathroom Odor Detector - Milesight IoT

The payload decoder function is applicable to GS301.

## Payload Definition

|   CHANNEL   |  ID  | TYPE | LENGTH | DESCRIPTION                              |
| :---------: | :--: | :--: | :----: | ---------------------------------------- |
|   Battery   | 0x01 | 0x75 |   1    | battery(1B)<br/>battery, unit: %         |
| Temperature | 0x02 | 0x67 |   2    | temperature(2B)<br/>temperature, unit: ℃ |
|  Humidity   | 0x03 | 0x68 |   1    | humidity(1B)<br/>humidity, unit: %RH     |
|     NH3     | 0x04 | 0x7D |   2    | nh3(2B)<br/>nh3, unit: ppm               |
|     H2S     | 0x05 | 0x7D |   2    | h2s(2B)<br/>h2s, unit: ppm               |