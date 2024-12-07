# Smart Fill Level Monitoring Sensor - Milesight IoT

The payload decoder function is applicable to WS201.

## Payload Definition

|  CHANNEL  |  ID  | TYPE | LENGTH | DESCRIPTION                          |
| :-------: | :--: | :--: | :----: | ------------------------------------ |
|  Battery  | 0x01 | 0x75 |   1    | battery(1B)<br/>battery, unit: %     |
| Distance  | 0x03 | 0x82 |   2    | distance(2B)<br/>distance, unit: mm  |
| Remaining | 0x04 | 0xD6 |   1    | remaining(1B)<br/>remaining, unit: % |