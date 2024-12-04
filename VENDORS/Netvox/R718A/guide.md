# Device Guide for R718A (Netvox)

## Overview

This document provides detailed information about the payload definition, configurations, and examples of uplink and downlink messages for the **R718A Netvox** device.

---

## 5.1 Example of `ReportDataCmd` (FPort: 0x06)

### Payload Structure

| Bytes  | Length  | Field           | Description                                                            |
|--------|---------|-----------------|------------------------------------------------------------------------|
| 1      | 1 byte  | Version         | The version of the Netvox LoRaWAN Application Command. Example: `0x01`. |
| 2      | 1 byte  | DeviceType      | Device type identifier. Example: `0x0B` for R718A.                     |
| 3      | 1 byte  | ReportType      | Type of report: `0x00` for version, `0x01` for sensor data.            |
| 4-11   | 8 bytes | NetvoxPayLoadData | Contains various data depending on the `ReportType`.                   |

---

### Details of `NetvoxPayLoadData`

#### For `ReportType = 0x00` (Version Information)

| Field            | Length   | Description                              |
|------------------|----------|------------------------------------------|
| SoftwareVersion  | 1 byte   | Version of the software. Example: `0x0A` (V1.0). |
| HardwareVersion  | 1 byte   | Version of the hardware. Example: `0x0A` (V1.0). |
| DateCode         | 4 bytes  | Manufacturing date. Example: `0x20170503` (2017-05-03). |
| Reserved         | 2 bytes  | Fixed value: `0x0000`.                   |

#### For `ReportType = 0x01` (Sensor Data)

| Field            | Length   | Description                              |
|------------------|----------|------------------------------------------|
| Battery          | 1 byte   | Battery level in 0.1V units. Example: `0x24` → 3.6V. |
| Temperature      | 2 bytes  | Signed value in 0.01°C units. Example: `0x0670` → 16.48°C. |
| Humidity         | 2 bytes  | Unsigned value in 0.01% units. Example: `0x1A9E` → 68.14%. |
| Reserved         | 3 bytes  | Fixed value: `0x000000`.                 |

---

## Report Configuration (FPort: 0x07)

### Payload Structure

| Bytes  | Length  | Field           | Description                                                 |
|--------|---------|-----------------|-------------------------------------------------------------|
| 1      | 1 byte  | CmdID           | Command ID. Example: `0x01` for configuration request.       |
| 2      | 1 byte  | DeviceType      | Device Type. Example: `0x13` for R718AB.                    |
| 3–11   | Var (9 bytes) | NetvoxPayLoadData | Variable payload for configuration settings (max 9 bytes).   |

---

### Details of `NetvoxPayLoadData`

#### Configuration Payload Fields

| Field              | Length   | Description                                  |
|--------------------|----------|----------------------------------------------|
| MinTime            | 2 bytes  | Minimum reporting interval in seconds.       |
| MaxTime            | 2 bytes  | Maximum reporting interval in seconds.       |
| BatteryChange      | 1 byte   | Change in battery level to trigger reporting (unit: 0.1V). |
| TemperatureChange  | 2 bytes  | Change in temperature to trigger reporting (unit: 0.01°C). |
| HumidityChange     | 2 bytes  | Change in humidity to trigger reporting (unit: 0.01%).      |
| Reserved           | 8 bytes  | Fixed value: `0x0000000000000000` (for `ConfigReportRsp`).   |

---

### Commands and Responses

| Description          | CmdID | DeviceType | NetvoxPayLoadData                                          |
|----------------------|-------|------------|-----------------------------------------------------------|
| **ConfigReport Rsp** | 0x81  | 0x0B       | Status (`0x00` for success) + Reserved (8 bytes).         |
| **ReadConfigReportRsp** | 0x82 | 0x0B       | `MinTime` + `MaxTime` + `BatteryChange` + `TemperatureChange` + `HumidityChange`. |

---

## Example of GlobalCalibrateCmd (FPort: 0x0E)

### Payload Structure

| Description           | CmdID | Sensor Type | PayLoad (Fixed = 9 Bytes)                                      |
|-----------------------|-------|-------------|---------------------------------------------------------------|
| **SetGlobalCalibrateRsp** | 0x81  | See below   | Channel (1 Byte) + Status (1 Byte, 0x00 = success) + Reserved (7 Bytes, fixed 0x00). |
| **GetGlobalCalibrateRsp** | 0x82  | See below   | Channel (1 Byte) + Multiplier (2 Bytes) + Divisor (2 Bytes) + DeltValue (2 Bytes) + Reserved (2 Bytes, fixed 0x00). |
| **ClearGlobalCalibrateRsp** | 0x83  | See below   | Status (1 Byte, 0x00 = success) + Reserved (9 Bytes, fixed 0x00). |

