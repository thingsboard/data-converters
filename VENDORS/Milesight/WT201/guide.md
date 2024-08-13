

# UplinkDecoder:
## Payload Definition 

| CHANNEL                  |  ID  | TYPE | LENGTH | DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                           |
| :----------------------- | :--: | :--: | :----: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Protocol Version         | 0xFF | 0x01 |   1    | protocol_version(1B)                                                                                                                                                                                                                                                                                                                                                                                                  |
| Device Status            | 0xFF | 0x0B |   1    | device_status(1B)                                                                                                                                                                                                                                                                                                                                                                                                     |
| Serial Number            | 0xFF | 0x16 |   8    | sn(8B)                                                                                                                                                                                                                                                                                                                                                                                                                |
| Hardware Version         | 0xFF | 0x09 |   2    | hardware_version(2B)                                                                                                                                                                                                                                                                                                                                                                                                  |
| Firmware Version         | 0xFF | 0x0A |   2    | firmware_version(2B)                                                                                                                                                                                                                                                                                                                                                                                                  |
| LoRaWAN Class Type       | 0xFF | 0x0F |   1    | lorawan_class(1B)<br />lorawan_class, values: (0: classA, 1: classB, 2: classC, 3: classCtoB)                                                                                                                                                                                                                                                                                                                         |
| TSL Version              | 0xFF | 0xFF |   2    | tsl_version(2B)                                                                                                                                                                                                                                                                                                                                                                                                       |
| Ambient Temperature      | 0x03 | 0x67 |   2    | temperature(2B)<br />temperature, unit: ℃, read: int16/10                                                                                                                                                                                                                                                                                                                                                             |
| Target Temperature       | 0x04 | 0x67 |   2    | temperature_target(2B)<br />temperature_target, unit: ℃, read: int16/10                                                                                                                                                                                                                                                                                                                                               |
| Temperature Control      | 0x05 | 0xE7 |   1    | temperature_ctl_mode(0..1) + temperature_ctl_status(4..7)<br />temperature_ctl_mode, values: (0: heat, 1: em heat, 2: cool, 3: auto)<br />temperature_ctl_status: (0: standby, 1: stage-1 heat, 2: stage-2 heat, 3: stage-3 heat, 4: stage-4 heat, 5: em heat, 6: stage-1 cool, 7: stage-2 cool)                                                                                                                      |
| Fan Control              | 0x06 | 0xE8 |   1    | fan_mode(0..1) + fan_status(2..3)<br />fan_mode, values: (0: auto, 1: on, 2: circulate, 3: disable)<br />fan_status, values: (0: standby, 1: high speed, 2: low speed, 3: on)                                                                                                                                                                                                                                         |
| Plan Event               | 0x07 | 0xBC |   1    | plan_event(0..3)<br />plan_event, values: (0: not executed, 1: wake, 2: away, 3: home, 4: sleep)                                                                                                                                                                                                                                                                                                                      |
| System Status            | 0x08 | 0x8E |   1    | system_status(1B)<br />system_status, values: (0: off, 1: on)                                                                                                                                                                                                                                                                                                                                                         |
| Humidity                 | 0x09 | 0x68 |   1    | humidity(1B)<br />humidity, unit: %RH, read: int8/2                                                                                                                                                                                                                                                                                                                                                                   |
| Wires Relay Status       | 0x0A | 0x6E |   1    | wire_relay_status(1B) bit0: Y1, bit1: Y2/GL, bit2: W1, bit3: W2/AUX, bit4: E, bit5: G, bit6: O/B, bit7: 0                                                                                                                                                                                                                                                                                                             |
| Plan Settings            | 0xFF | 0xC8 |   6    | type(1B) + temperature_ctl_mode(1B) + fan_mode(1B) + temperature_target(1B), unit: ℃, read: int16/10  +  temperature_unit(1B: bit:7), values: (0: "℃", 1: "℉") + temperature_error(1B), read: int16/10                                                                                                                                                                                                              |
| Plan                     | 0xFF | 0xC9 |   6    | type(1B) + index(1B) + plan_enable(1B) + week_recycle(1B) + time(1B)<br />type, values: (0: wake, 1: away, 2: home, 3: sleep)<br />index, range: [0, 15]<br />week_recycle, read: bits, (bit1: mon, bit2: tues, bit3: wed, bit4: thur, bit5: fri, bit6: sat, bit7: sun)<br />time, unit: mins                                                                                                                         |
| Wires                    | 0xFF | 0xCA |   3    | value1(1B) + value2(1B) + value3(1B)<br />value1, bit0-bit1: y1, bit2-bit3: gh, bit4-bit5: o/b, bit6-bit7: w1<br />value2, bit0-bit1: e, bit2-bit3: di, bit4-bit5: pek, bit6-bit7: (1: w2, 2: aux)<br />value3, bit0-bit1: (1: y2, 2: gl), bit2-bit3: (0: cool, 1: heat)                                                                                                                                              |
| Temperature Mode Support | 0xFF | 0xCB |   3    | mode_enable(1B) + heat_level_enable(1B) + cool_level_enable(1B)<br />mode_enable, read: bits, (bit0: heat, bit1: em heat, bit2: cool, bit3: auto)<br />heat_level_enable, read: bits, (bit0: stage-1 heat, bit1: stage-2 heat, bit2: stage-3 heat, bit3: stage-4 heat, bit4: aux heat)<br />cool_level_enable: read: bits, (bit0: stage-1 cool, bit1: stage-2 cool)                                                   |
| Control Permissions      | 0xFF | 0xF6 |   1    | control_permissions(1B)<br />control_permissions, values: (0: thermostat, 1: remote control)                                                                                                                                                                                                                                                                                                                          |
| Temperature Alarm        | 0x83 | 0x67 |   3    | temperature(2B) + temperature_alarm(1B)<br />temperature, unit: ℃, read: int16/10<br />temperature_alarm, values: (1: emergency heating timeout, 2: auxiliary heating timeout, 3: persistent low temperature, 4: persistent low temperature release, 5: persistent high temperature, 6: persistent high temperature release, 7: freeze protection, 8: freeze protection release, 9: threshold, 10: threshold release) |
| Temperature Exception    | 0xB3 | 0x67 |   1    | temperature_exception(1B)<br />temperature_exception, values: (1: read failed, 2: out of range)                                                                                                                                                                                                                                                                                                                       |
| Humidity Exception       | 0xB9 | 0x68 |   1    | humidity_exception(1B)<br />humidity_exception, values: (1: read failed, 2: out of range)                                                                                                                                                                                                                                                                                                                             |
| Historical Data          | 0x20 | 0xCE |   8    | timestamp(4B) + value_1(2B) + value_2(2B)<br />timestamp, unit: s, read: uint32<br />value_1, fan_mode(0..1) + fan_status(2..3) + system_status(4) + temperature(5..15)<br />value_2, temperature_ctl_mode(0..1) + temperature_ctl_status(2..4) + temperature_target(5..15)<br />temperature, unit: ℃, read: unit16 / 10 - 100                                                                                        |

