## Models
```json
{
  "deviceType": "0x4A",
  "model_id": "r718n3",
  "deviceNames": [
      "R718N37",
      "R718N37E",
      "R718N315",
      "R718N315E",
      "R718N325",
      "R718N325E",
      "R718N363",
      "R718N363E",
      "R718N3100",
      "R718N3100E"
    ]  
}
```

## Payload Definition
- **Fport:0x06**
- description: *ReportDataCmd*

|       NAME        | VALUE | LENGTH | DESCRIPTION                                                                             |
|:-----------------:|:-----:|:------:|-----------------------------------------------------------------------------------------|
|      Version      |  0x01 |   1    | 0x01 - the Version of NetvoxLoRaWAN Application Command Version                         |
|    DeviceType     |  0x4A |   1    | Device Type of Device ("model_id": "r718n3")                                            |
|    ReportType     |  0xXX |   1    | {0x00...0x04}<br/>- The presentation of the NetvoxPayLoadData, according the devicetype |
| NetvoxPayLoadData |  data |   8    | Var (Fix=8 Bytes)                                                                       |


| Version | DeviceType | ReportType | NetvoxPayloadData                        |                                                                                                                                                                                                           |                                                                                   |                                |                                                                                                            |
|---------|------------|------------|------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|--------------------------------|------------------------------------------------------------------------------------------------------------|
| 0x01    | 0x4A       | 0x00       | SoftwareVersion<br/>(1 Byte)Eg.0x0A-V1.0 | HardwareVersion<br/>(1 Byte)                                                                                                                                                                              | DateCode<br/>(4 Byte)eg 0x20170503                                                | Reserved <br/>(2 Byte)         |                                                                                                            |
| 0x01    | 0x4A       | 0x01       | Battery (1 Byte, unit:0.1v)              | Current1<br/>(2 Byte, unit:mA)                                                                                                                                                                            | Current2 <br/>(2 Byte, unit:mA)                                                   | Current3 <br/>(2 Byte,unit:mA) | Multiplier1<br/>(1 Byte)the real current should convert with Current* Multiplie                            |
| 0x01    | 0x4A       | 0x02       | Battery (1 Byte, unit:0.1v)              | Multiplier2 <br/>(1 Byte) the real current should convert with Current* Multiplier                                                                                                                        | Multiplier3 <br/>(1 Byte)the real current should convert with Current* Multiplier | Reserved<br/>(5 Byte)          |                                                                                                            |
| 0x01    | 0x4A       | 0x03       | Battery (1 Byte, unit:0.1v)              | Current1 <br/>(2 Byte, unit:mA)                                                                                                                                                                           | Current2 <br/>(2 Byte, unit:mA)                                                   | Current3<br/>(2 Byte,unit:mA)  | Multiplier_1_3<br/>(1 Byte),Bit0_1:Multiplier1,Bit2_3:Multiplier2,Bit4_5:Multiplier3,Bit6_7:Reserved_2Bit) |
| 0x01    | 0x4A       | 0x04       | Battery (1 Byte, unit:0.1v)              | ThresholdAlarm_Current<br/>(1 Byte,Bit0:LowCurrent1Alarm,Bit1:HighCurrent1Alarm,<br/>Bit2:LowCurrent2Alarm,Bit3:HighCurrent2Alarm,<br/>Bit4:LowCurrent3Alarm,Bit5:HighCurrent3Alarm,Bit6_7:Reserved_2Bit) | Reserved <br/>(6 Byte)                                                            |                                |                                                                                                            |


- **Fport:0x07**

|        NAME        | VALUE | LENGTH | DESCRIPTION                                    |
|:------------------:|:-----:|:------:|------------------------------------------------|
|       CmdID        |  0xXX |   1    | {0x01, 0x81, 0x02, 0x82 0x03, 0x83 0x04, 0x84} |
|     DeviceType     |  0x4A |   1    | Device Type of Device ("model_id": "r718n3")   |
|  NetvoxPayLoadData |  data |   9    | Var bytes (Max=9bytes)                         |

- description: *ConfigureCmd*