---

### Sensor and Channel Details

| Field                | Length  | Description                                  |
|----------------------|---------|----------------------------------------------|
| **Channel**          | 1 Byte  | Sensor channel: 0x00 (Temperature), 0x01 (Humidity). |
| **Multiplier**       | 2 Bytes | Calibration multiplier (unsigned).           |
| **Divisor**          | 2 Bytes | Calibration divisor (unsigned).              |
| **DeltValue**        | 2 Bytes | Calibration offset value (signed).           |
| **Reserved**         | Var     | Fixed bytes reserved for command responses.  |

---

## Example of Set/GetSensorAlarmThresholdCmd (FPort: 0x10)

### Payload Structure

| Field                | Length  | Description                                                                                  |
|----------------------|---------|----------------------------------------------------------------------------------------------|
| CmdID               | 1 Byte  | Command ID. Indicates the type of alarm threshold command.                                    |
| Payload             | 10 Bytes | Contains channel, sensor type, thresholds, and reserved fields.                              |

---

### Command Descriptions

| CmdDescriptor                  | CmdID  | Payload Structure                                                                                  |
|--------------------------------|--------|----------------------------------------------------------------------------------------------------|
| **SetSensorAlarmThresholdRsp** | `0x81` | Status (1 Byte) + Reserved (9 Bytes, fixed `0x00`).                                               |
| **GetSensorAlarmThresholdRsp** | `0x82` | Channel (1 Byte) + SensorType (1 Byte) + SensorHighThreshold (4 Bytes) + SensorLowThreshold (4 Bytes). |

---

### Details of Payload Fields

#### Threshold Response (`SetSensorAlarmThresholdRsp`)

| Field                | Length  | Description                                                                                  |
|----------------------|---------|----------------------------------------------------------------------------------------------|
| Status               | 1 Byte  | Status of the command: `0x00` (Success).                                                     |
| Reserved             | 9 Bytes | Fixed reserved value: `0x000000000000000000`.                                                |

#### Threshold Response (`GetSensorAlarmThresholdRsp`)

| Field                | Length  | Description                                                                                  |
|----------------------|---------|----------------------------------------------------------------------------------------------|
| Channel              | 1 Byte  | Sensor channel: `0x00` (Channel 1), `0x01` (Channel 2), etc.                                 |
| SensorType           | 1 Byte  | Sensor type: `0x00` (Disable All Thresholds), `0x01` (Temperature), `0x02` (Humidity).       |
| SensorHighThreshold  | 4 Bytes | Upper threshold for the sensor. Units: `0.01°C` for temperature, `0.01%` for humidity.       |
| SensorLowThreshold   | 4 Bytes | Lower threshold for the sensor. Units: `0.01°C` for temperature, `0.01%` for humidity.       |

---

## Example of NetvoxLoRaWANRejoin Command (FPort: 0x20)

The `NetvoxLoRaWANRejoin` command checks if the device is still in the network. If the device is disconnected, it will automatically rejoin the network.

---

### Payload Structure

| Field                | Length  | Description                                                                                  |
|----------------------|---------|----------------------------------------------------------------------------------------------|
| CmdID               | 1 Byte  | Command ID. Indicates the type of rejoin command.                                             |
| Payload             | 5 Bytes | Contains `RejoinCheckPeriod`, `RejoinThreshold`, and reserved fields.                        |

---

### Command Descriptions

| CmdDescriptor                  | CmdID  | Payload Structure                                                                                  |
|--------------------------------|--------|----------------------------------------------------------------------------------------------------|
| **SetNetvoxLoRaWANRejoinRsp**  | `0x81` | `Status` (1 Byte) + Reserved (4 Bytes, fixed `0x00`).                                              |
| **GetNetvoxLoRaWANRejoinRsp**  | `0x82` | `RejoinCheckPeriod` (4 Bytes) + `RejoinThreshold` (1 Byte).                                       |

---

### Details of Payload Fields

| Field                | Length  | Description                                                                                  |
|----------------------|---------|----------------------------------------------------------------------------------------------|
| RejoinCheckPeriod    | 4 Bytes | Period for rejoin check in seconds (unit: 1s). `0xFFFFFFFF` disables the rejoin function.    |
| RejoinThreshold      | 1 Byte  | Threshold value for rejoining the network.                                                   |
| Status               | 1 Byte  | Status of the command: `0x00` (Success).                                                     |
| Reserved             | Var     | Fixed reserved value for padding (e.g., `0x00000000` for responses).                        |

---