### WIRES(3B)

#### WIRES-BYTE1

| BITS | 7..6 | 5..4 | 3..2 | 1..0 |
| :--: | :--: | :--: | :--: | :--: |
| LINE |  W1  | O/B  |  GH  |  Y1  |

#### WIRES-BYTE2

| BITS |   7..6    | 5..4 | 3..2 | 1..0 |
| :--: | :-------: | :--: | :--: | :--: |
| LINE | W2 or AUX | PEK  |  DI  |  E   |

#### WIRES-BYTE3

| BITS | 7..4 |       3..2        | 1..0  |
| :--: | :--: | :---------------: | :---: |
| LINE | RFU  | O/B: COOL or HEAT | Y2/GL |

### WIRE RELAY(2B)

```
+-------+--------+--------+--------+--------+--------+--------+--------+
|   7   |    6   |    5   |    4   |    3   |    2   |    1   |    0   |
+-------+--------+--------+--------+--------+--------+--------+--------+
|  RFU  |   O/B  |    G   |    E   | W2/AUX |   W1   |  Y1/GL |   Y1   |

```

## Example

```
// All:
{
"hex": "036702010467A60005E70006E80007BC008367FB000920CE5C470A65D09EC091FFCB0D1101FFCA158004FFC900000000B302FFC9020101280000FFC80303014E36FFC80303014E36FF0BFFFF0101FF166791D19604050005FF090100FF0A0103FF0F02FFFF010003671101088E0109684A0A6E72036711010467FA0005E77206E80607BC00088E01096844FFF600",
"data": "A2cCAQRnpgAF5wAG6AAHvACDZ/sACSDOXEcKZdCewJH/yw0RAf/KFYAE/8kAAAAAswL/yQIBASgAAP/IAwMBTjb/yAMDAU42/wv//wEB/xZnkdGWBAUABf8JAQD/CgED/w8C//8BAANnEQEIjgEJaEoKbnIDZxEBBGf6AAXncgboBge8AAiOAQloRP/2AA=="
}
// 
```