| Description          | Device              | CmdID  | Device Type  | NetvoxPayLoadData                |                            |                                    |                                  |
|:---------------------|:--------------------|:------:|:------------:|:---------------------------------|:---------------------------|:-----------------------------------|:---------------------------------|
| Config ReportReq     | R718N3xxx(E) Series |  OxOl  |     Ox4A     | MinTime<br/>(2bytes Units)       | MaxTime<br/>(2bytes Units) | CurrentChange<br/>(2byte Unit lmA) | Reserved<br/>(3Bytes,Fixed OxOO) |
| Config ReportRsp     |                     |  Ox81  |              | Status<br/>(OxOO_success)        |                            | Reserved<br/>(8Bytes,Fixed OxOO)   |                                  |
| ReadConfig ReportReq |                     |  Ox02  |              | Reserved<br/>(9Bytes,Fixed OxOO) |                            |                                    |                                  |
| ReadConfig ReportRsp |                     |  Ox82  |              | MinTime<br/>(2bytes Units)       | MaxTime<br/>(2bytes Units) | CurrentChange<br/>(2byte Unit lmA) | Reserved<br/>(3Bytes,Fixed OxOO) |

- description: *SetRportType*

| Description      | Device              | CmdID | Device 'fype  | NetvoxPayLoadData                                          |                              |
|:-----------------|:--------------------|:------|:-------------:|:-----------------------------------------------------------|:-----------------------------|
| SetRport'fypeReq | R718N3xxx(E) Series | Ox03  |     Ox4A      | ReportTypeSet (!Byte) OxOO_reporttype 1&2 OxOl_reporttype3 | Reserved (8Bytes,Fixed OxOO) |
| SetRportTypeRsp  |                     | Ox83  |               | Status (OxOO_success)                                      | Reserved (8Bytes,Fixed OxOO) |
| GetRportTypeReq  |                     | Ox04  |               | Reserved (9Bytes,Fixed OxOO)                               |                              |
| GetRportTypeRsp  |                     | Ox84  |               | ReportTypeSet (!Byte) OxOO_reporttypel&2 Ox0l_reporttype3  | Reserved (2Bytes,Fixed OxOO) |

* Note : 
- a. Remain the last configuration when the device is reset back to factory setting. 
- b. Report Type = OxOO is two packets.(Default) 
- c. Report Type = OxOl is one packet. 
- d. Firmware after 2022.08.24 supports SetRportTypeReq

- **Fport:0x10**
- description: *SetSensorAlarmThresholdCmd*

| CmdDescriptor                   | CmdID (lByte) | Payload (10Bytes)                                                    |                                                         |                                           |                                          |
|:--------------------------------|:-------------:|:---------------------------------------------------------------------|:--------------------------------------------------------|:------------------------------------------|:-----------------------------------------|
| SetSensorAlarm<br/>ThresholdReq |     0x01      | Channel(1Byte)<br/>0x00_Channel1<br/>0x01_Channel2<br/>0x02_Channel3 | SensorType(lByte)<br/>0x00_Disable ALL<br/>0x27_Current | SensorHighThreshold<br/>(4Bytes,Unit:1mA) | SensorLowThreshold<br/>(4Bytes,Unit:1mA) |
| SetSensorAlarm<br/>ThresholdRsp |     0x81      | Status<br/>(0x00_success)                                            |                                                         | Reserved<br/>(9Bytes,Fixed  0x00)         |                                          |
| GetSensorAlarm<br/>ThresholdReq |     0x02      | Channel(1Byte)<br/>0x00_Channel1<br/>0x01_Channel2<br/>0x02_Channel3 | SensorType(1Byte)<br/>0x00_Disable ALL<br/>0x27_Current | Reserved<br/>(9Bytes,Fixed  0x00)         |                                          |
| GetSensorAlarm<br/>ThresholdRsp |     0x82      | Channel(1Byte)<br/>0x00_Channel1<br/>0x01_Channel2<br/>0x02_Channel3 | SensorType(1Byte)<br/>0x00_Disable ALL<br/>0x27_Current | SensorHighThreshold<br/>(4Bytes,Unit:1mA) | SensorLowThreshold<br/>(4Bytes,Unit:1mA) |


