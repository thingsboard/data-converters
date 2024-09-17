# Introduction

This library is designed to simplify process of the integration setup for popular IoT devices. 
ThingsBoard Team is maintaining the library and welcomes outside contributions from community. 

# Library Structure

Library of ThingsBoard Data Converters grouped by Vendor and integration type.

The library structure are as follows:

```
└── VENDORS
    └── Milesight
        ├── info.json
        ├── logo.svg
        └── WT201
            ├── info.json
            ├── photo.png
            └── ChirpStack
                └── uplink
                │   ├── converter.json
                │   ├── metadata.json
                │   ├── payload.json
                │   └── result.json
                └── downlink
                    ├── converter.json
                    ├── metadata.json
                    ├── payload.json
                    └── result.json
```

Here

- VENDORS - root level folder with all vendors. 

- Milesight - the name of the vendor. 

  - info.json - describes the vendor with the following structure:


    ```
    {
      "url" : "https://www.milesight.com/",
      "description" : "Milesight offers multi-potential sensing products to capture the most meaningful data and makes it accessible across diverse applications. It innovatively applies emerging technologies such as Al, 5G, and loT to distinct use scenarios. With a commitment to making sensing matter, Milesight quickly responds to customer-specific challenges and collaborates with an expanding network of partners to deliver unique data value. It is determined to make real, positive impacts in smart buildings, intelligent traffic, intelligent security, smart cities, and beyond."
    }
    ```

  - logo.svg - a scalable image that contains the vendor logo.

- WT201 - the device model.

  - info.json - describes the device with the following structure:

    ```
    {
      "url": "https://www.milesight.com/iot/product/lorawan-sensor/ws202",
      "label" "WS202 PIR & Light Sensor",
      "description": "PIR sensor based on passive infrared technology to detect a motion or occupancy."
    }
    
    ```

  - photo.png - photo of the device. Optional. 

- ChirpStack - the integration type which is used to connect the device. Multiple integration types may be supported for the same device model. Complete list of supported integration type folder names:
  'Actility ThingPark', 'Apache Kafka', 'Apache Pulsar', 'AWS IoT', 'AWS Kinesis', 'AWS SQS', 'Azure Event Hub', 'Azure IoT Hub', 'Azure Service Bus', 'ChirpStack', 'CoAP', 'HTTP', 'IBM Watson IoT', 'KPN', 'LORIOT', 'MQTT', 'OPC UA', 'Particle', 'PubSub', 'RabbitMQ', 'Sigfox', 'TCP', 'ThingsStackIndustries', 'Tuya', 'UDP'.

- uplink - subfolder for uplink data convertor:
    - converter.json - converter entity that was exported into JSON from the platform. Both TBEL and JS converters supported. 
    - metadata.json - json object representing the map of the metadata keys and values. Optional.
    - payload.json - an example of incoming payload for particular device and corresponding integration type. This payload will be automatically imported into debug window when you load the converter from the library. Alternatively, you may define `payload.txt` or `payload.base64` to represent payload in text or binary form. 
    - result.json - an expected result of the convertor based on provided payload and metadata. Used to double-check that the convertor code is working as expected.
    - payload_XX.json, result_XX.json - additional payload files for automatic tests. 
- downlink - subfolder for downlink data convertor with the structure similar to uplink folder. Optional.

# How to contribute?

We welcome you to create a Pull Request for this repository with your device convertors. We expect you to use the proposed library [structure](#library-structure). 
Once created, our team will review the request and run manual + automatic tests. 
Once the PR is merged, it will take up to 24 hours for existing ThingsBoard instances to fetch new converter. 
  