```json
//1) 
// description: Ambient Temperature; Target Temperature; Temperature Control; Fan Control; Plan Event
// 03670201 0467A600 05E700 06E800 07BC00 
// "HEX_bytes": 036702010467A60005E70006E80007BC00 :: ""HEX_bytes_base64"": "A2cCAQRnpgAF5wAG6AAHvAA="
{
    "fan_mode": "auto",
    "fan_status": "standby",
    "plan_event": "not executed",
    "temperature": 25.8,
    "temperature_ctl_mode": "heat",
    "temperature_ctl_status": "standby",
    "temperature_target": 16.6
}

//2) 
// description: Temperature Alarm
// 8367FB0009 
// "HEX_bytes": 8367FB0009 :: "HEX_bytes_base64"": "g2f7AAk="
{
    "temperature": 25.1,
    "temperature_alarm": "threshold alarm"
}

//3) 
// description: Historical Data
// 20CE5C470A65D09EC091 
// "HEX_bytes": 20CE5C470A65D09EC091 :: "HEX_bytes_base64"": "IM5cRwpl0J7AkQ=="
{
    "history": [
        {
            "fan_mode": "auto",
            "fan_status": "standby",
            "system_status": "on",
            "temperature": 27,
            "temperature_ctl_mode": "heat",
            "temperature_ctl_status": "standby",
            "temperature_target": 16.6,
            "timestamp": 1695172444
        }
    ]
}

//4) 
// description: Temperature Mode Support; Wires
// FFCB0D1101 FFCA158004 
// "HEX_bytes": FFCB0D1101FFCA158004 :: "HEX_bytes_base64"": "/8sNEQH/yhWABA=="
{
    "ob_mode": "heat",
    "temperature_ctl_mode_enable": ["heat", "cool", "auto"],
    "temperature_ctl_status_enable": ["stage-1 heat", "aux heat", "stage-1 cool"],
    "wires": ["y1", "gh", "ob", "aux"]
}

//5) 
// description: plan Schedule
// FFFC900000000B302 FFC9020101280000 
// "HEX_bytes": FFC900000000B302FFC9020101280000 :: "HEX_bytes_base64"": "/8kAAAAAswL/yQIBASgAAA=="
{
    "plan_schedule": [
        {
            "index": 1,
            "plan_enable": "disable",
            "time": "11:31",
            "type": "wake",
            "week_recycle": []
        },
        {
            "index": 2,
            "plan_enable": "enable",
            "time": "0:00",
            "type": "home",
            "week_recycle": [
                "Wed.",
                "Fri."
            ]
        }
    ]
}

//6) 
// description: Plan Settings
// FFC80303014E36
// "HEX_bytes": FFC80303014E36 :: "HEX_bytes_base64"": "/8gDAwFONg=="
{
    "plan_settings": [
        {
            "fan_mode": "on",
            "temperature_ctl_mode": "auto",
            "temperature_error": 5.4,
            "temperature_target": 78,
            "type": "sleep"
        }
    ]
}

```//7) 
// description: Device Status, Protocol Version, Serial Number, Hardware Version, Firmware Version, LoRaWAN Class Type, TSL Version
// FF0BFF FF0101 FF166791D19604050005 FF090100 FF0A0103 FF0F02 FFFF0100
// "HEX_bytes": FF0BFFFF0101FF166791D19604050005FF090100FF0A0103FF0F02FFFF0100 :: "HEX_bytes_base64"": "/wv//wEB/xZnkdGWBAUABf8JAQD/CgED/w8C//8BAA=="
{
    "device_status": "on",      // FF
    "ipso_version": "v1.0",     // 01
    "sn": "6791D19604050005",   // 6791D19604050005
    "hardware_version": "v1.0", // 0100
    "firmware_version": "v1.3", // 0103
    "lorawan_class": "ClassC",  // 02
    "tsl_version": "v1.0"       // 0100
}
```

```
//8) 
// description: Ambient Temperature, System Status, Humidity, Wires Relay Status
// 03671101 088E01 09684A 0A6E72
// "HEX_bytes": 03671101088E0109684A0A6E72 :: "HEX_bytes_base64"": "A2cRAQiOAQloSgpucg=="
{
      "temperature": 27.3,
      "system_status": "on",
      "humidity": 37.0,
      "wires_relay": {      // 0x72 => 114 => 0111 0010
        "y1": 0,            // bit0
        "y2_gl": 1,         // bit1
        "w1": 0,            // bit2
        "w2_aux": 0,        // bit3
        "e": 1,             // bit4
        "g": 1,             // bit5
        "ob": 1             // bit6
      }
}
```

```
//9) 
// description: Ambient Temperature, Target Temperature, Temperature Control, Fan Control, Plan Event, System Status, Humidity
// 03671101 0467FA00 05E772 06E806 07BC00 088E01 096844
// "HEX_bytes": 036711010467FA0005E77206E80607BC00088E01096844 :: "HEX_bytes_base64": "A2cRAQRn+gAF53IG6AYHvAAIjgEJaEQ="
{
    "temperature": 27.3,
    "temperature_target": 25.0,
    "temperature_control_mode": "cool",
    "temperature_control_status": "stage-2 cool",
    "fan_mode": "circulate",
    "fan_status": "high speed",
    "plan_event": "not executed",
    "system_status": "on",
    "humidity": 34.0,
}
```

```
//10) 
// description: Control Permissions
// FFF600
// "HEX_bytes": FFF600 :: "HEX_bytes_base64"": "//YA"
{
    "control_permissions": "thermostat"
}
```

# DownlinkDecoder (Downlink Command):
## Payload Definition 
WT201 supports downlink commands to configure the device. The application port is 85 by
default and can be configured via ToolBox.
**Note:** If confirmed mode on the device or network server is enabled, the device will reply the downlink command with reply format.

1) Command Format 1:

| Channel | Type   | Command |
|:-------:|:-------|:--------|
|   ff    | 1 Byte | N Bytes |


   Reply Format:

| Channel | Type            | Command         |
|:-------:|:----------------|:----------------|
|   ff    | Same as command | Same as command |


2) Command Format 2:

| Channel | Type   | Command |
|:-------:|:-------|:--------|
|   f9    | 1 Byte | N Bytes |


Reply Format:

| Channel | Type            | Command         | Return Code                                                  |
|:-------:|:----------------|-----------------|:-------------------------------------------------------------|
|   f8    | Same as command | Same as command | 00: success<br /> 01: not support<br /><br/>02: out of range |

### Basic Settings

|             Item             | Channel | Type | Byte | Description                                                                                                                                                                                                                                              |
|:----------------------------:|:--------|------|------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|            Reboot            | 0xFF    | 0x10 | 1    | ff                                                                                                                                                                                                                                                       |
|     Query Current Status     | 0xFF    | 0x28 | 1    | 01, the device will return a periodic packet                                                                                                                                                                                                             |
|      Reporting Interval      | 0xFF    | 0x8E | 3    | Byte 1: 00<br />Byte 2-3: Interval time, unit: min                                                                                                                                                                                                       |
|        System On/Off         | 0xFF    | 0xC5 | 1    | System On/Off                                                                                                                                                                                                                                            |
|      Control Permission      | 0xFF    | 0xF6 | 1    | 00=Thermostat, 01=Remote Control                                                                                                                                                                                                                         |
|          Child Lock          | 0xFF    | 0x25 | 2    | Byte 1: ff<br />Byte 2: for every bit 0=disable, 1=enable.<br />Bit0: System on/off; Bit1: Temperature +; Bit2: Temperature -; Bit3: Fan mode; Bit4: Temperature control mode; Bit5: Reset and reboot; Bit6-7: 00                                        |
|        UTC Time Zone         | 0xFF    | 0xBD | 2    | INT16/60                                                                                                                                                                                                                                                 |
|     Daylight Saving Time     | 0xFF    | 0xBA | 10   | Byte 1: 00-disable, 01-enable<br />Byte 2: DST bias, unit: min<br />Byte 3-6: Start time, Month (1B)+Week(1B) + Hours of a Day (2B)<br />Week: Bit7-4 1: 1st, 2: 2nd,...;  Bit3-0: 1: Monday, 2:Tuesday,...7: Sunday;<br />Byte 7-10: End time           |
|         Data Storage         | 0xFF    | 0x68 | 1    | 00: disable, 01: enable                                                                                                                                                                                                                                  |
|     Data Retransmission      | 0xFF    | 0x69 | 1    | 00: disable, 01: enable                                                                                                                                                                                                                                  |
| Data Retransmission Interval | 0xFF    | 0x6A | 1    | Byte 1: 00<br />Byte 2-3: Interval time, unit: s<br />range: 30~1200s (600s by default)                                                                                                                                                                  |
|       Multicast group        | 0xFF    | 0x82 | 1    | Bit 7-4: multicast group 4 to 1 change status, 0 = not allow control, 1 = allow control.<br /> Bit 3-0: multicast group 4 to 1 control status, 0 for disable, 1 for enable..<br />Note: after disabling or enabling, the device will re-join the network |

## Example

```
// All:
// payload
{
  "reboot": 1,
  "report_interval": 2,
    "child_lock_config": {
    "power_button": 1,  
    "up_button": 0,     
    "down_button": 1,   
    "fan_button": 0,    
    "mode_button": 0,   
    "reset_button": 1   
  },
  "timezone": -4,
    "dst_config": {
    "enable": 1,
    "bias": 60,
    "start_time": {
      "month": 10,
      "week": 1,
      "weekday": 7,
      "time": "2:45"
    },
    "end_time": {
      "month": 4,
      "week": 1,
      "weekday": 7,
      "time": "23:38"
    }
  },
  "multicast_group_config": {
    "group1_enable": 0,
    "group2_enable": 1,
    "group3_enable": 0,
    "group4_enable": 1
  }
}