* Note:
- a. Set SensorHigh/LowThreshold as 0xFFFFFFFF to disable threshold.
- b. Remain the last configuration when the device is reset back to factory setting.
- c. Firmware after 2023.07.31 supports Set/GetSensorAlarmThresholdCmd
- d. Current1 uses channel 1 (0x00), Current2 uses channel 2 (0x01), and Current3 uses channel 3 (0x02)

- **Fport:0x20**
- description: *NetvoxLoRaWANRejoin*

| CmdDescriptor              | CmdID (1 byte) |           Payload (5 bytes)           |                                |
|:---------------------------|:--------------:|:-------------------------------------:|:-------------------------------|
| SetNetvoxLoRaWAN RejoinReq |      0x01      | RejoinCheckPeriod(4 Bytes, Unit: 1s)  | RejoinThreshold(l  Byte)       |
| SetNetvoxLoRaWANRejoinRsp  |      0x81      |     Status (1 Byte, 0x00_success)     | Reserved (4 Bytes, Fixed 0x00) |
| GetNetvoxLoRaWANRejoinReq  |      0x02      |    Reserved (5 Bytes, Fixed 0x00)     |                                |
| GetNetvoxLoRaWANRejoinRsp  |      0x82      | RejoinCheckPeriod (4 Bytes, Unit: 1s) | RejoinThreshold (1Byte)        |

* Note:
- a. Set RejoinCheckThreshold as 0xFFFFFFFF to stop the device from rejoining the network.
- b. Remain the last configuration when the device is reset back to factory setting.
- c. Default setting: RejoinCheckPeriod = 2 (hr) and RejoinThreshold = 3 (times)
- d. Firmware after 2023.12.07 supports SetNetvoxLoRaWANRejoinReq.

## Example

### uplinkDecoder:

#### Example of ReportDataCmd

```json
// All:  1), 2) 3), 4), 5)
{
 "hex": "014A000A02202007060000014A019F03E800C81B5801014A019F03E800C81B5801014A029F030A0000000000014A032405DD05D41B5836014A049F39000000000000", 
 "data": "AUoACgIgIAcGAAABSgGfA+gAyBtYAQFKAZ8D6ADIG1gBAUoCnwMKAAAAAAABSgMkBd0F1BtYNgFKBJ85AAAAAAAA"
}
```

```json
// 1) 
// description: Startup version report
// fPort: 6
//  01 4A 00 0A 02 20200706 0000 :: "HEX_bytes": 014A000A02202007060000 :: ""HEX_bytes_base64"": "AUoACgIgIAcGAAA="

{
  "SWver": 1.0,
  "SWverStr": "V1.0",
  "HWver": 2,
  "Datecode": "20200706"
}
```

```json
// 2) When ReportTypeSet=0x00 (reporttype1&2), R718N3xxx(E) will report two data packets, and the multiplier will be either 1 or 10;
// description: Status report - 1
// fPort: 6
//  01 4A 01 9F 03E8 00C8 1B58 01 :: "HEX_bytes": 014A019F03E800C81B5801 :: "frm_payload": "AUoBnwPoAMgbWAE="
//  "Multiplier1": 1

{
  "Volt": 3.1,       // byte (9F): Battery-3.1V, 9F (Hex) = 1001 1111(Bin) >> 1F(Hex) =31(Dec), 31*0.1v=3.1v
  "LowVolt": true,   // (low voltage), 9F (Hex) = 1001 1111(Bin), if bit 7= 1, it means low voltage.
  "Current1": 1000,  // Current1 = 1000 * "Multiplier1" =  1 ==  1000
  "Current2": 600,   // Current2 =  200 * "Multiplier1" =  3 ==   600 
  "Current3": 70000, // Current3 = 7000 * "Multiplier1" = 10 == 70000 
}

// 3) description: Status report - 1, 2
// fPort: 6
// 01 4A 01 9F 03E8 00C8 1B58 01 01 4A 02 9F 03 0A 00 00000000 :: "HEX_bytes": 014A019F03E800C81B5801014A029F030A0000000000 :: "frm_payload": "AUoBnwPoAMgbWAEBSgKfAwoAAAAAAA=="
//  "Multiplier1": 1
//  "Multiplier2": 3,
//  "Multiplier3": 10

{
  "Volt": 3.1,       // byte (9F): Battery-3.1V, 9F (Hex) = 1001 1111(Bin) >> 1F(Hex) =31(Dec), 31*0.1v=3.1v
  "LowVolt": true,   // (low voltage), 9F (Hex) = 1001 1111(Bin), if bit 7 = 1, it means low voltage. 
  "Current1": 1000,  // Current1 = 1000 * "Multiplier1" =  1 ==  1000
  "Current2": 600,   // Current2 =  200 * "Multiplier2" =  3 ==   600 
  "Current3": 70000, // Current3 = 7000 * "Multiplier3" = 10 == 70000 
}
```

