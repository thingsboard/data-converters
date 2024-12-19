# Multifunctional Ultrasonic Distance/Level Sensor - Milesight IoT

The payload decoder function is applicable to EM400-UDL.

## Payload Definition

|        CHANNEL         |  ID  | TYPE | LENGTH | DESCRIPTION                                            |
| :--------------------: | :--: | :--: | :----: | ------------------------------------------------------ |
|        Battery         | 0x01 | 0x75 |   1    | battery(1B)<br />battery, unit: %                      |
|      Temperature       | 0x03 | 0x67 |   2    | temperature(2B)<br />temperature, unit: ℃              |
|        Distance        | 0x04 | 0x82 |   2    | distance(2B)<br />distance, unit: mm                   |
|        Position        | 0x05 | 0x00 |   1    | position(1B)<br />position, values(0: normal, 1: tilt) |
| Location<br />(NB-IoT) | 0x06 | 0x88 |   9    | longitude(4B) + latitude(4B) + motion_status(1B)       |
|  Temperature Abnormal  | 0x83 | 0x67 |   3    | temperature(2B) + status(1B)                           |
|     Distance Alarm     | 0x84 | 0x82 |   3    | distance(2B) + status(1B)                              |

### Motion Status Definition

|    BITS     | 7..4                                                                  | 3..0                                                                            |
| :---------: | :-------------------------------------------------------------------- | :------------------------------------------------------------------------------ |
| DESCRIPTION | geofence_status, values: (0: inside, 1: outside, 2: unset, 3: unknown | motion_status, values: (0: unknown, 1: start moving, 2: moving, 3: stop moving) |