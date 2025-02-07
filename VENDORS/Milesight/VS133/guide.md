
## Payload Definition

|          CHANNEL           |  ID  | TYPE | LENGTH | DESCRIPTION                                                                       |
| :------------------------: | :--: | :--: | :----: | --------------------------------------------------------------------------------- |
|   Total In<br/>(Line 1)    | 0x03 | 0xD2 |   4    | line_1_total_in(4B)                                                               |
|   Total Out<br/>(Line 1)   | 0x04 | 0xD2 |   4    | line_1_total_out(4B)                                                              |
| Period IN/OUT<br/>(Line 1) | 0x05 | 0xCC |   4    | line_1_period_in(2B) + line_1_period_out(2B)                                      |
|   Total In<br/>(Line 2)    | 0x06 | 0xD2 |   4    | line_2_total_in(4B)                                                               |
|   Total Out<br/>(Line 2)   | 0x07 | 0xD2 |   4    | line_2_total_out(4B)                                                              |
| Period IN/OUT<br/>(Line 2) | 0x08 | 0xCC |   4    | line_2_period_in(2B) + line_2_period_out(2B)                                      |
|   Total In<br/>(Line 3)    | 0x09 | 0xD2 |   4    | line_3_total_in(4B)                                                               |
|   Total Out<br/>(Line 3)   | 0x0A | 0xD2 |   4    | line_3_total_out(4B)                                                              |
| Period IN/OUT<br/>(Line 3) | 0x0B | 0xCC |   4    | line_3_period_in(2B) + line_3_period_out(2B)                                      |
|   Total In<br/>(Line 4)    | 0x0C | 0xD2 |   4    | line_4_total_in(4B)                                                               |
|   Total Out<br/>(Line 4)   | 0x0D | 0xD2 |   4    | line_4_total_out(4B)                                                              |
| Period IN/OUT<br/>(Line 4) | 0x0E | 0xCC |   4    | line_4_period_in(2B) + line_4_period_out(2B)                                      |
|        Region Count        | 0x0F | 0xE3 |   4    | region_1_count(1B) + region_2_count(1B) + region_3_count(1B) + region_4_count(1B) |
|         Dwell Time         | 0x10 | 0xE4 |   5    | region(1B) + region_avg_dwell(2B) + region_max_dwell(2B)                          |