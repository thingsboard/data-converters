## Payload Definition

|   CHANNEL    | TYPE | LENGTH | DESCRIPTION                                  |
| :----------: | :--: | :----: | -------------------------------------------- |
| Battery Status | string | 1 | Critical<br/>Replace<br/>OK<br/>Good  |
| Temperature    | float  | 2 | temperature, unit: ℃ |

## Example

```json
{
  "name": "as.up.data.forward",
  "time": "2025-11-07T08:52:14.744360741Z",
  "identifiers": [
    {
      "device_ids": {
        "device_id": "rs261-erik-internal",
        "application_ids": {
          "application_id": "thingsboard-ttn-demo"
        },
        "dev_eui": "0025CA00000017C2",
        "join_eui": "ECC07A0000000009",
        "dev_addr": "260BDF71"
      }
    }
  ],
  "data": {
    "@type": "type.googleapis.com/ttn.lorawan.v3.ApplicationUp",
    "end_device_ids": {
      "device_id": "rs261-erik-internal",
      "application_ids": {
        "application_id": "thingsboard-ttn-demo"
      },
      "dev_eui": "0025CA00000017C2",
      "join_eui": "ECC07A0000000009",
      "dev_addr": "260BDF71"
    },
    "correlation_ids": [
      "gs:uplink:01K9ER8B2712V0HV1YBNRF35ZY"
    ],
    "received_at": "2025-11-07T08:52:14.742127657Z",
    "uplink_message": {
      "session_key_id": "AZpdcJdm3ixYYWExQAIgUg==",
      "f_port": 1,
      "f_cnt": 25,
      "frm_payload": "AMQAFdQ=",
      "decoded_payload": {
        "Battery Status": "Good",
        "Device Status": {
          "Backlog Wraparound": "No",
          "Backlogs Available": "Yes",
          "Bandwidth Limitation": "No",
          "Sensor Fault": "No",
          "Unsupported API Version": "No"
        },
        "Temperature": 21.83
      },
      "rx_metadata": [
        {
          "gateway_ids": {
            "gateway_id": "eriks-rg186",
            "eui": "C0EE40FFFF293903"
          },
          "time": "2025-11-07T08:52:14.405836105Z",
          "timestamp": 1645246307,
          "rssi": -69,
          "channel_rssi": -69,
          "snr": 8.25,
          "uplink_token": "ChkKFwoLZXJpa3MtcmcxODYSCMDuQP//KTkDEOPuwZAGGgwIvua2yAYQlLeq/wEguLXJgvHwFA==",
          "received_at": "2025-11-07T08:52:14.516913023Z"
        }
      ],
      "settings": {
        "data_rate": {
          "lora": {
            "bandwidth": 125000,
            "spreading_factor": 7,
            "coding_rate": "4/5"
          }
        },
        "frequency": "868100000",
        "timestamp": 1645246307,
        "time": "2025-11-07T08:52:14.405836105Z"
      },
      "received_at": "2025-11-07T08:52:14.536109379Z",
      "confirmed": true,
      "consumed_airtime": "0.051456s",
      "version_ids": {
        "brand_id": "ezurio",
        "model_id": "rs26x-int-temp-sensor",
        "hardware_version": "rev 1",
        "firmware_version": "1.0.2+1748617279",
        "band_id": "EU_863_870"
      },
      "network_ids": {
        "net_id": "000013",
        "ns_id": "EC656E0000000181",
        "tenant_id": "ttn",
        "cluster_id": "eu1",
        "cluster_address": "eu1.cloud.thethings.network"
      }
    }
  },
  "correlation_ids": [
    "gs:uplink:01K9ER8B2712V0HV1YBNRF35ZY"
  ],
  "origin": "ip-10-100-15-195.eu-west-1.compute.internal",
  "context": {
    "tenant-id": "CgN0dG4="
  },
  "visibility": {
    "rights": [
      "RIGHT_APPLICATION_TRAFFIC_READ"
    ]
  },
  "unique_id": "01K9ER8B8R0V4HDCXNZ34B1H9G"
}
```