```json
// 4) When ReportTypeSet=0x01 (reporttype3), R718N3xxx(E) will report one data packet.
// description: Status report - 3
// fPort: 6
//  01 4A 03 24 05DD 05D4 1B58 36 :: "HEX_bytes": 014A032405DD05D41B5836 :: "frm_payload": "AUoDJAXdBdQbWDY="
// "Multiplier1": 10,  //  0x36 = 00 11 01 10 (Bin): 10 == 10
// "Multiplier2": 5,   //  0x36 = 00 11 01 10 (Bin): 01 == 5
// "Multiplier3": 100  //  0x36 = 00 11 01 10 (Bin): 11 == 100

{
  "Volt": 3.6,        // byte (24): Battery-3.6V, 24 (Hex) = 0010 0100(Bin) >> 24(Hex) =36(Dec), 36*0.1v=3.6v, if bit 7 = 0, this means that the voltage is normal. 
  "Current1": 1000,   // Current1 = 1501 * "Multiplier1" =  10 ==  15010 mA
  "Current2": 600,    // Current2 = 1492 * "Multiplier2" =   5 ==   7460 mA
  "Current3": 700000, // Current3 = 7000 * "Multiplier3" = 100 == 700000 mA = 700A 
}
```

#### Example of Threshold Alarm

```json
// 5) 
// description: Status report - 4
// fPort: 6
//  01 4A 04 9F 39 000000000000 :: "HEX_bytes": 014A049F39000000000000 :: "frm_payload": "AUoEnzkAAAAAAAA="

{
  "Volt": 3.1,            // byte (9F): Battery-3.1V, 9F (Hex) = 1001 1111(Bin) >> 1F(Hex) =31(Dec), 31*0.1v=3.1v
  "LowVolt": true,        // if bit 7= 1, it means low voltage.
  "LowCurrent1Alarm": 1,  //  0x39 = 00 11 10 01 (Bin0): 0 == 1
  "HighCurrent1Alarm": 0, //  0x39 = 00 11 10 01 (Bin1): 0 == 0
  "LowCurrent2Alarm": 0,  //  0x39 = 00 11 10 01 (Bin2): 0 == 0
  "HighCurren2Alarm": 1,  //  0x39 = 00 11 10 01 (Bin3): 0 == 1
  "LowCurrent3Alarm": 1,  //  0x39 = 00 11 10 01 (Bin4): 0 == 1
  "HighCurrent3Alarm": 1  //  0x39 = 00 11 10 01 (Bin5): 0 == 1
}
```


### downlinkDecoder:

#### Example of ConfigureCmd

```json
// 1) 
// description: Configure report request/response

// payload
{
  "Cmd": "ConfigReportReq",
  "Device": "R718N3",
  "MinTime": 900,
  "MaxTime": 1800,
  "CurrentChange": 100
}

// fPort: 7
//  0x01, 0x4A, 0x03, 0x84, 0x07, 0x08, 0x00, 0x64, 0x00, 0x00, 0x00
// reult send
{
  "fPort": 7,
  "bytes": [ 0x01, 0x4A, 0x03, 0x84, 0x07, 0x08, 0x00, 0x64, 0x00, 0x00, 0x00]
}

// response success
// fPort: 7
//  81 4A 00 0000000000000000
{
  "Cmd": "ConfigReportRsp",
  "Device": "R718N3",
  "Status": "Success"  
}
// response failed
// fPort: 7
//  81 4A 01 0000000000000000
{
  "Cmd": "ConfigReportRsp",
  "Device": "R718N3",
  "Status": "Failed"  
}
```

