## Payload Definition

|     CHANNEL     |  ID  | TYPE | LENGTH | DESCRIPTION                                    |
| :-------------: | :--: | :--: | :----: | ---------------------------------------------- |
|     Battery     | 0x01 | 0x75 |   1    | battery(1B)<br/>battery, unit: %               |
|   Temperature   | 0x03 | 0x67 |   2    | temperature(2B)<br/>temperature, unit: ℃       |
|    Humidity     | 0x04 | 0x68 |   1    | humidity(1B)<br/>humidity, unit: %RH           |
| Historical Data | 0x20 | 0xCE |   7    | timestamp(4B) + temperature(2B) + humidity(1B) |

## Example

```json
// 017564 03671801 04686D
{
    "battery": 100,
    "temperature": 28,
    "humidity": 54.5
}
```