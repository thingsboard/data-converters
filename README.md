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
