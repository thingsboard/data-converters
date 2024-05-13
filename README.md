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
