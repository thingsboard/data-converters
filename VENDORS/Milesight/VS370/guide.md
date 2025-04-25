# Radar Human Presence Sensor - Milesight IoT

The payload decoder function is applicable to VS370.

## Payload Definition

| CHANNEL          |  ID  | TYPE | LENGTH | DESCRIPTION                                                                                      |
|:-----------------| :--: | :--: | :----: |:-------------------------------------------------------------------------------------------------|
| Protocol Version | 0xFF | 0x01 |   1    | ipso_version(1B)                                                                                 |
| Device Status    | 0xFF | 0x0B |   1    | device_status(1B)                                                                                |
| Serial Number    | 0xFF | 0x16 |   8    | sn(8B)                                                                                           |
| Hardware Version | 0xFF | 0x09 |   2    | hardware_version(2B)                                                                             |
| Firmware Version | 0xFF | 0x0A |   2    | firmware_version(2B)                                                                             |
| TSL Version      | 0xFF | 0xFF |   2    | tsl_version(2B)                                                                                  |
| Battery          | 0x01 | 0x75 |   1    | battery(1B)                                                                                      |
| Occupancy        | 0x03 | 0x00 |   1    | occupancy(1B)<br />occupancy, values: (0: vacant, 1: occupied)                                   |
| Illuminance      | 0x04 | 0x00 |   1    | illuminance(1B)<br />illuminance, values: (0: dim, 1: bright, 0xFE: disable)                     |