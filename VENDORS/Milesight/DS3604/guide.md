### Template Data Definition

| ID(1Byte) |  Type(1Byte)  | Template ID(Bit 6-7) | Block ID(Bit 0-6) | Data Length(1B) | Data(N Bytes) |
| :-------: | :-----------: | :------------------: | :---------------: | :-------------: | :-----------: |
|   0xFB    |     0x01      |          00          |      000000       |      0x05       |  4d696c6573   |
| Template  | Text/QR Frame |     Template ID      |     Block ID      |   Data Length   | UTF-8 Unicode |
|           |               |          1           |      text 1       |     5 Bytes     |     Miles     |

-   Id
    -   Template id range `0 - 1`
    -   Text block id range `0 - 9`
    -   QRcode block id `10`

## Example

```json
// 017564 FB0100054D696C6573 FB010A0568656C6C6F
{
    "battery": 100,
    "template": 1,
    "text_1": "Miles",
    "qrcode": "hello"
}
```