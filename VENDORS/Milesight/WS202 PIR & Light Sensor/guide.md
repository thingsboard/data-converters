
## Payload Definition

| CHANNEL  |  ID  | TYPE | LENGTH | DESCRIPTION                                            |
| :------: | :--: | :--: | :----: | ------------------------------------------------------ |
| Battery  | 0x01 | 0x75 |   1    | battery(1B)<br/>battery, unit: %                       |
|   PIR    | 0x03 | 0x00 |   1    | pir(1B)<br/>pir, values: (0: normal, 1: trigger)       |
| Daylight | 0x04 | 0x00 |   1    | daylight(1B)<br/>daylight, values: (0: dark, 1: light) |

## Example

```json
// 017510 030001 040000
{
    "battery": 16,
    "pir": "trigger",
    "daylight": "dark"
}
```
