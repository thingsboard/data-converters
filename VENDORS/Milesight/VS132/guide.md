# 3D ToF People Counting Sensor - Milesight IoT

The payload decoder function is applicable to VS132.

## Payload Definition

|     CHANNEL      |  ID  | TYPE | LENGTH | DESCRIPTION                                        |
| :--------------: | :--: | :--: | :----: | -------------------------------------------------- |
| Protocol Version | 0xFF | 0x01 |   1    | protocol_version(1B)                               |
|  Serial Number   | 0xFF | 0x16 |   8    | sn(8B)                                             |
| Hardware Version | 0xFF | 0x09 |   2    | hardware_version(2B)                               |
| Firmware Version | 0xFF | 0x1F |   4    | firmware_version(4B)                               |
|     Total IN     | 0x03 | 0xD2 |   4    | total_counter_in(4B)                               |
|    Total OUT     | 0x04 | 0xD2 |   4    | total_counter_out(4B)                              |
|  Period IN/OUT   | 0x05 | 0xCC |   4    | periodic_counter_in(2B) + periodic_counter_out(2B) |
