# Report Data Command Example

This document describes the structure of the `ReportDataCmd` message and provides examples of its usage. (FPort: 0x06)

## **Command Structure**

| Bytes | Version (1 Byte) | DeviceType (1 Byte) | ReportType (1 Byte) | Var (Fixed: 8 Bytes) |
|-------|------------------|---------------------|---------------------|----------------------|
| 1     | Version of NetvoxLoRaWAN Application Command | Device Type | Presentation of the Netvox Payload Data | Fixed 8 bytes |
---

## **Device-Specific Payload Example**

| Device | DeviceType | ReportType | NetvoxPayLoadData                            |
|--------|------------|------------|----------------------------------------------|
| R719A  | 0x59       | 0x01       | Battery (1 Byte, Unit: 0.1V), CarOnOff (1 Byte, 0: Off, 1: On), Reserved For Internal Use (6 Bytes) |

### **Payload Data Breakdown**
- **Battery:**
    - 1 Byte → Unit: 0.1V.
- **CarOnOff:**
    - 1 Byte → `0: Off`, `1: On`.
- **Reserved Data:**
    - Remaining 6 Bytes are reserved for Netvox internal use and can be ignored in custom decoders.


# Report Configuration Example

This document describes the structure and examples of the `Report Configuration` messages for Netvox devices. (FPort: 0x07)

---

## **Command Structure**

| Bytes | CmdID (1 Byte)  | DeviceType (1 Byte) | NetvoxPayLoadData (Variable: Max 9 Bytes) |
|-------|-----------------|---------------------|-------------------------------------------|
| 1     | Command ID      | Device Type         | Payload data (dependent on the device type and command) |

---

### **Field Descriptions**

- **CmdID (1 Byte):**
    - Represents the specific command type.

- **DeviceType (1 Byte):**
    - Specifies the type of device.
    - Device types are listed in the "Netvox LoRaWAN Application DeviceType.doc".

- **NetvoxPayLoadData:**
    - Variable-length data field (maximum: 9 bytes).
    - Contents depend on the `CmdID` and device type.

---

## **Device-Specific Command Details**

| Description       | Device | CmdID | Device Type | NetvoxPayLoadData                                                                                 |
|--------------------|--------|-------|-------------|---------------------------------------------------------------------------------------------------|
| **Config ReportRsp** | R719A  | 0x81  | 0x59        | Status (0x00 = success), Reserved (8 bytes, 0x00)                                                |
| **ReadConfig ReportRsp** | R719A  | 0x82  | 0x59        | MinTime (2 bytes), MaxTime (2 bytes), BatteryChange (1 byte, unit: 0.1V), Reserved (4 bytes, 0x00) |

---

# Geomagnetic Threshold Configuration

This document describes the commands and structure for configuring geomagnetic thresholds in Netvox devices.(FPort: 0x07)

> **Note:**  
> It is not recommended to modify the default settings of the device to prevent incorrect configurations, which could cause false detection of parking status.

---

## **Command Structure**

| Fport | CmdID (1 Byte) | DeviceType (1 Byte) | NetvoxPayLoadData (Variable Bytes) |
|-------|----------------|---------------------|-------------------------------------|
| 0x07  | Command ID     | Device Type         | Payload data (dependent on the command type) |

---

## **Device-Specific Command Details**

| Description                 | Device | CmdID | Device Type | NetvoxPayLoadData                               | Description                    |
|-----------------------------|--------|-------|-------------|------------------------------------------------|--------------------------------|
| **SetDetect ThresholdRsp**  | R719A  | 0x83  | 0x59        | Status (0x00 = success), Reserved (8 bytes, Fixed 0x00) | Acknowledges the threshold configuration. |
| **GetDetect ThresholdRsp**  | R719A  | 0x84  | 0x59        | DetectThreshold (2 bytes), Reserved (7 bytes, Fixed 0x00) | Returns the current detection threshold. |

---

### **Field Descriptions**

- **CmdID (1 Byte):**  
  Identifies the type of command:
    - `0x83`: Set detection threshold response.
    - `0x84`: Get detection threshold response.

- **DeviceType (1 Byte):**  
  Specifies the device type.  
  For example: `0x59` for the R719A device.

- **NetvoxPayLoadData:**  
  Contains the command-specific payload data, as described in the table above.

---
