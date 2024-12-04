# Magnetic Contact Switch - Milesight IoT

The payload decoder function is applicable to WS301.

## Payload Definition

|    CHANNEL    |  ID  | TYPE | LENGTH | DESCRIPTION                                                                 |
| :-----------: | :--: | :--: | :----: | --------------------------------------------------------------------------- |
|    Battery    | 0x01 | 0x75 |   1    | battery(1B)<br/>battery, unit: %                                            |
| Magnet Status | 0x03 | 0x00 |   1    | magnet_status(1B)<br/>state, values: (0: close, 1: open)                    |
| Tamper Status | 0x04 | 0x00 |   1    | tamper_status(1B)<br/>tamper_status, values: (0: installed, 1: uninstalled) |