```json
// 2) 
// description: Read Configure report request/response

// payload
{
  "Cmd": "ReadConfigReportReq",
  "Device": "R718N3"
}

// fPort: 7
//  0x02, 0x4A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
// result send
{
  "fPort": 7,
  "bytes": [0x02, 0x4A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
}

// The device returns:
// 82 4A 003C 003C 0064 000000 (Current device configuration parameters)
{
    "Cmd": "ReadConfigReportRsp",
    "Device": "R718N3",
    "MinTime": 60,
    "MaxTime": 60,
    "CurrentChange": 100
}
```

#### Example of SetReportType

```json
// 3) 
// description: Set Configure type request/response (reporttype1&2)

// payload
{
  "Cmd": "SetRportTypeReq",
  "Device": "R718N3",
  "ReportTypeSet": 0
}

// fPort: 7
//  03 4A 00 00000000000000x00  // 0x00 Uplink return two packet (reporttype1&2)
// result send
{
  "fPort": 7,
  "bytes": [0x03, 0x4A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
}
// response success
// fPort: 7
//  83 4A 00 0000000000000000
{
  "fPort": 7,
  "Cmd": "SetRportTypeRsp",
  "Device": "R718N3",
  "Status": "Success"
}

// response failed
// fPort: 7
//  83 4A 01 0000000000000000
{
  "fPort": 7,
  "Cmd": "SetRportTypeRsp",
  "Device": "R718N3",
  "Status": "Failed"
}

// Next, see example ReportDataCmd #2
```

```json
// 4) 
// description: Set Configure type request/response reporttype3

// payload
{
  "fPort": 7,
  "Cmd": "SetRportTypeReq",
  "Device": "R718N3",
  "ReportTypeSet": 1
}

// fPort: 7
//  03 4A 01 0000000000000000  // 0x01 Uplink return one packet (reporttype3)
// result send
{
  "fPort": 7,
  "bytes": [0x03, 0x4A, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
}
// response success
// fPort: 7
//  83 4A 00 0000000000000000
{
  "fPort": 7,
  "Cmd": "SetRportTypeRsp",
  "Device": "R718N3",
  "Status": "Success"
}


// response failed
// fPort: 7
//  83 4A 01 0000000000000000
{
  "fPort": 7,
  "Cmd": "SetRportTypeRsp",
  "Device": "R718N3",
  "Status": "Failed"
}

// Next, see example ReportDataCmd #3
```

```json
// 5) 
// description: Get Configure type request/response 
// payload
{
  "fPort": 7,
  "Cmd": "GetRportTypeReq",
  "Device": "R718N3",
  "ReportTypeSet": 0
}

// fPort: 7
//  04 4A 0000000000000000x00  
// result send
{
    "fPort": 7,
    "bytes": [0x04, 0x4A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
}

// response
// fPort: 7
//  84 4A 00 0000000000000000
{
  "fPort": 7,
  "Cmd": "GetRportTypeRsp",
  "Device": "R718N3",
  "ReportTypeSet": 0
}

// Next, see example ReportDataCmd #1_2


// response
// fPort: 7
//  84 4A 01 0000000000000000
{
  "fPort": 7,
  "Cmd": "GetRportTypeRsp",
  "Device": "R718N3",
  "ReportTypeSet": 1     // 0x01 Uplink return one packet.
}

// Next, see example ReportDataCmd #3


```

#### Example of SetSensorAlarmThresholdCmd

