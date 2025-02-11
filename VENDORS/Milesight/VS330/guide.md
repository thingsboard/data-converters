# Bathroom Occupancy Sensor - Milesight IoT

The payload decoder function is applicable to VS330.

## Payload Definition

|   CHANNEL   |  ID  | TYPE | LENGTH | DESCRIPTION                                                      |
| :---------: | :--: | :--: | :----: | ---------------------------------------------------------------- |
|   Battery   | 0x01 | 0x75 |   1    | battery(1B)<br/>battery, unit: %                                 |
|  Distance   | 0x02 | 0x82 |   2    | distance(2B)<br/>distance, unit: mm                              |
|  Occupancy  | 0x03 | 0x8E |   1    | occupancy(1B)<br/>occupancy, values: (0: vacant, 1: occupied)    |
| Calibration | 0x04 | 0x8E |   1    | calibration(1B)<br/>calibration, values: (0: failed, 1: success) |
