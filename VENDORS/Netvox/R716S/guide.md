# Device Guide for R716S (Netvox)

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