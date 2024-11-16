# Insertion Temperature Sensor - Milesight IoT

The payload decoder function is applicable to TS101.

## Payload Definition

| **Item**                 | **Channel** | **Type** | **Description**                                                                 |
|--------------------------|-------------|----------|---------------------------------------------------------------------------------|
| **Battery Level**        | 01          | 75       | UINT8, Unit: %                                                                  |
| **Temperature**          | 03          | 67       | INT16/10, Unit: °C, Resolution: 0.1°C                                          |
| **Threshold Alarm**      | 83          | 67       | 3 Bytes, Temperature(2B) + 01<br>Temperature: INT16/10, Unit: °C               |
| **Mutation Threshold Alarm** | 93      | d7       | 5 Bytes, Temperature(2B) + Mutation Value(2B) + 02<br>Temperature: INT16/10, Unit: °C<br>Mutation Value: INT16/100, Unit: °C |