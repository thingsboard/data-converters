# data-converters
Library of Data Converters grouped by integration type and vendor

The sample structure has already been committed to the repository. For example:
```
├── LICENSE
├── README.md
└── VENDORS
    └── Milesight
        ├── info.json
        ├── logo.svg
        └── WS202
            ├── ChirpStack
            │   └── uplink
            │       ├── converter.json
            │       ├── metadata.json
            │       ├── payload.base64
            │       ├── payload.json
            │       ├── payload.txt
            │       └── result.json
            ├── guide.md
            ├── info.json
            ├── Loriot
            └── photo.png
```

Here

- LICENSE - regular Apache 2.0 License. 

- README.md - description of the project with instructions on how to add a new converter.

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

- WS202 - the device model.

- guide.md - markdown document with the description of the device payload.

- info.json - describes the device with the following structure:

```
{
  "url": "https://www.milesight.com/iot/product/lorawan-sensor/ws202",
  "label" "WS202 PIR & Light Sensor",
  "description": "PIR sensor based on passive infrared technology to detect a motion or occupancy."
}

```

- photo.png - photo of the device. Optional. 

- ChirpStack and Loriot are folders named after the types of integrations supported by this device. The enumeration will be provided later and must be listed in README.md

- uplink or downlink- subfolder for each integration type that contains converter.json - the exported converter, optional  metadata.json with the message metadata, and one of payload.json,  payload.txt or payload.base64 that contains sample data for running the test. The expected result is stored here in result.json
  
