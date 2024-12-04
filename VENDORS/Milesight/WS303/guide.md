# Mini Leak Detection Sensor - Milesight IoT

The payload decoder function is applicable to WS303.

## Payload Definition

|    CHANNEL     |  ID  | TYPE | LENGTH | DESCRIPTION                                                 |
| :------------: | :--: | :--: | :----: | ----------------------------------------------------------- |
|    Battery     | 0x01 | 0x75 |   1    | battery(1B)<br/>battery, unit：%                            |
| Leakage Status | 0x03 | 0x00 |   1    | leakage_status(1B)<br/>leakage_status: (0：normal, 1：leak) |