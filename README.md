# unifaun-rest-client

## Quick Start

```python
from unifaun import UnifaunClient
from unifaun.carriers import DB_Schenker_Sverige as Schenker
from unifaun.countries import Sweden

client = UnifaunClient(user=API_ID, password=API_SECRET)
local_pickups = client.get_agents(zip=17144, countryCode=Sweden, type=Schenker)
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
