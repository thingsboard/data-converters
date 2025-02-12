# AI Workplace Occupancy Sensor - Milesight IoT

The payload decoder function is applicable to VS121.

![VS121](VS121.png)

## Payload Definition

|       CHANNEL        |  ID  | TYPE | LENGTH | DESCRIPTION                                               |
| :------------------: | :--: | :--: | :----: | --------------------------------------------------------- |
|   Protocol Version   | 0xFF | 0x01 |   1    | protocol_version(1B)                                      |
|    Serial Number     | 0xFF | 0x08 |   6    | sn(6B)                                                    |
|   Hardware Version   | 0xFF | 0x09 |   2    | hardware_version(2B)                                      |
|   Firmware Version   | 0xFF | 0x1F |   4    | firmware_version(4B)                                      |
|     People Count     | 0x04 | 0xC9 |   4    | people_count_all(1B) + region_count(1B) + region_mask(2B) |
|    People Passing    | 0x05 | 0xCC |   4    | people_in(2B) + people_out(2B)                            |
|      People Max      | 0x06 | 0xCD |   1    | people_count_max(1B)                                      |
|  Region Count(1-8)   | 0x07 | 0xD5 |   8    | region_1(1B) + region_2(1B) + ... + region_8(1B)          |
|  Region Count(9-16)  | 0x08 | 0xD5 |   8    | region_9(1B) + region_10(1B) + ... + region_16(1B)        |
|        A flow        | 0x09 | 0xDA |   8    | AtoA(2B) + AtoB(2B) + ... + AtoD(2B)                      |
|        B flow        | 0x0A | 0xDA |   8    | BtoA(2B) + BtoB(2B) + ... + BtoD(2B)                      |
|        C flow        | 0x0B | 0xDA |   8    | CtoA(2B) + CtoB(2B) + ... + CtoD(2B)                      |
|        D flow        | 0x0C | 0xDA |   8    | DtoA(2B) + DtoB(2B) + ... + DtoD(2B)                      |
|        D flow        | 0x0C | 0xDA |   8    | DtoA(2B) + DtoB(2B) + ... + DtoD(2B)                      |
| People Total Passing | 0x0D | 0xCC |   4    | people_total_in(2B) + people_total_out(2B)                |
|      Dwell Time      | 0x0E | 0xE4 |   5    | id(1B) + dwell_avg(2B) + dwell_max(2B)                    |
|      Timestamp       | 0x0F | 0x85 |   4    | timestamp(4B)                                             |
