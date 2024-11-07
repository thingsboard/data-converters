# Elsys ERS Device Data Types Guide

This guide explains the data types used in the Elsys ERS2 device payloads. Each data type represents a specific measurement with its own unique identifier, size, and range.

## Data Types

| Type Value | Type                | Data Size (Bytes) | Range / Units                               | Description                                                                                     |
|------------|----------------------|--------------------|---------------------------------------------|-------------------------------------------------------------------------------------------------|
| `0x01`     | Temperature          | 2                  | -3276.5 °C to 3276.5 °C                    | Temperature data. Each value of `100` represents `10.0 °C`.                                    |
| `0x02`     | Humidity             | 1                  | 0 to 100 %                                 | Relative humidity as a percentage.                                                              |
| `0x07`     | VDD (Battery Voltage)| 2                  | 0 to 65535 mV                              | Battery voltage measured in millivolts (mV).                                                    |
| `0x3D`     | Debug Information    | 4                  | Depends on debug info                      | Information for debugging, which varies based on the data included by the device.               |
| `0x3E`     | Sensor Settings      | n (variable)       | Sent at startup (Port + 1)                 | Device settings sent to the server upon startup. This is sent only once on Port + 1.            |

## Detailed Descriptions

- **Temperature (`0x01`)**: Represented in 2 bytes, with a range of -3276.5 °C to 3276.5 °C. Each value increment of `100` corresponds to an increase of `10.0 °C`.

- **Humidity (`0x02`)**: Represented in 1 byte, with a range of 0 to 100%. This is the relative humidity measured by the device.

- **Light (`0x04`)**: Represented in 2 bytes, with a range of 0 to 65535 Lux. This value indicates the intensity of ambient light.

- **Motion (PIR) (`0x05`)**: Represented in 1 byte, with a range of 0 to 255. This indicates the count of motions detected by the PIR sensor since the last transmission.

- **Battery Voltage (VDD) (`0x07`)**: Represented in 2 bytes, with a range of 0 to 65535 mV. This value shows the current battery voltage of the device.

- **Debug Information (`0x3D`)**: Represented in 4 bytes. This information depends on the device’s specific debug configuration and is intended for troubleshooting or debugging purposes.

- **Sensor Settings (`0x3E`)**: Variable size, represented by `n` bytes. This data is sent once to the server during device startup (first package) and is sent on Port + 1. It contains the sensor's configuration settings.

---

This guide provides an overview of each data type and its intended use. Make sure to handle each type accordingly when decoding payloads from the Elsys ERS2 device.