// reult send
{
    "contentType": "JSON",
    "fPort": 85,
    "data": "{\"bytes\":\"/xD//44AAgD/Jf8l/70Q//+6ATwKF6UABBeKBf+C+g==\"}",
    "dataHex": "FF10FFFF8E000200FF25FF25FFBD10FFFFBA013C0A17A50004178A05FF82FA",
    "metadata": {
        "topic": "smartThermostat/sensorWT201/6791D19604050005/upload"
    }
}
```

```

```json
// 1) 
// description: Reboot (Reboot the device).

// payload
{
  "reboot": 1
}

// fPort: 85
// bytes: FF10FF :: "bytes_base64"": "/xD/"
// reult send
{
{
    "contentType": "JSON",
    "fPort": 85,
    "data": "{\"bytes\":\"/xD//44AAgD/Jf8l/70Q//+6ATwKF6UABBeKBQ==\"}",
    "dataHex": "FF10FFFF8E000200FF25FF25FFBD10FFFFBA013C0A17A50004178A05",
    "metadata": {
        "topic": "smartThermostat/sensorWT201/6791D19604050005/upload"
    }
}
```

```json
// 2) 
// description: Reporting Interval (Set reporting interval as 2 minutes).

// payload
{
  "report_interval": 2
}

// fPort: 85
// bytes: FF8E000200 :: "bytes_base64"": "/44AAgA="
// reult send
{
  "contentType": "JSON",
  "fPort": 85,
  "data": "{\"bytes\":\"/44AAgA=\"}",
  "dataHex": "FF8E000200",
  "metadata": {
    "topic": "smartThermostat/sensorWT201/6791D19604050005/upload"
  }
}
```

