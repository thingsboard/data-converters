# ReportDataCmd Format and Examples

## Overview

This document provides details on the **ReportDataCmd** structure for NetvoxLoRaWAN devices. Below is an example of the message structure sent via FPort `0x06`.

---

### Message Structure

| Bytes       | 1          | 1          | 1          | Var (Fixed = 8 Bytes) |
|-------------|------------|------------|------------|-----------------------|
| **Field**   | Version    | DeviceType | ReportType | NetvoxPayLoadData    |
| **Details** | 1 byte - Version of NetvoxLoRaWAN Application Command Version | 1 byte - Device Type of Device | 1 byte - Presentation of NetvoxPayLoadData (based on device type) | Fixed bytes (8 bytes) |

### Example Data Structure

#### Example for `R718H`

| Device  | Device Type | Report Type | NetvoxPayLoadData                                                       |
|---------|------------|-------------|--------------------------------------------------------------------------|
| R718H   | 0x1F       | 0x00        | SoftwareVersion (1 Byte, e.g., 0x0A → V1.0), HardwareVersion (1 Byte), DateCode (4 Bytes, e.g., 0x20170503), Reserved (2 Bytes, Fixed 0x00) |
|R718H    | 0x1F       | 0x01        | Battery (1 Byte, Unit: 0.1V), PulseCount (2 Bytes), Reserved (5 Bytes, Fixed 0x00) |

---

# ReportDataCmd Format and Examples (FPort: 0x07)

## Overview

This document describes the **ReportDataCmd** structure for FPort `0x07`. This command is used for configuring and reading device settings, as well as reporting configuration responses.

---

### Message Structure

| Bytes       | 1          | 1          | Var (Fixed = 9 Bytes) |
|-------------|------------|------------|-----------------------|
| **Field**   | CmdID      | DeviceType | NetvoxPayLoadData    |
| **Details** | 1 byte - Command ID    | 1 byte - Device Type of Device | Variable bytes (Max = 9 bytes) |

---

### NetvoxPayLoadData Structure

#### Configuration and Reporting Examples

| Description               | Device | Cmd ID | Device Type | NetvoxPayLoadData                                                                                          |
|---------------------------|--------|--------|---------|-----------------------------------------------------------------------------------------------------------|
| **Config ReportRsp**      |  R718H | 0x81   |  0x1F   | **Status** (0x00 = success), **Reserved** (8 bytes, Fixed 0x00)                                           |
| **ReadConfig ReportRsp**  |  R718H | 0x82   |  0x1F   | **MinTime** (2 bytes, Units: s), **MaxTime** (2 bytes, Units: s), **BatteryChange** (1 byte, Unit: 0.1V), **Reserved** (4 bytes, Fixed 0x00)|
| **SetFilter timeRsp**     | R718H  | 0x83   |             | **Status** (0x00 = success), **Reserved** (8 bytes, Fixed 0x00)                                           |
| **GetFilter timeRsp**     |  R718H | 0x84   |             | **FilterTime** (1 byte, Unit: 5ms), **Reserved** (8 bytes, Fixed 0x00)                                    |
| **SetPulseCounter ClearModeRsp** | R718H | 0x85   |             | **Status** (0x00 = success), **Reserved** (8 bytes, Fixed 0x00)                                           |
| **GetPulseCounter ClearModeRsp** | R718H | 0x86   |             | **PulseCounterClearMode** (1 byte, 0x00 = Clear When SEND, 0x01 = Clear When Roll-Over), **Reserved** (8 bytes, Fixed 0x00) |


