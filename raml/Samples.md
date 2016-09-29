# Sample requests
We have created a small collection of sample requests demonstrating a number of common scenarios. For simplicty and better readability, all samples except the first one are made for use with /stored-shipments resource's POST method but can also be used for /shipments resource's POST method if pdfConfig object and "shipment" header are added as in the first sample.
The requests are service-neutral, i.e. they should work for any service that matches certain criteria regarding addon-services and routes. Replace the "..." in service object's property "id" with desired service code.
Also, replace the ".." in senderPartners object's properties "id" and "custNo" to corresponding carrier ID and customer number. Carrier and service codes can be found in your account under the Help -> Code lists section.

#### Service with single parcel and no addons


```json
{
    "pdfConfig": {
        "target4XOffset": 0,
        "target2YOffset": 0,
        "target1Media": "laser-ste",
        "target1YOffset": 0,
        "target3YOffset": 0,
        "target2Media": "laser-a4",
        "target4YOffset": 0,
        "target4Media": null,
        "target3XOffset": 0,
        "target3Media": null,
        "target1XOffset": 0,
        "target2XOffset": 0
    },
    "shipment": {
        "sender": {
            "quickId": "1",
            "name": "Unifaun AB",
            "address1": "Skeppsbron 5-6",
            "zipcode": "41121",
            "city": "GÖTEBORG",
            "country": "SE",
            "phone": "+46 31 725 35 00",
            "email": "info@unifaun.com"
        },
        "senderPartners": [{
            "id": "...",
            "custNo": "..."
        }],
        "receiver": {
            "name": "Test Sverige",
            "address1": "Testgatan 1",
            "zipcode": "41763",
            "city": "GÖTEBORG",
            "country": "SE",
            "phone": "+46 31 725 35 00",
            "email": "test@sweden.se"
        },
        "service": {
            "id": "..."
        },
        "parcels": [{
            "copies": 1,
            "weight": 5,
            "contents": "Important stuff",
            "valuePerParcel": true
        }],
        "orderNo": "Orderno 001",
        "senderReference": "Some reference"
    }
}
```


#### Service with two parcels and no addons


```json
{
    "sender": {
        "quickId": "1",
        "name": "Unifaun AB",
        "address1": "Skeppsbron 5-6",
        "zipcode": "41121",
        "city": "GÖTEBORG",
        "country": "SE",
        "phone": "+46 31 725 35 00",
        "email": "info@unifaun.com"
    },
    "senderPartners": [{
        "id": "...",
        "custNo": "..."
    }],
    "receiver": {
        "name": "Test Sverige",
        "address1": "Testgatan 1",
        "zipcode": "41763",
        "city": "GÖTEBORG",
        "country": "SE",
        "phone": "+46 31 725 35 00",
        "email": "test@sweden.se"
    },
    "service": {
        "id": "...",
        "addons": [{
            "id": "NOT"
        }]
    },
    "parcels": [{
        "copies": 1,
        "weight": 5,
        "contents": "Important stuff",
        "valuePerParcel": true
    },
    {
        "copies": 1,
        "weight": 8,
        "contents": "Some other stuff",
        "valuePerParcel": true
    }],
    "orderNo": "Orderno 001",
    "senderReference": "Some reference"
}
```


#### Service with one addon (Notification)


```json
{
    "sender": {
        "quickId": "1",
        "name": "Unifaun AB",
        "address1": "Skeppsbron 5-6",
        "zipcode": "41121",
        "city": "GÖTEBORG",
        "country": "SE",
        "phone": "+46 31 725 35 00",
        "email": "info@unifaun.com"
    },
    "senderPartners": [{
        "id": "...",
        "custNo": "..."
    }],
    "receiver": {
        "name": "Test Sverige",
        "address1": "Testgatan 1",
        "zipcode": "41763",
        "city": "GÖTEBORG",
        "country": "SE",
        "phone": "+46 31 725 35 00",
        "email": "test@sweden.se"
    },
    "service": {
        "id": "...",
        "addons": [{
            "id": "NOT"
        }]
    },
    "parcels": [{
        "copies": 1,
        "weight": 5,
        "contents": "Important stuff",
        "valuePerParcel": true
    }],
    "orderNo": "Orderno 001",
    "senderReference": "Some reference"
}
```


#### Service with two addons (Notification and Receiver pays)


```json
{
    "sender": {
        "quickId": "1",
        "name": "Unifaun AB",
        "address1": "Skeppsbron 5-6",
        "zipcode": "41121",
        "city": "GÖTEBORG",
        "country": "SE",
        "phone": "+46 31 725 35 00",
        "email": "info@unifaun.com"
    },
    "senderPartners": [{
        "id": "...",
        "custNo": "..."
    }],
    "receiver": {
        "name": "Test Sverige",
        "address1": "Testgatan 1",
        "zipcode": "41763",
        "city": "GÖTEBORG",
        "country": "SE",
        "phone": "+46 31 725 35 00",
        "email": "test@sweden.se"
    },
    "service": {
        "id": "...",
        "addons": [{
            "id": "NOT"
        },
        {
            "id": "RPAY",
            "custNo": "12345674"
        }]
    },
    "parcels": [{
        "copies": 1,
        "weight": 5,
        "contents": "Important stuff",
        "packageCode": "PC",
        "valuePerParcel": true
    }],
    "orderNo": "Orderno 001",
    "senderReference": "Some reference"
}
```


