# Ultrasonic Distance/Level Sensor - Milesight IoT

The payload decoder function is applicable to EM310-UDL.

## Payload Definition

| CHANNEL  |  ID  | TYPE | LENGTH | DESCRIPTION                                             |
| :------: | :--: | :--: | :----: | ------------------------------------------------------- |
| Battery  | 0x01 | 0x75 |   1    | battery(1B)<br/>battery, unit: %                        |
| Distance | 0x03 | 0x82 |   2    | distance(2B)<br/>distance, unit: mm                     |
| Position | 0x04 | 0x00 |   1    | position(1B)<br/>position, values: (0: normal, 1: tilt) |