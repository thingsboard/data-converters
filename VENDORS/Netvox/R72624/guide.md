# ReportDataCmd Documentation

## Overview
This document provides detailed information about the `ReportDataCmd` used in the Netvox LoRaWAN application. The structure, fields, and decoding examples are applicable to multiple devices. Specific device types may have unique implementations of `NetvoxPayLoadData`.

## Command Format
- **FPort**: `0x06`

### Data Structure
| Bytes        | 1       | 1          | 1          | Var (Fixed: 8 Bytes)            |
|--------------|---------|------------|------------|---------------------------------|
| Field        | Version | DeviceType | ReportType | NetvoxPayLoadData              |
---

## Common Fields in `NetvoxPayLoadData`

| Field          | Size          | Unit           | Description                            |
|-----------------|---------------|----------------|----------------------------------------|
| **Battery**     | 1 Byte        | 0.1V           | Battery level of the device.           |
| **CO2**         | 2 Bytes       | 0.1ppm         | CO2 concentration.                     |
| **NH3**         | 2 Bytes       | 0.1ppm         | Ammonia (NH3) concentration.           |
| **Noise**       | 2 Bytes       | 0.1dB          | Noise level.                           |
| **Temperature** | 2 Bytes (Signed) | 0.01°C       | Temperature measurement.               |
| **Humidity**    | 2 Bytes       | 0.01%          | Humidity level.                        |
| **WindSpeed**   | 2 Bytes       | 0.01m/s        | Wind speed measurement.                |
| **Reserved**    | 1 Byte        | Fixed `0x00`   | Reserved for future use.               |

---

## Device-Specific Implementation

### Example: R72624
| Description  | Device Type | Report Type | NetvoxPayLoadData Fields                     |
|--------------|-------------|-------------|---------------------------------------------|
| **R72623**   | `0x09`      | `0x07`      | **Battery**, **CO2**, **NH3**, **Noise**, **Reserved** |

### Example: R72624
| Description  | Device Type | Report Type | NetvoxPayLoadData Fields                     |
|--------------|-------------|-------------|---------------------------------------------|
| **RA0723Y**  | `0x09`      | `0x0C`      | **Battery**, **Temperature**, **Humidity**, **WindSpeed**, **Reserved** |

---

# ConfigureCmd Documentation

## Overview
This document provides details about the `ConfigureCmd` used in the Netvox LoRaWAN application. It describes the structure, fields, and payload decoding examples for configuring and retrieving device settings.

## Command Format
- **FPort**: `0x07`

### Data Structure
| Bytes        | 1       | 1          | Var (Fixed: 9 Bytes)            |
|--------------|---------|------------|---------------------------------|
| Field        | CmdID   | DeviceType | NetvoxPayLoadData              |

---

## Device-Specific Implementation

### Command Descriptions

| Description            | CmdID  | Device Type | NetvoxPayLoadData Fields                        |
|------------------------|--------|-------------|------------------------------------------------|
| **ConfigReportRsp**    | `0x81` | `0x09`      | **Status**, **Reserved**                        |
| **ReadConfigReportRsp** | `0x82` | `0x09`      | **MinTime**, **MaxTime**, **Reserved**          |

---

### Payload Field Details

| Field          | Size           | Unit           | Description                            |
|-----------------|----------------|----------------|----------------------------------------|
| **MinTime**     | 2 Bytes        | Seconds        | Minimum reporting interval.            |
| **MaxTime**     | 2 Bytes        | Seconds        | Maximum reporting interval.            |
| **Status**      | 1 Byte         | -              | Indicates the success of the configuration (e.g., `0x00` = success). |
| **Reserved**    | 5–9 Bytes      | Fixed `0x00`   | Reserved for future use.               |

---

# GlobalCalibrateCmd Documentation

## Overview
This document describes the `GlobalCalibrateCmd` used in the Netvox LoRaWAN application. This command allows calibration of specific sensor channels and retrieval of calibration parameters. The payload structure and examples for encoding/decoding are provided below.

## Command Format
- **FPort**: `0x0E`

### Data Structure
| Bytes        | 1       | 1          | Var (Fixed: 9 Bytes)            |
|--------------|---------|------------|---------------------------------|
| Field        | CmdID   | SensorType | Payload                        |

---

## Sensor Types
| Sensor Type Code | Description             |
|------------------|-------------------------|
| `0x01`           | Temperature Sensor      |
| `0x02`           | Humidity Sensor         |
| `0x18`           | Noise Sensor            |

---

## Command Descriptions

| Description                   | CmdID  | Sensor Type | Payload Fields                              |
|-------------------------------|--------|-------------|---------------------------------------------|
| **SetGlobalCalibrateRsp**      | `0x81` | Sensor Type | **Channel**, **Status**, **Reserved**       |
| **GetGlobalCalibrateRsp**      | `0x82` | Sensor Type | **Channel**, **Multiplier**, **Divisor**, **DeltValue**, **Reserved** |

---

## Payload Field Details

| Field          | Size           | Type          | Description                            |
|-----------------|----------------|---------------|----------------------------------------|
| **Channel**     | 1 Byte         | Unsigned      | Sensor channel ID (e.g., `0_Channel1`, `1_Channel2`). |
| **Multiplier**  | 2 Bytes        | Unsigned      | Calibration multiplier.                |
| **Divisor**     | 2 Bytes        | Unsigned      | Calibration divisor.                   |
| **DeltValue**   | 2 Bytes        | Signed        | Delta value for calibration adjustments. |
| **Status**      | 1 Byte         | Unsigned      | Calibration response status (`0x00` = Success). |
| **Reserved**    | 2–8 Bytes      | Fixed `0x00`  | Reserved for future use.               |

---