#### International service outside EU


```json
{
    "sender": {
        "quickId": "1",
        "name": "Unifaun AB",
        "address1": "Skeppsbron 5-6",
        "zipcode": "41121",
        "city": "GÖTEBORG",
        "country": "SE",
        "phone": "+46 31 725 35 00",
        "email": "info@unifaun.com"
    },
    "senderPartners": [{
            "id": "...",
            "custNo": "..."
    }],
    "receiver": {
        "name": "Test Norge",
        "address1": "Testgatan 1",
        "zipcode": "0185",
        "city": "OSLO",
        "country": "NO",
        "phone": "+46 31 725 35 00",
        "email": "test@norway.no"
    },
    "service": {
        "id": "..."
    },
    "customsDeclaration": {
        "invoiceType": "STANDARD",
        "invoiceNo": "2016-05-01",
        "termCode": "022",
        "currencyCode": "SEK",
        "lines": [{
            "statNo": "12345678",
            "value": 150,
            "contents": "Imported stuff",
            "copies": 1,
            "netWeight": 2,
            "sourceCountryCode": "SE",
            "valuesPerItem": true
        }],
        "printSet": ["proforma"]
    },
    "parcels": [{
        "copies": 1,
        "weight": 5,
        "contents": "Important stuff",
        "packageCode": "PC",
        "valuePerParcel": true
    }],
    "orderNo": "Orderno 001",
    "senderReference": "Some reference"
}
```


#### Service with Dangerous goods addon


```json
{
    "sender": {
        "quickId": "1",
        "name": "Unifaun AB",
        "address1": "Skeppsbron 5-6",
        "zipcode": "41121",
        "city": "GÖTEBORG",
        "country": "SE",
        "phone": "+46 31 725 35 00",
        "email": "info@unifaun.com"
    },
    "senderPartners": [{
        "id": "...",
        "custNo": "..."
    }],
    "receiver": {
        "name": "Test Sverige",
        "address1": "Testgatan 1",
        "zipcode": "41763",
        "city": "GÖTEBORG",
        "country": "SE",
        "phone": "+46 31 725 35 00",
        "email": "test@sweden.se"
    },
    "service": {
        "id": "...",
        "addons": [{
            "id": "DNG"
        }]
    },
    "parcels": [{
        "copies": 1,
        "weight": 5,
        "contents": "Important stuff",
        "packageCode": "PC",
        "valuePerParcel": true,
        "dangerousGoods": {
            "unCode": "1234",
            "hazardCode": "1.4",
            "packageCode": "Liquids",
            "packageType": "II",
            "description": "Petroleum",
            "adrClass": "1",
            "netVolume": 12,
            "trCode": "E"
        }
    }],
    "orderNo": "Orderno 001",
    "senderReference": "Some reference"
}
```


#### Providing sender data
Sender data can be provided in three ways. Sender information in all samples above is provided as described in case 1 below. 
1. Completely in request with address data and relevant carrier information
2. Only as "quickId" property in request. The rest of the information is fetched from your account, provided that you have a sender in your address book with matching Quick ID.
3. Partly in request, missing data will be autocompleted from your address book, provided that you have a sender in your address book with matching Quick ID.


**Case 2**


```json
{
    "sender": {
        "quickId": "1"
    },
    "receiver": {
        "name": "Test Sverige",
        "address1": "Testgatan 1",
        "zipcode": "41763",
        "city": "GÖTEBORG",
        "country": "SE",
        "phone": "+46 31 725 35 00",
        "email": "test@sweden.se"
    },
    "service": {
        "id": "..."
    },
    "parcels": [{
        "copies": 1,
        "weight": 5,
        "contents": "Important stuff",
        "valuePerParcel": true
    }],
    "orderNo": "Orderno 001",
    "senderReference": "Some reference"
}
```


**Case 3**


```json
{
    "sender": {
        "quickId": "1",
        "name": "Some Company",
        "email": "somecompany@test.com"
    },
    "receiver": {
        "name": "Test Sverige",
        "address1": "Testgatan 1",
        "zipcode": "41763",
        "city": "GÖTEBORG",
        "country": "SE",
        "phone": "+46 31 725 35 00",
        "email": "test@sweden.se"
    },
    "service": {
        "id": "..."
    },
    "parcels": [{
        "copies": 1,
        "weight": 5,
        "contents": "Important stuff",
        "valuePerParcel": true
    }],
    "orderNo": "Orderno 001",
    "senderReference": "Some reference"
}
```


The principle described above is applicable to all shipment parties involved, e.g. sender, receiver, payer etc. 