```json
// 3) 
// description: Child Lock.

// payload
{
  "child_lock_config": {
    "power_button": 1,  // System on/off
    "up_button": 0,     // Temperature +
    "down_button": 1,   // Temperature -
    "fan_button": 0,    // Fan mode
    "mode_button": 0,   // Temperature control mode
    "reset_button": 1   // Reset and reboot
  }
}

// fPort: 85
// bytes: FF25FF25 :: "bytes_base64"": "/yX/JQ=="
// reult send
{
  "contentType": "JSON",
  "fPort": 85,
  "data": "{\"bytes\":\"/yX/JQ==\"}",
  "dataHex": "FF25FF25",
  "metadata": {
    "topic": "smartThermostat/sensorWT201/6791D19604050005/upload"
  }
}
```

```json
// 4) 
// description: UTC Time Zone (Set time zone).

// payload
{
  "timezone": -4
}

// fPort: 85
// bytes: FFBD10FF :: "bytes_base64"": "/70Q/w=="
// reult send
{
  "contentType": "JSON",
  "fPort": 85,
  "data": "{\"bytes\":\"/70Q/w==\"}",
  "dataHex": "FFBD10FF",
  "metadata": {
    "topic": "smartThermostat/sensorWT201/6791D19604050005/upload"
  }
}
```

