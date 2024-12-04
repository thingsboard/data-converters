# Smart Button - Milesight IoT

The payload decoder function is applicable to WS101.

## Payload Definition

|   CHANNEL    |  ID  | TYPE | LENGTH | DESCRIPTION                                                 |
| :----------: | :--: | :--: | :----: | ----------------------------------------------------------- |
|   Battery    | 0x01 | 0x75 |   1    | battery(1B)<br/>battery, unit: %                            |
| Button Press | 0xFF | 0x2E |   1    | press(1B)<br/>press, values: (1: short, 2: long, 3: double) |
