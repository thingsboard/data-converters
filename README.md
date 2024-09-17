# Introduction

This library is designed to simplify process of the integration setup for popular IoT devices. 
ThingsBoard Team is maintaining the library and welcomes outside contributions from community.

The contents of the library are periodically synchronized with running ThingsBoard instances. 
Any changes made to the main branch will be propagated to these instances within 24 hours.

# Library Structure

The library consists of ThingsBoard Data Converters, organized by Vendor and Integration type.

The structure is as follows:

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


Here is a breakdown of the structure:

- **VENDORS** - Root-level folder containing all vendors.
  
  - **Milesight** - Name of the vendor.

    - `info.json` - Describes the vendor using the following structure:

      ```json
      {
        "url": "https://www.milesight.com/",
        "description": "Milesight offers a range of sensing products to capture valuable data for diverse applications. It applies emerging technologies such as AI, 5G, and IoT to various scenarios. By responding quickly to customer challenges, Milesight collaborates with partners to deliver data-driven solutions for smart buildings, traffic management, security, cities, and more."
      }
      ```

    - `logo.svg` - A scalable image containing the vendor’s logo.

- **WT201** - Device model.

  - `info.json` - Describes the device using the following structure:

    ```json
    {
      "url": "https://www.milesight.com/product/wt201/",
      "description": "The WT201 is a smart occupancy sensor that detects indoor movement and monitors various environmental factors."
    }
    ```

  - `photo.png` - Photo of the device (optional).

- **ChirpStack** - The integration type used to connect the device. Multiple integration types may be supported for the same device model. Supported integration types include:
  
  `Actility ThingPark`, `Apache Kafka`, `Apache Pulsar`, `AWS IoT`, `AWS Kinesis`, `AWS SQS`, `Azure Event Hub`, `Azure IoT Hub`, `Azure Service Bus`, `ChirpStack`, `CoAP`, `HTTP`, `IBM Watson IoT`, `KPN`, `LORIOT`, `MQTT`, `OPC UA`, `Particle`, `PubSub`, `RabbitMQ`, `Sigfox`, `TCP`, `The Things Stack Industries`, `Tuya`, `UDP`.

  - **uplink** - Subfolder for uplink data converters:

    - `converter.json` - The converter entity exported as JSON from the platform. Both TBEL and JS converters are supported.
    - `metadata.json` - Represents a map of metadata keys and values (optional).
    - `payload.json` - An example of an incoming payload for the device and integration type. This payload will automatically load into the debug window when the converter is imported from the library. You may also use `payload.txt` or `payload.base64` for text or binary payload representation.
    - `result.json` - Expected result from the converter based on the provided payload and metadata, used to validate that the converter works correctly.
    - `payload_XX.json`, `result_XX.json` - Additional payload files for automated tests.

  - **downlink** - Subfolder for downlink data converters with a structure similar to the uplink folder (optional).

# How to Contribute?

We encourage you to contribute by creating a Pull Request (PR) for this repository with your device converters. Please adhere to the proposed [library structure](#library-structure).

If you encounter any issues creating a Pull Request, you may alternatively create a [public gist](https://gist.github.com/) with the necessary files and submit a GitHub issue containing the link to your gist.

Once submitted, our team will review the request and run manual and automated tests. After the PR is merged, it may take up to 24 hours for the new converter to be available in existing ThingsBoard instances.
