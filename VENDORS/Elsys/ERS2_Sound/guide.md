# Elsys ERS2 Device Data Types Guide

This guide outlines the data types used in the Elsys ERS2 device payloads. Each data type is identified by a unique type value and includes specific details about the data it represents, including its size and comments for interpretation.

## Data Types

| Type Value | Type                | Data Size (Bytes) | Comment                                                                           |
|------------|---------------------|--------------------|-----------------------------------------------------------------------------------|
| `0x01`     | Temperature         | 2                  | -3276.5 °C to 3276.5 °C (Value of: 100 → 10.0 °C)                                 |
| `0x02`     | Humidity            | 1                  | 0 to 100%                                                                        |
| `0x04`     | Light               | 2                  | 0 to 65535 Lux                                                                   |
| `0x05`     | Motion (PIR)        | 1                  | 0 to 255 (Number of motion counts)                                               |
| `0x07`     | VDD (Battery voltage)| 2                  | 0 to 65535 mV                                                                    |
| `0x15`     | Sound               | 2                  | Sound data: 1 byte for peak value, 1 byte for average dB                         |
| `0x3D`     | Debug Information   | 4                  | Data depends on debug information                                                |
| `0x3E`     | Sensor Settings     | n (variable)       | Sensor settings sent to server at startup (first package). Sent on Port + 1.     |

## Detailed Descriptions

- **Temperature (0x01)**: Represented in 2 bytes, with a range of -3276.5 °C to 3276.5 °C. Each value increment of `100` corresponds to an increase of `10.0 °C`.

- **Humidity (0x02)**: Represented in 1 byte, with a range of 0 to 100%. This is the relative humidity measured by the device.

- **Light (0x04)**: Represented in 2 bytes, with a range of 0 to 65535 Lux. This value indicates the intensity of ambient light.

- **Motion (PIR) (0x05)**: Represented in 1 byte, with a range of 0 to 255. This indicates the count of motions detected by the PIR sensor since the last transmission.

- **Battery Voltage (VDD) (0x07)**: Represented in 2 bytes, with a range of 0 to 65535 mV. This value shows the current battery voltage of the device.

- **Sound (0x15)**: Represented in 2 bytes. Contains 1 byte for the peak value and 1 byte for the average decibel (dB) level.

- **Debug Information (0x3D)**: Represented in 4 bytes. This information depends on the device’s specific debug configuration and is intended for troubleshooting or debugging purposes.

- **Sensor Settings (0x3E)**: Variable size, represented by `n` bytes. This data is sent once to the server during device startup (first package) and is sent on Port + 1. It contains the sensor's configuration settings.

---
