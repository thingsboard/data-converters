# ReportDataCmd Documentation

## Overview
This document describes the structure and details of the `ReportDataCmd` used in the Netvox LoRaWAN application. Below is a breakdown of the data structure, examples, and additional tips for decoding the payload.

## Command Format
- **FPort**: `0x06`

### Data Structure
| Bytes        | 1        | 1          | 1          | Var (Fixed: 8 Bytes) |
|--------------|----------|------------|------------|----------------------|
| Field        | Version  | DeviceType | ReportType | NetvoxPayLoadData   |

---

## Device-Specific Example: R311A

| Device   | Device Type | Report Type | NetvoxPayLoadData                          |
|----------|------------|-------------|--------------------------------------------|
| R311A    | `0x02`     | `0x00`      | **SoftwareVersion**: 1 Byte (e.g., `0x0A` - `V1.0`), **HardwareVersion**: 1 Byte, **DateCode**: 4 Bytes (e.g., `0x20170503`), **Reserved**: 2 Bytes (Fixed `0x00`). |
| R311A    |  `0x02`    | `0x01`      | **Battery**: 1 Byte (unit: 0.1V), **ContactSwitchOnOff**: 1 Byte (`0x01`: On), **Reserved**: 6 Bytes (Fixed `0x00`). |

---

# ConfigureCmd Documentation

## Overview
This document provides information about the `ConfigureCmd` used in the Netvox LoRaWAN application. Below are the details regarding the structure, examples, and decoding of the `ConfigureCmd`.

## Command Format
- **FPort**: `0x07`

### Data Structure
| Bytes        | 1       | 1          | Var (Fixed: 9 Bytes)            |
|--------------|---------|------------|---------------------------------|
| Field        | CmdID   | DeviceType | NetvoxPayLoadData              |

## Device-Specific Example: R311A

| Description  | Device   | Cmd ID  | Device Type | NetvoxPayLoadData                                                        |
|--------------|----------|---------|-------------|---------------------------------------------------------------------------|
| **ConfigRsp**| R311A    | `0x81`  | `0x02`      | **Status** (1 Byte: `0x00` = success), **Reserved** (8 Bytes, Fixed `0x00`). |
| **ReadConfigRsp** | R311A | `0x82` | `0x02`      | **MinTime** (2 Bytes, Units: seconds), **MaxTime** (2 Bytes, Units: seconds), **BatteryChange** (1 Byte, Unit: 0.1V), **Reserved** (4 Bytes, Fixed `0x00`). |

---

# OnOffStateDuration Documentation

## Overview
This document provides detailed information about the `OnOffStateDuration` command used in the Netvox LoRaWAN application. Below are the descriptions, structure, and examples of the payloads for configuring and retrieving on/off state durations.

## Command Format
- **FPort**: `0x07`

### Data Structure
| Bytes        | 1       | 1          | Var (Fixed: 9 Bytes)            |
|--------------|---------|------------|---------------------------------|
| Field        | CmdID   | DeviceType | NetvoxPayLoadData              |

---

## Device-Specific Example: R311A

| Description                | Device   | Cmd ID  | Device Type | NetvoxPayLoadData                                                       |
|----------------------------|----------|---------|-------------|-------------------------------------------------------------------------|
| **SetOnOffStateDurationRsp** | R311A   | `0x83`  | `0x02`      | **Status** (1 Byte: `0x00` = success), **Reserved** (8 Bytes, Fixed `0x00`). |
| **GetOnOffStateDurationRsp** | R311A   | `0x84`  | `0x02`      | **OnStateDuration** (2 Bytes, Units: seconds), **OffStateDuration** (2 Bytes, Units: seconds), **Reserved** (5 Bytes, Fixed `0x00`). |

---

# LastMessageResendtime Documentation

## Overview
This document provides details about the `LastMessageResendtime` command used in the Netvox LoRaWAN application. It includes command descriptions, data structures, and examples for configuring and retrieving the last message resend time.

## Command Format
- **FPort**: `0x07`

### Data Structure
| Bytes        | 1       | 1          | Var (Fixed: 9 Bytes)            |
|--------------|---------|------------|---------------------------------|
| Field        | CmdID   | DeviceType | NetvoxPayLoadData              |

## Device-Specific Example: R311A

| Description                   | Device   | Cmd ID  | Device Type | NetvoxPayLoadData                                                       |
|-------------------------------|----------|---------|-------------|-------------------------------------------------------------------------|
| **SetLastMessageResendtimeRsp** | R311A   | `0x9F`  | `0xFF`      | **Status** (1 Byte: `0x00` = success), **Reserved** (8 Bytes, Fixed `0x00`). |
| **GetLastMessageResendtimeRsp** | R311A   | `0x9E`  | `0xFF`      | **Resendtime** (1 Byte, Units: seconds, Range: 3–254s), **Reserved** (8 Bytes, Fixed `0x00`). |



