# Report Data Command Example

This document describes the structure of the `ReportDataCmd` message and provides examples of its usage for Netvox devices.

---

## **Port Information**
- **FPort:** `0x06`

---

## **Command Structure**

| Bytes | Version (1 Byte)  | DeviceType (1 Byte) | ReportType (1 Byte) | NetvoxPayLoadData (Fixed: 8 Bytes) |
|-------|-------------------|---------------------|---------------------|------------------------------------|
| 1     | Command version   | Device type         | Data type           | Fixed-length payload data          |


## **Device-Specific Payload Example**

| Device  | DeviceType | ReportType | NetvoxPayLoadData                                                                                               |
|---------|------------|------------|-----------------------------------------------------------------------------------------------------------------|
| R718DA  | 0x1A       | 0x00       | SoftwareVersion (1 Byte, e.g., `0x0A` = V1.0), HardwareVersion (1 Byte), DateCode (4 Bytes), Reserved (2 Bytes) |
| R718DA  | 0x1A       | 0x01       | Battery (1 Byte, unit: 0.1V), Ball Status (1 Byte, `0: Off`, `1: On`), Reserved (6 Bytes, Fixed: `0x00`)        |

---

### **Payload Data Breakdown**

#### **For ReportType = 0x00 (Version Packet):**
| Field              | Size      | Description                                    |
|--------------------|-----------|------------------------------------------------|
| SoftwareVersion    | 1 Byte    | Example: `0x0A` = V1.0                        |
| HardwareVersion    | 1 Byte    | Example: `0x01`                               |
| DateCode           | 4 Bytes   | Example: `0x20170503` (Year: 2017, Month: 05, Day: 03) |
| Reserved           | 2 Bytes   | Fixed: `0x00`                                 |

#### **For ReportType = 0x01 (Data Packet):**
| Field              | Size      | Description                                    |
|--------------------|-----------|------------------------------------------------|
| Battery            | 1 Byte    | Example: `0x20` = 3.2V (unit: 0.1V)           |
| Status             | 1 Byte    | `0: Off`, `1: On`                             |
| Reserved           | 6 Bytes   | Fixed: `0x00`                                 |

---

# Configure Command Example

This document describes the structure and usage of the `ConfigureCmd` message for Netvox devices.

---

## **Port Information**
- **FPort:** `0x07`

---

## **Command Structure**

| Bytes | CmdID (1 Byte)  | DeviceType (1 Byte) | NetvoxPayLoadData (Variable: Max 9 Bytes) |
|-------|-----------------|---------------------|-------------------------------------------|
| 1     | Command ID      | Device Type         | Payload data (dependent on the command type) |

## **Device-Specific Command Details**

| Description                 | Device   | CmdID | Device Type | NetvoxPayLoadData                                                                                 |
|-----------------------------|----------|-------|-------------|---------------------------------------------------------------------------------------------------|
| **Config ReportRsp**        | R718DA2  | 0x81  | 0x2F        | Status (0x00 = success), Reserved (8 bytes, Fixed 0x00)                                           |
| **ReadConfig ReportRsp**    | R718DA2  | 0x82  | 0x2F        | MinTime (2 bytes), MaxTime (2 bytes), BatteryChange (1 byte, unit: 0.1V), Reserved (4 bytes, 0x00) |

---

### **Payload Data Breakdown**

#### **For Config ReportRsp (CmdID: 0x81):**
| Field            | Size      | Description                           |
|------------------|-----------|---------------------------------------|
| Status           | 1 Byte    | 0x00 = Success.                      |
| Reserved         | 8 Bytes   | Reserved (Fixed: 0x00).               |

#### **For ReadConfig ReportRsp (CmdID: 0x82):**
| Field            | Size      | Description                           |
|------------------|-----------|---------------------------------------|
| MinTime          | 2 Bytes   | Minimum time interval (in seconds).  |
| MaxTime          | 2 Bytes   | Maximum time interval (in seconds).  |
| BatteryChange    | 1 Byte    | Change in battery level (unit: 0.1V). |
| Reserved         | 4 Bytes   | Reserved (Fixed: 0x00).               |

---
