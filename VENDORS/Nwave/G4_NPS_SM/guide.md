# Nwave G4 NPS SM Sensor Guide

## 4.2 Uplink Messages

| Message Type               | Port | Description                                                                                                                                       |
|----------------------------|------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Parking Status             | 1    | Sends the current parking status.                                                                                                                 |
| Heartbeat                  | 2    | Sends health monitoring data, including battery level and temperature.                                                                            |
| Startup                    | 3    | Sent after every startup, reboot, or re-join event to indicate the version and reset cause.                                                      |
| SDI Tag Registration       | 10   | Provides a 32-bit SDI tag serial ID.                                                                                                              |

---

## 4.2.1 Parking Status

| Byte | Bits | Name                  | Description                                                                                              |
|------|------|------------------------|----------------------------------------------------------------------------------------------------------|
| 0    | 0    | Parking status         | `0`: Free parking space, `1`: Occupied parking space                                                     |
| 0    | 7.1  | Compressed duration    | Compressed duration of the previous status                                                               |

**Compressed Duration Calculation Table**:

| Compressed Duration            | Calculated Duration (minutes)                    | Max Compression Error (minutes)** |
|--------------------------------|--------------------------------------------------|-----------------------------------|
| compressed_duration < 90       | `compressed_duration`                            | 0                                 |
| 90 ≤ compressed_duration < 120 | `90 + (compressed_duration - 90) * 5`            | 4                                 |
| 120 ≤ compressed_duration < 127| `240 + (compressed_duration - 120) * 60`         | 59                                |
| 127                            | `>= 660`                                         | undefined                         |

**Note**: The total error of previous status duration consists of:
- Maximum compression error
- Rounding error up to 1 minute (duration is calculated in full minutes)
- Transmission delay caused by LoRaWAN in-air limitations

Actual previous status duration is in `[Calculated duration .. Calculated duration + total error]`.

---

## 4.2.2 Heartbeat

| Byte | Bits | Name                  | Description                                                                                              |
|------|------|------------------------|----------------------------------------------------------------------------------------------------------|
| 0    | 0    | Parking status         | `0`: Free parking space, `1`: Occupied parking space                                                     |
| 1    | 7.0  | Battery voltage        | Formula: `Vbat = (2500 + X*4)mV` where X is the value as unsigned integer                                |
| 2    | 7.0  | Temperature (voltage)  | Temperature at which battery voltage was measured                                                        |
| 3    | 7.0  | Min temperature        | Minimum temperature over the last 24 hours                                                               |
| 4    | 7.0  | Max temperature        | Maximum temperature over the last 24 hours                                                               |
| 5    | 5.0  | Current consumption    | Average current consumption for the last 24 hours, `Current = (X * 10)μA`                                |

**Note**: Heartbeat messages initiate the re-join procedure if the sensor has lost connection.

---

## 4.2.3 Startup

| Byte | Name                      | Description                                                                                               |
|------|----------------------------|-----------------------------------------------------------------------------------------------------------|
| 0    | Major version number       | Major part of the version number                                                                          |
| 1    | Minor version number       | Minor part of the version number                                                                          |
| 2    | Micro version number       | Micro part of the version number                                                                          |
| 3    | Reset cause                | Code indicating the cause of reset (e.g., `0x00`: No reset, `0x01`: Watchdog reset, `0x02`: Power On)     |
| 4    | Parking status             | `0`: Free parking space, `1`: Occupied parking space                                                      |

---

## 4.2.4 SDI Tag Registration

| Byte | Name                          | Description                                                                                              |
|------|--------------------------------|----------------------------------------------------------------------------------------------------------|
| 0    | Registration byte              | Varies based on the timing of the registration message                                                   |
| 1-4  | SDI tag serial address bits    | Contains 32-bit SDI tag serial ID in Big Endian format                                                   |

---

## 4.2.5 Debug Messages

| Byte | Debug Code                    | Meaning                                         | Additional Parameters                               |
|------|--------------------------------|-------------------------------------------------|----------------------------------------------------|
| 404 (0x194) | Calibration completed | Calibration has been completed                    | 1 byte                                             |
| 899 (0x383) | Invalid user request   | Downlink command not recognized or configuration cannot be used | None                                               |
| 805 (0x325) | No change in config    | Provided parameters match current configuration  | None                                               |
