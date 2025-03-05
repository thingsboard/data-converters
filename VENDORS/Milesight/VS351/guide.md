Mini AI Thermopile People Counter - Milesight IoT

The payload decoder function is applicable to VS351.

## Payload Definition

|       CHANNEL       |  ID  | TYPE | LENGTH  | DESCRIPTION                                                                                                                                                                                         |
| :-----------------: | :--: | :--: | :-----: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  Protocol Version   | 0xFF | 0x01 |    1    | protocol_version(1B)                                                                                                                                                                                |
|    Serial Number    | 0xFF | 0x08 |    6    | sn(6B)                                                                                                                                                                                              |
|  Hardware Version   | 0xFF | 0x09 |    2    | hardware_version(2B)                                                                                                                                                                                |
|  Firmware Version   | 0xFF | 0x1F |    4    | firmware_version(4B)                                                                                                                                                                                |
|       Battery       | 0x01 | 0x75 |    1    | battery(1B)<br/>battery, read: uint8, unit：%                                                                                                                                                       |
|     Temperature     | 0x03 | 0x67 |    2    | temperature(2B)<br/>temperature, read: int16/10, unit: ℃                                                                                                                                            |
|    Total IN/OUT     | 0x04 | 0xCC |    4    | total_in(2B) + total_out(2B)                                                                                                                                                                        |
|    Period IN/OUT    | 0x05 | 0xCC |    4    | period_in(2B) + period_out(2B)                                                                                                                                                                      |
|  Temperature Alarm  | 0x83 | 0x67 |    3    | temperature(2B) + temperature_alarm(1B)<br/>temperature_alarm, values: (0: threshold alarm release, 1: threshold alarm, 3: high temperature alarm, 4: high temperature alarm release)               |
| Total IN/OUT Alarm  | 0x84 | 0xCC |    5    | total_in(2B) + total_out(2B) + total_count_alarm(1B)<br/>total_count_alarm, values: (1: threshold alarm)                                                                                            |
| Period IN/OUT Alarm | 0x85 | 0xCC |    5    | period_in(2B) + period_out(2B) + period_count_alarm(1B)<br/>period_count_alarm, values: (1: threshold alarm)                                                                                        |
|   Historical Data   | 0x20 | 0xCE | 9 or 13 | timestamp(4B) + data_type(1B) + period_in(2B) + period_out(2B) + total_in(2B) + total_out(2B)<br/>data_type, values: (0: period_in + period_out, 1: period_in + period_out + total_in + total_out ) |