# Sound Contact Switch - Milesight IoT

The payload decoder function is applicable to WS302.

## Payload Definition

|   CHANNEL   |  ID  | TYPE | LENGTH | DESCRIPTION                            |
| :---------: | :--: | :--: | :----: | -------------------------------------- |
|   Battery   | 0x01 | 0x75 |   1    | battery(1B)<br />battery, unit: %      |
| Sound Level | 0x05 | 0x5B |   7    | wight(1B) + l(2B) + leq(2B) + lmax(2B) |


