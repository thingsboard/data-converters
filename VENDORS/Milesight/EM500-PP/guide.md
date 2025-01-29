# Pipe Pressure Sensor - Milesight IoT

The payload decoder function is applicable to EM500-PP.

## Payload Definition

|     CHANNEL      |  ID  | TYPE | LENGTH | DESCRIPTION                     |
|:----------------:| :--: | :--: | :----: | ------------------------------- |
|     Battery      | 0x01 | 0x75 |   1    | battery(1B)<br/>battery, unit: % |
|     Pressure     | 0x03 | 0x7B |   2    | pressure(2B)<br/>pressure, unit: kPa |
| Historical Data  | 0x20 | 0XCE |   6    | timestamp(4B) + pressure(2B) |