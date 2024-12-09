# Capacitive Level Sensor - Milesight IoT

The payload decoder function is applicable to EM300-CL.

## Payload Definition

|     CHANNEL      |  ID  | TYPE | LENGTH | DESCRIPTION                                                                                                                                       |
| :--------------: | :--: | :--: | :----: | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|     Battery      | 0x01 | 0x75 |   1    | battery(1B)<br/>battery, unit: %                                                                                                                  |
|  Liquid Status   | 0x03 | 0xED |   1    | liquid(1B)<br/>liquid, values: (0: uncalibrated, 1: full, 2: empty, 0xff: error)                                                                  |
| Calibrate Result | 0x04 | 0xEE |   1    | calibrate_result(1B)<br/>calibrate_result, values: (0: failed, 1: success)                                                                        |
|   Liquid Alarm   | 0x83 | 0xED |   2    | liquid(1B) + alarm(1B)<br/>liquid, values: (0: uncalibrated, 1: full, 2: empty, 0xff: error)<br/>alarm: (0: empty alarm release, 1: empty alarm ) |
