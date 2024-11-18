# Data Payload Description for SensiLoRa 2.0

|        CHANNEL        | LENGTH | DESCRIPTION                                                                                     |
| :-------------------: | :----: | ----------------------------------------------------------------------------------------------- |
|        Battery        |   2    | Battery voltage (2 bytes), unit: Volts (divide by 100)                                          |
|      Temperature      |   2    | Temperature (2 bytes), unit: ℃ (divide by 100)                                                 |
|       Humidity        |   2    | Humidity (2 bytes), unit: %RH (divide by 100)                                                  |
|   Acceleration X      |   2    | Acceleration in the X axis (2 bytes), unit: m/s²                                               |
|   Acceleration Y      |   2    | Acceleration in the Y axis (2 bytes), unit: m/s²                                               |
|   Acceleration Z      |   2    | Acceleration in the Z axis (2 bytes), unit: m/s²                                               |
|        Gyro X         |   2    | Gyroscope data in the X axis (2 bytes), unit: rad/s                                            |
|        Gyro Y         |   2    | Gyroscope data in the Y axis (2 bytes), unit: rad/s                                            |
|        Gyro Z         |   2    | Gyroscope data in the Z axis (2 bytes), unit: rad/s                                            |
|   Magnetometer X      |   2    | Magnetometer data in the X axis (2 bytes), unit: µT                                            |
|   Magnetometer Y      |   2    | Magnetometer data in the Y axis (2 bytes), unit: µT                                            |
|   Magnetometer Z      |   2    | Magnetometer data in the Z axis (2 bytes), unit: µT                                            |
|      Light Level      |   2    | Light intensity (2 bytes), raw value                                                          |
|       Pressure        |   2    | Pressure (2 bytes), unit: hPa (divide by 10)                                                  |