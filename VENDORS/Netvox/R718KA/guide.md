# R718KA Device Documentation

## Overview

The **R718KA** is a LoRaWAN-enabled device designed to measure and report current values. It provides reliable monitoring of battery voltage, current, and fine current measurements with an easy-to-interpret payload format.

---

## Payload Structure

The payload sent by the R718KA device is structured as follows:

### General Format

| **Bytes** | **1** | **1** | **1** | **Var (8 bytes)** |
|-----------|--------|--------|--------|------------------|
| **Field** | Version | DeviceType | ReportType | NetvoxPayLoadData |

- **Version**: 1 byte - Command version of the Netvox LoRaWAN Application. (Default: `0x01`)
- **DeviceType**: 1 byte - Indicates the device type. (For R718KA: `0x22`)
- **ReportType**: 1 byte - Presentation type of the payload. (Default: `0x01`)
- **NetvoxPayLoadData**: Fixed length of 8 bytes.

### Device-Specific Payload

For **R718KA**, the payload structure of `NetvoxPayLoadData` is:

| **Field**        | **Battery** | **Current** | **FineCurrent** | **Reserved**       |
|-------------------|-------------|-------------|------------------|--------------------|
| **Bytes**        | 1           | 1           | 1                | 5                  |
| **Description**  | Battery voltage in 0.1V units | Current in 1mA units | Fine current in 0.1mA units | Fixed value `0x00` |

---

## Detailed Explanation

- **Battery**: 1 byte representing the device's battery voltage. Multiply the value by `0.1` to get the voltage in volts (e.g., `0x1E` = 3.0V).
- **Current**: 1 byte representing the current measurement in milliamps (mA).
- **FineCurrent**: 1 byte representing a more precise current measurement in 0.1mA units.
- **Reserved**: 5 bytes reserved for future use; always fixed to `0x00`.

---

## LoRaWAN Configuration

- **FPort**: `0x06`
- **Device Type**: `0x22`
- **Report Type**: `0x01`

---

### Configuration Command IDs

The **R718KA** uses specific Command IDs to perform configuration tasks. Below is a breakdown of the relevant Command IDs for this device:

| **CmdID** | **DeviceType** | **Description**                                          |
|-----------|----------------|----------------------------------------------------------|
| `0x81`    | `0x22`         | Configuration Report Response. Provides the status of a configuration request. |
| `0x82`    | `0x22`         | Read Configuration Response. Returns the current device configuration settings. |

---

#### **CmdID: 0x81 (Config Report Response)**

This response confirms the success of a configuration command. It includes:
- **Status**: Success or failure of the configuration (1 byte, `0x00` for success).
- **Reserved**: 8 bytes, always fixed to `0x00`.

---

#### **CmdID: 0x82 (Read Configuration Response)**

This response provides the current configuration settings. It includes:
- **MinTime**: Current minimum reporting interval (2 bytes).
- **MaxTime**: Current maximum reporting interval (2 bytes).
- **BatteryChange**: Current battery change threshold (1 byte).
- **CurrentChange**: Current change threshold (1 byte).
- **Reserved**: 3 bytes, always fixed to `0x00`.

---
