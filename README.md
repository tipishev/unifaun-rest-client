# unifaun-rest-client

## Examples

### List Schenker pickup locations by zip
```python
from unifaun import UnifaunClient
from unifaun.codes.carriers import DB_SCHENKER_SVERIGE as SCHENKER
from unifaun.codes.countries import SWEDEN

client = UnifaunClient(user=API_ID, password=API_SECRET)
local_pickups = client.get_agents(zip=17144, countryCode=SWEDEN, type=SCHENKER)
print(local_pickups)
```

```
[{'address1': 'SKYTTEHOLMSVÄGEN 5',
  'address2': '',
  'city': 'SOLNA',
  'contact': '',
  'countryCode': 'SE',
  'email': None,
  'fax': None,
  'id': '0136',
  'name': 'MALINS KIOSK',
  'openingHours': 'M-F830-1830 L10-18 S STÄNGT',
  'phone': '',
  'serviceCode': None,
  'serviceType': None,
  'sms': None,
  'state': None,
  'zipcode': '17144'}]
```

### Create a shipment and save shipping slip PDF
```python
receiver = {
    'name': 'Bob',
    'address1': 'Test Street 5-6',
    'zipcode': 41121,
    'city': 'GÖTEBORG',
    'country': SWEDEN,
    'phone': '+46 31 725 34 00',
    'email': 'a@b.com',
}

parcel = {
    'copies': '1',
    'weight': '37.5',
    'contents': 'important things',
    'valuePerParcel': True,
}

option = {
    'id': 'ENOT',
    'message': 'This is order number 123456789',
    'to': 'sales@unifaun.com',
    'languageCode': 'SE',
    'from': 'info@unifaun.com',
}

shipment = {
    'sender': DEFAULT_SENDER,
    'receiver': receiver,
    'parcels': [parcel],
    'orderNo': '123456789',
    'senderReference': 'Mr. Sender',
    'receiverReference': 'Mr. Receiver',
    'service': POSTNORD,
    'options': [option],
}

result = client.create_shipment(pdfConfig=LASER_A4, shipment=shipment)
print(result)
```

```
[{'changed': '2016-09-29T14:48:34.560+0000',
  'consolidated': False,
  'created': '2016-09-29T14:48:34.560+0000',
  'href': 'https://api.unifaun.com/rs-extapi/v1/shipments/31415926',
  'id': '31415926',
  'normalShipment': True,
  'orderNo': '123456789',
  'parcelCount': 1,
  'parcels': [{'parcelNo': '69799319669SE',
               'reference': None,
               'returnParcelNo': None}],
  'pdfs': [{'description': 'Label',
            'href': 'https://api.unifaun.com/rs-extapi/v1/shipments/31415926/pdfs/271826',
            'id': '271826',
            'pdf': None}],
  'previousPdfs': None,
  'rcvCity': 'GÖTEBORG',
  'rcvCountry': 'SE',
  'rcvName': 'Bob',
  'rcvZipcode': '41121',
  'reference': 'Mr. Sender',
  'returnShipment': False,
  'serviceId': 'P15',
  'shipDate': '2016-09-29T14:48:34.000+0000',
  'shipmentNo': None,
  'sndCity': 'SOLNA',
  'sndCountry': 'SE',
  'sndName': 'Sender AB',
  'sndZipcode': '17144',
  'status': 'PRINTED'}]
```
