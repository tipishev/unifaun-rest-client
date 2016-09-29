# /addresses/agents
Find agents close to a receiver's address for a carrier. Request is made by supplying country and carrier code and a zipcode.

**Carrier codes**
- **SBTL** (DB Schenker Sverige)
- **PP** (DB Schenker Privpak Sverige)
- **PPFI** (DB Schenker Privpak Finland)
- **POSTNORD** (PostNord Sverige)
- **DHLSP** (DHL ServicePoint)
- **DHLSPCOD** (DHL ServicePoint C.O.D.)
- **GLS** (GLS)
- **MHM** (Matkahuolto)
- **MHT** (Matkahuolto - Tradeka Retail Shops)
- **ITELLA** (Posti)
- **ITELLASP** (Posti SmartPOST)
- **BRING** (Bring)
- **BUSSGODS** (Bussgods)

**Response**
- **id** *(string)*
- **name** *(string)*
- **address1** *(string)*
- **address2** *(string)*
- **zipcode** *(string)*
- **city** *(string)*
- **state** *(string)*
- **countryCode** *(string)*
- **contact** *(string)*
- **phone** *(string)*
- **fax** *(string)*
- **email** *(string)*
- **sms** *(string)*
- **serviceType** *(string)*
    - Bring only.
- **serviceCode** *(string)*
    - Bring only.
- **openingHours** *(string)*
    - Bring only.


# /addresses/status
Create validation status for an address.

**Request**
- **name** *(string)*
- **address1** *(string)*
- **address2** *(string)*
- **zipcode** *(string)*
- **city** *(string)*
- **state** *(string)*
- **countryCode** *(string)*
- **contact** *(string)*
- **phone** *(string)*
- **fax** *(string)*
- **email** *(string)*
- **sms** *(string)*

**Response**
- **location** *(string)*
	- Location in request.
- **messageId** *(string)*
	- System message ID.
- **message** *(string)*
	- System message.
- **arguments** *(string)*
	- Message arguments.
- **error** *(boolean)*
	- Error.

# /addresses/zipcodes
Get zipcode information by supplying country code and zipcode in the request.

**Response**
- **city** *(string)*
    - Zipcode's city.
- **pattern** *(string)*
    - Formatting pattern, **N** = number, **A** = letter.
- **valid** *(boolean)*
    - Validity status.
- **box** *(boolean)*
    - Zipcode belongs to a postal box.
- **rural** *(boolean)*
    - Zipcode is in rural delivery area (i.e. longer delivery time).
- **customer** *(boolean)*
    - Zipcode belongs to a certain company, i.e. is company specific.