```json
// 5) 
// description: Daylight Saving Time ( Set DST time: start time is October 1st Sunday 2:45, end time is April 1st Sunday 23:38, and bias is 1h (60 minutes)).

// payload
{
  "dst_config": {
    "enable": 1,
    "bias": 60,
    "start_time": {
      "month": 10,
      "week": 1,
      "weekday": 7,
      "time": "2:45"
    },
    "end_time": {
      "month": 4,
      "week": 1,
      "weekday": 7,
      "time": "23:38"
    }
  }
}

// fPort: 85
// bytes: FFBA 01 3C 0A17A500 04178A05 :: "bytes_base64"": "/7oBPAoXpQAEF4oF"
// reult send
{
  "contentType": "JSON",
  "fPort": 85,
  "data": "{\"bytes\":\"/7oBPAoXpQAEF4oF\"}",
  "dataHex": "FFBA013C0A17A50004178A05",
  "metadata": {
    "topic": "smartThermostat/sensorWT201/6791D19604050005/upload"
  }
}
```

```json
// 6) 
// description: Multicast group (Set multicast group: 1 as disable; 2 as enable; 3 as disable; 4 as enable;).

// payload
{
  "multicast_group_config": {
    "group1_enable": 0,
    "group2_enable": 1,
    "group3_enable": 0,
    "group4_enable": 1
  }
}
// fPort: 85
// bytes: FF82FA :: "bytes_base64"": "/4L6"
// reult send
{
  "contentType": "JSON",
  "fPort": 85,
  "data": "{\"bytes\":\"/4L6\"}",
  "dataHex": "FF82FA",
  "metadata": {
    "topic": "smartThermostat/sensorWT201/6791D19604050005/upload"
  }
}
```

### Installation Setting
** Below settings only take effect when control permission is Thermostat.

|       Item        | Channel | Type | Byte | Description                                                                                                                                                                                                                                                                                                                                                                                                       |
|:-----------------:|:-------:|:----:|:----:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  Wiring Settings  |  0xFF   | 0xCA |  3   | Byte 1:  Bit1-0: Y1;   Bit3-2: G/GH;   Bit5-4: OB;   Bit7-6: W1;  (00=disable, 01=enable)                                                                                                                                                                                                                                                                                                                         |
|                   |         |      |      | Byte 2:  Bit1-0: E;    Bit3-2: CL&CN;  Bit5-4: PEK; (00=disable, 01=enable)<br/>_________Bit7-6: W2/AUX  (00=disable, 01=W2, 10=AUX)                                                                                                                                                                                                                                                                              |
|                   |         |      |      | Byte 3:  Bit1-0: Y2/GL (00=disable, 01=Y2, 10=GL); Bit3-2: OB (00=O/B on cool, 01=O/B on heat 11=Keep Original Setting);) Bit7-4: 0000                                                                                                                                                                                                                                                                            | 
|  Reversing Valve  |  0xFF   | 0xB5 |  1   | 00=O/B on cool, 01=O/B on heat                                                                                                                                                                                                                                                                                                                                                                                    |
| Freeze Protection |  0xFF   | 0xB0 |  3   | Byte 1: 00-disable, 01-enable; Byte 2-3: Protection temperature, INT16/10, unit: °C                                                                                                                                                                                                                                                                                                                               |
| Room Card Setting |  0xFF   | 0xC1 |  4   | Byte 1: 00-disable, 01-enable; Byte 2: 00=System on/off, 01=Insert an event<br/>Byte 3: for every bit: 0=disable, 1=enable <br/>Corresponding event of every bit:<br/>Bit0: Insert card- Wake; Bit1: Insert card- Wake; Bit2: Insert card- Home (Default); Bit3: Insert card- Sleep; Bit4: Remove card- Wake; Bit5: Remove card- Away(Default); Bit6: Remove card- Home; Bit7: Remove card- Sleep;<br/>Byte 4: 00 |
