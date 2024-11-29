# Report Data Command Example fPort = 0x06

---

## **Command Structure**

| Bytes | Version (1 Byte)  | DeviceType (1 Byte) | ReportType (1 Byte) | NetvoxPayLoadData (Fixed: 8 Bytes) |
|-------|-------------------|---------------------|---------------------|------------------------------------|
| 1     | Command version   | Device type         | Data type           | Fixed-length payload data          |

---

## **Tips**

### **1. Battery Voltage:**
- The battery voltage is represented using **bit 6** and **bit 7**:
    - **Bit 7 = 0:** Normal voltage.
    - **Bit 7 = 1:** Low voltage.
- Example:
    - `Battery = 0xA0` → `binary = 1010 0000`
    - If `bit 7 = 1`, it means low voltage.
    - Actual voltage = `0010 0000` → `0x20 = 32` → `32 * 0.1V = 3.2V`.

### **2. Version Packet:**
- When `ReportType = 0x00`, the packet contains the version information:
    - Example:
      ```plaintext
      0112000A0B202005200000
      ```
    - Firmware version: `2020.05.20`.

### **3. Data Packet:**
- When `ReportType = 0x01`, the packet contains data.

---

## **Device-Specific Payload Example**

| Device  | DeviceType | ReportType | NetvoxPayLoadData                                                                      |
|---------|------------|------------|---------------------------------------------------------------------------------------|
| R718WB  | 0x12       | 0x00       | SoftwareVersion (1 Byte, e.g., `0x0A` = V1.0), HardwareVersion (1 Byte), DateCode (4 Bytes), Reserved (2 Bytes) |
| R718WB  | 0x12       | 0x01       | Battery (1 Byte, unit: 0.1V), WaterLeak (1 Byte, `0: No Leak`, `1: Leak`), Reserved (6 Bytes, Fixed: `0x00`) |

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
| WaterLeak          | 1 Byte    | `0: No Leak`, `1: Leak`                       |
| Reserved           | 6 Bytes   | Fixed: `0x00`                                 |

# Configure Command Example fPort = 0x07

This document describes the structure of the `ConfigureCmd` message and provides examples for configuring Netvox devices.

---

## **Command Structure**

| Bytes | CmdID (1 Byte)  | DeviceType (1 Byte) | NetvoxPayLoadData (Variable: Max 9 Bytes) |
|-------|-----------------|---------------------|-------------------------------------------|
| 1     | Command ID      | Device Type         | Payload data (dependent on the command type) |

---

### **Field Descriptions**

- **CmdID (1 Byte):**  
  Represents the specific command type.

- **DeviceType (1 Byte):**  
  Specifies the type of device.  
  Device types are listed in the "Netvox LoRaWAN Application DeviceType.doc".

- **NetvoxPayLoadData (Max: 9 Bytes):**  
  Contains command-specific payload data, as described below.

---

## **Device-Specific Command Details**

| Description       | Device  | CmdID | Device Type | NetvoxPayLoadData                                                                                 |
|--------------------|---------|-------|-------------|---------------------------------------------------------------------------------------------------|
| **Config ReportRsp** | R718WB  | 0x81  | 0x12        | Status (0x00 = success), Reserved (8 bytes, Fixed 0x00)                                           |
| **ReadConfig ReportRsp** | R718WB  | 0x82  | 0x12        | MinTime (2 bytes), MaxTime (2 bytes), BatteryChange (1 byte, unit: 0.1V), Reserved (4 bytes, 0x00) |

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

## **Examples of Use**

### **1. Configure Device Parameters**
- **Configuration Details:**
    - `MinTime` = 1 minute (0x003C).
    - `MaxTime` = 1 minute (0x003C).
    - `BatteryChange` = 0.1V (0x01).