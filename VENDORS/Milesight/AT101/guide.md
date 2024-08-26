
## Payload Definition

|       CHANNEL        |  ID  | TYPE | LENGTH | DESCRIPTION                                                             |
| :------------------: | :--: | :--: | :----: | ----------------------------------------------------------------------- |
|       Battery        | 0x01 | 0x75 |   1    | battery(1B)<br/>battery, unit: %                                        |
|     Temperature      | 0x03 | 0x67 |   2    | temperature(2B)<br/>temperature, unit: ℃                                |
|       Location       | 0x04 | 0x88 |   9    | latitude(4B) + longitude(4B) + motion_status(1B)                        |
|       Position       | 0x05 | 0x00 |   1    | position(1B)<br/>position, values: (0: normal, 1: tilt)                 |
|      Wifi Scan       | 0x06 | 0xD9 |   9    | ID(1B) + MAC(6B) + RSSI(1B) + motion_status(1B)                         |
|    Tamper Status     | 0x07 | 0x00 |   1    | tamper_status(1B)<br/>tamper_status, values: (0: install, 1: uninstall) |
| Temperature Abnormal | 0x83 | 0x67 |   3    | temperature(2B) + temperature_abnormal(1B)                              |
|     History Data     | 0x20 | 0xCE |   12   | timestamp(4B) + longitude(4B) + latitude(4B)                            |

motion_status

|    BITS     | 7 - 4                                                          | 3 - 0                                                                   |
|:-----------:|:---------------------------------------------------------------|:------------------------------------------------------------------------|
| DESCRIPTION | Geofence Status, (0: inside, 1: outside, 2: unset, 3: unknown) | Motion Status, (0: unknown, 1: start moving, 2: moving, 3: stop moving) |



## Example

```json
// All:
{
  "hex": "01756403671B010488FFFFFFFFFFFFFFFF3305000106D9081CC316222DF9C31006D90824E124F6A667B62106D90824E124F54DE3BC0206D90824E124F57971B23306D90824E124F319A8C820",
  "data": "AXVkA2cbAQSI//////////8zBQABBtkIHMMWIi35wxAG2Qgk4ST2pme2IQbZCCThJPVN47wCBtkIJOEk9XlxsjMG2Qgk4STzGajIIA=="
}

// 01 75 64                     - BATTERY
// 03 67 1B01                   - TEMPERATURE
// 04 88 36BF7701 F0000907 22   - LOCATION, Geofence Status = 2 ("unset"), Motion Status = 2 ("moving")
// 05 00 00                     - DEVICE POSITION
// HexTobytesToBase64: AXVkA2cbAQUAAASINr93AfAACQci 
{
  "battery": 100,
  "ggeofence_status_location": "unset",
  "longitude": 118.030576,
  "latitude": 24.62495,
  "motion_status_location": "moving",
  "position": "normal",
  "temperature": 28.3
}
```

```json
// 01756403671B010488FFFFFFFFFFFFFFFF3305000106D9081CC316222DF9C31006D90824E124F6A667B62106D90824E124F54DE3BC0206D90824E124F57971B23306D90824E124F319A8C820
// 01 75 64                   - BATTERY
// 03 67 1B01                 - TEMPERATURE
// 04 88 FFFFFFFFFFFFFFFF 33  - LOCATION, Geofence Status = 3 ("unknown"), Motion Status = 3 ("stop")
// 05 00 01                   - DEVICE POSITION
// 06 D9 081CC316222DF9C310   - Wi-Fi SCAN RESULT
// 06 D9 0824E124F6A667B621 
// 06 D9 0824E124F54DE3BC02 
// 06 D9 0824E124F57971B233 
// 06 D9 0824E124F319A8C820
// HexToBase64: AXVkA2cbAQSI//////////8zBQABBtkIHMMWIi35wxAG2Qgk4ST2pme2IQbZCCThJPVN47wCBtkIJOEk9XlxsjMG2Qgk4STzGajIIA==
{
  "battery": 100,
  "temperature": 28.3,
  "latitude": 4294.9673,
  "longitude": 4294.9673,
  "motion_stat_location": "stop",
  "geofence_status_location": "unknown",
  "position": "tilt",
  "motion_status_wifi": "unknown",
  "geofence_status_wifi": "unset",
  "wifi": [{
    "group": 8,
    "mac": "1C:C3:16:22:2D:F9",
    "rssi": -61,
    "motion_status": "unknown",
    "geofence_status": "outside"
  }, {
    "group": 8,
    "mac": "24:E1:24:F6:A6:67",
    "rssi": -74,
    "motion_status": "start",
    "geofence_status": "unset"
  }, {
    "group": 8,
    "mac": "24:E1:24:F5:4D:E3",
    "rssi": -68,
    "motion_status": "moving",
    "geofence_status": "inside"
  }, {
    "group": 8,
    "mac": "24:E1:24:F5:79:71",
    "rssi": -78,
    "motion_status": "stop",
    "geofence_status": "unknown"
  }, {
    "group": 8,
    "mac": "24:E1:24:F3:19:A8",
    "rssi": -56,
    "motion_status": "unknown",
    "geofence_status": "unset"
  }],
  "wifi_scan_result": "finish"
}
```