```json
// 5) 
// description: Set Sensor Alarm Threshold request/response 
// payload: Set Current1 HighThresholdt to 500mA, LowThreshold to 100mA
{
  "fPort": 10,
  "Cmd": "SetSensorAlarmThresholdReq",
  "ChannelId": 0,                // 0x00_Channel1, 0x01_Channel2, 0x02_Channel3
  "SensorType": 39,              // 0x00_Disable ALL, 0x27_Current
  "SensorHighThreshold": 500,    // (4Bytes,Unit:1mA)
  "SensorLowThreshold": 100      // (4Bytes,Unit:1mA)
}

// fPort: 10
// 010027000001F400000064  
// result send
{
  "fPort": 10,
  "bytes": [0x01, 0x00, 0x27, 0x00, 0x00, 0x01, 0xF4, 0x00, 0x00, 0x00, 0x64]
}

// response
// fPort: 10
//  81 00 000000000000000000
{
  "fPort": 10,
  "Cmd": "SetSensorAlarmThresholdRsp",
  "Status": "Success"
}

// response failed
// fPort: 10
//  81 01 000000000000000000
{
  "fPort": 10,
  "Cmd": "SetSensorAlarmThresholdRsp",
  "Status": "Failed"
}
```

```json
// 6) 
// description: Get Sensor Alarm Threshold request/response 
// payload: 
{
  "fPort": 10,
  "Cmd": "GetSensorAlarmThresholdReq",
  "ChannelId": 0,               // 0x00_Channel1, 0x01_Channel2, 0x02_Channel3
  "SensorType": "Current"       // 0x00_Disable ALL, 0x27_Current
}

// fPort: 10
// 0200270000000000000000  
// result send
{
  "fPort": 10,
  "bytes": [0x02, 0x00, 0x27, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
}

// response
// fPort: 10
// 82 00 27 000001F4 00000064
{
  "fPort": 10,
  "Cmd": "GetSensorAlarmThresholdRsp",
  "ChannelId": 0,
  "SensorType": "Current",
  "SensorHighThreshold": 500,
  "SensorLowThreshold": 100 
}

```json
// 7) 
// description: Disable all sensor thresholds for channel 1 
// payload: Configure the Sensor Type to 0
{
    "fPort": 10,
    "Cmd": "SetSensorAlarmThresholdReq",
    "ChannelId": 1,                // 0x00_Channel1, 0x01_Channel2, 0x02_Channel3
    "SensorType": "Disable ALL",   // 0x00_Disable ALL, 0x27_Current
    "SensorHighThreshold": 0,      // (4Bytes,Unit:1mA)
    "SensorLowThreshold": 0        // (4Bytes,Unit:1mA)
}

// fPort: 10
//  01 00 00 00000000 00000000  
// result send
{
  "fPort": 10,
  "bytes": [0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
}

// response
// fPort: 10
//  81 00 000000000000000000
{
    "fPort": 10,
    "Cmd": "SetSensorAlarmThresholdRsp",
    "Status": "Success"
}

```

#### Example of  NetvoxLoRaWANRejoin

```json
// 8) 
// description: Set Netvox LoRaWAN Rejoin request/response 
// payload: Set RejoinCheckPeriod = 3600s (0x00000E10), RejoinThreshold = 3 times

{
  "fPort": 20,
  "Cmd": "SetNetvoxLoRaWANRejoinReq",
  "RejoinCheckPeriod": 3600,   // (4 Bytes, Unit: 1s)
  "RejoinThreshold": 3         // (1 Byte)
}

// fPort: 20
//  01 00000E10 03  
// result send
{
  "fPort": 20,
  "bytes": [0x01, 0x00, 0x00, 0x0E, 0x10, 0x03]
}

// response success
// fPort: 20
//  81 00 00000000
{
  "fPort": 20,
  "Cmd": "SetNetvoxLoRaWANRejoinRsp",
  "Status": "Success"
}
// response failed
// fPort: 20
//  81 01 00000000
{
  "fPort": 20,
  "Cmd": "SetNetvoxLoRaWANRejoinRsp",
  "Status": "Failed"
}
```

```json
// 9) 
// description: Get Netvox LoRaWAN Rejoin request/response 
// payload: 
{
    "fPort": 20,
    "Cmd": "GetNetvoxLoRaWANRejoinReq"
}

// fPort: 20
// 02 0000000000  
// result send
{
"fPort": 20,
"bytes": [0x02, 0x00, 0x00, 0x00, 0x00, 0x00]
}

// response
// fPort: 20
// 82 00000E10 03
{
    "fPort": 20,
    "Cmd": "GetNetvoxLoRaWANRejoinRsp",
    "RejoinCheckPeriod ": 3600,
    "RejoinThreshold": 3
}

```