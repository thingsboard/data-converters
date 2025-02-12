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
    └── VendorName
        ├── info.json
        ├── logo.svg
        └── DeviceName
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
  
  - **VendorName** - Name of the vendor.

    - `info.json` - Describes the vendor using the following structure:

      ```json
      {
        "url": "https://www.vendorwebsite.com/",
        "description": "VendorName offers a range of sensing products to capture valuable data for diverse applications. It applies emerging technologies such as AI, 5G, and IoT to various scenarios. By responding quickly to customer challenges, VendorName collaborates with partners to deliver data-driven solutions for smart buildings, traffic management, security, cities, and more."
      }
      ```

    - `logo.svg` - A scalable image containing the vendor’s logo.

- **DeviceName** - Device model.

  - `info.json` - Describes the device using the following structure:

    ```json
    {
      "url": "https://www.vendorwebsite.com/product/device-name/",
      "label": "DeviceName: Smart Thermostat. Heat, EM (Emergency) Heat, Cool, Auto",
      "description": "The DeviceName is a smart occupancy sensor that detects indoor movement and monitors various environmental factors."
    }
    ```

  - `photo.png` - Photo of the device.

- **ChirpStack** - The integration type used to connect the device. Multiple integration types may be supported for the same device model. Supported integration types include:
  
  `Actility ThingPark`, `Apache Kafka`, `Apache Pulsar`, `AWS IoT`, `AWS Kinesis`, `AWS SQS`, `Azure Event Hub`, `Azure IoT Hub`, `Azure Service Bus`, `ChirpStack`, `CoAP`, `HTTP`, `IBM Watson IoT`, `KPN`, `LORIOT`, `MQTT`, `OPC UA`, `Particle`, `PubSub`, `RabbitMQ`, `Sigfox`, `TCP`, `The Things Stack Industries`, `Tuya`, `UDP`.

  - **uplink** - Subfolder for uplink data converters:

    - `converter.json` - The converter entity exported as JSON from the platform. Both TBEL and JS converters are supported. Converter Naming Format: `[Converter Name] Uplink Decoder for [Vendor Name] [Model Name]`.
    - `metadata.json` - Represents a map of metadata keys and values.
    - `payload.json` - An example of an incoming payload for the device and integration type. This payload will automatically load into the debug window when the converter is imported from the library. You may also use `payload.txt` or `payload.base64` for text or binary payload representation.
    - `result.json` - Expected result from the converter based on the provided payload and metadata, used to validate that the converter works correctly.
    - `payload_XX.json`, `result_XX.json` - Additional payload files for automated tests.

  - **downlink** - Subfolder for downlink data converters with a structure similar to the uplink folder (optional).

# How to Contribute?

We encourage you to contribute by creating a Pull Request (PR) for this repository with your device converters. Please adhere to the proposed [library structure](#library-structure).

If you encounter any issues creating a Pull Request, you may alternatively create a [public gist](https://gist.github.com/) with the necessary files and submit a GitHub issue containing the link to your gist.

Once you create a PR, our automated validation workflow will be triggered. This workflow checks that all uplink and downlink converters are valid by running the provided payloads through the corresponding converters.

If the validation passes, the PR will be marked as successful, and our team will review the request, performing additional manual and automated tests. After the PR is merged, it may take up to 24 hours for the new converter to become available in existing ThingsBoard instances.

## What to do if validation fails?

If your validation fails (**the workflow is marked with a red cross**) click on the workflow name **Validate Data Converters** to view the detailed logs and identify the issues.

For example, you may encounter a message like this:

`Validation failed for VENDORS/VendorName/DeviceName/ChirpStack/uplink with payload payload.json and result result.json. Expected output does not match.`

This error indicates that the result.json file does not match the actual output generated by the converter when processing the provided payload.json.

To resolve this issue, update your result.json file or modify the converter logic as necessary. After making the required changes, push your updates to the same branch. The validation workflow will automatically re-run and re-check your PR.
