## ReportDataCmd

Reports from the **RA0715A** are sent to **FPort: 0x06**. The `ReportDataCmd` contains structured data based on the `ReportType`.

---

## Payload Structure

The payload sent by the **RA0715A** is structured as follows:

| **Bytes** | **1**        | **1**        | **1**        | **Var (Fixed = 8 Bytes)** |
|-----------|--------------|--------------|--------------|---------------------------|
| **Field** | Version      | DeviceType   | ReportType   | NetvoxPayLoadData         |

### Field Descriptions
- **Version**: 1 byte - Version of the Netvox LoRaWAN Application Command (e.g., `0x01`).
- **DeviceType**: 1 byte - Identifier for the device type (`0x05` for RA0715A).
- **ReportType**: 1 byte - Indicates the type of report (e.g., `0x00`, `0x07`, `0x0C`).
- **NetvoxPayLoadData**: Contains the reported data, fixed at 8 bytes.

---

## NetvoxPayLoadData Structure for RA0715A

The `NetvoxPayLoadData` field contains the specific data reported by the device **RA0715A**, based on the `ReportType`. Reports are sent to **FPort: 0x06**.

| **Device**  | **Device Type** | **Report Type** | **Field**             | **Description**                            | **Unit**            |
|-------------|-----------------|-----------------|-----------------------|--------------------------------------------|---------------------|
| **RA0715A** | `0x05`          | `0x00`          | SoftwareVersion       | Software version of the device             | 1 byte, e.g., `0x0A` → V1.0 |
|             |                 |                 | HardwareVersion       | Hardware version of the device             | 1 byte              |
|             |                 |                 | DateCode              | Manufacturing date code                    | 4 bytes, e.g., `0x20170503` |
|             |                 |                 | Reserved              | Reserved for future use                    | 2 bytes, fixed `0x00` |
| **RA0715A** | `0x05`          | `0x07`          | Battery               | Battery level                              | 1 byte, unit: `0.1V` |
|             |                 |                 | CO2                   | CO2 concentration                          | 2 bytes, unit: `0.1ppm` |
|             |                 |                 | NH3                   | Ammonia concentration                      | 2 bytes, unit: `0.1ppm` |
|             |                 |                 | Noise                 | Noise level                                | 2 bytes, unit: `0.1dB` |
|             |                 |                 | Reserved              | Reserved for future use                    | 1 byte, fixed `0x00` |
| **RA0715A** | `0x05`          | `0x0C`          | Battery               | Battery level                              | 1 byte, unit: `0.1V` |
|             |                 |                 | Temperature           | Temperature measurement (signed)           | 2 bytes, unit: `0.01°C` |
|             |                 |                 | Humidity              | Humidity level                             | 2 bytes, unit: `0.01%` |
|             |                 |                 | WindSpeed             | Wind speed measurement                     | 2 bytes, unit: `0.01m/s` |
|             |                 |                 | Reserved              | Reserved for future use                    | 1 byte, fixed `0x00` |

---

## 5.2 Example of ConfigureCmd

The **ConfigureCmd** allows configuration of the **RA0715A** device's reporting behavior and settings. This command is sent to **FPort: 0x07**.

---

### Payload Structure

| **Bytes** | **1**         | **1**         | **Var (Max = 9 Bytes)** |
|-----------|---------------|---------------|--------------------------|
| **Field** | CmdID         | DeviceType    | NetvoxPayLoadData        |

- **CmdID**: 1 byte - Command Identifier (e.g., `0x01` for Config Report Request, `0x81` for Config Report Response).
- **DeviceType**: 1 byte - Identifier for the device type (`0x05` for RA0715A).
- **NetvoxPayLoadData**: Contains the command-specific data.

---

### Command Descriptions

#### Config Report Response

The `Config Report Response` (`CmdID: 0x81`) provides the status of the configuration request. The payload is structured as follows:

| **Field**       | **Bytes** | **Description**                    | **Value**         |
|------------------|-----------|------------------------------------|-------------------|
| **Status**       | 1         | Status of the configuration        | `0x00` (Success)  |
| **Reserved**     | 8         | Reserved for future use            | Fixed `0x00`      |

#### Read Config Report Response

The `Read Config Report Response` (`CmdID: 0x82`) provides the current reporting configuration. The payload is structured as follows:

| **Field**       | **Bytes** | **Description**                    | **Unit**          |
|------------------|-----------|------------------------------------|-------------------|
| **MinTime**      | 2         | Minimum reporting interval         | Seconds           |
| **MaxTime**      | 2         | Maximum reporting interval         | Seconds           |
| **Reserved**     | 5         | Reserved for future use            | Fixed `0x00`      |

---

