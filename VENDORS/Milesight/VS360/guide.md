# IR Breakbeam People Counter - Milesight IoT

The payload decoder function is applicable to VS360.

## Payload Definition

| CHANNEL             |  ID  | TYPE | LENGTH | DESCRIPTION                                                                                                                                                                                          |
| :------------------ | :--: | :--: | :----: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Protocol Version    | 0xFF | 0x01 |   1   | ipso_version(1B)                                                                                                                                                                                     |
| Device Status       | 0xFF | 0x0B |   1   | device_status(1B)                                                                                                                                                                                    |
| Serial Number       | 0xFF | 0x16 |   8   | sn(8B)                                                                                                                                                                                               |
| Hardware Version    | 0xFF | 0x09 |   2   | hardware_version(2B)                                                                                                                                                                                 |
| Firmware Version    | 0xFF | 0x0A |   2   | firmware_version(2B)                                                                                                                                                                                 |
| TSL Version         | 0xFF | 0xFF |   2   | tsl_version(2B)                                                                                                                                                                                      |
| LoRaWAN Class       | 0xFF | 0x0F |   1   | lorawan_class(1B)<br />lorawan_class, values: (0: classA, 1: classB, 2: classC, 3: classCtoB)                                                                                                        |
| Battery(Main)       | 0x01 | 0x75 |   1   | battery_main(1B)<br />battery_main, read: uint8, unit：%                                                                                                                                             |
| Battery(Node)       | 0x02 | 0x75 |   1   | battery_node(1B)<br />battery_node, read: uint8, unit：%                                                                                                                                             |
| Event               | 0x03 | 0xF4 |   2   | event_type(1B) + event_status(1B)<br />event_type, values: (0: counting anomaly, 1: node device without response, 2:devices misaligned)<br />event_status, values: (0: alarm release, 1: alarm)      |
| Total IN/OUT        | 0x04 | 0xCC |   4   | total_in(2B) + total_out(2B)                                                                                                                                                                         |
| Period IN/OUT       | 0x05 | 0xCC |   4   | period_in(2B) + period_out(2B)                                                                                                                                                                       |
| Total IN/OUT Alarm  | 0x84 | 0xCC |   5   | total_in(2B) + total_out(2B) + total_count_alarm(1B)<br />total_count_alarm, values: (1: threshold alarm)                                                                                            |
| Period IN/OUT Alarm | 0x85 | 0xCC |   5   | period_in(2B) + period_out(2B) + period_count_alarm(1B)<br />period_count_alarm, values: (1: threshold alarm)                                                                                        |
| Historical Data     | 0x20 | 0xCE | 9 / 13 | timestamp(4B) + data_type(1B) + period_in(2B) + period_out(2B) + total_in(2B) + total_out(2B)<br />data_type, values: (0: period_in + period_out, 1: period_in + period_out + total_in + total_out ) |