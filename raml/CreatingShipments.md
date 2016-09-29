Basically, a shipment consists of at least two parties (sender and receiver), service definition and parcel definition. There are three different methods available that can be used to create a shipment:
- Stored shipment method stores the shipment for later printing.
- Consolidated shipment method returns printed documents immediately and allows continuous printing of labels while holding the EDI message until a close message is received.
- Shipment method returns printed documents immediately.

# Party
There are a number of parties available, their usage depends on requirements of used service. Properties are only explained for sender party as they are identical for other parties as well. However, partner information (objects *senderPartners* and *receiverPartners*) are limited to sender and receiver party.

**Available parties**
- **sender** *(mandatory)*
- **receiver** *(mandatory)*
- **dispatch**
     - Alternative pickup address
- **delivery**
    - Alternative delivery address
- **agent**
    - Specifies agent (delivery point) for B2C services. Ideally, service /addresses/agents can be used to populate this.
- **returnPart**
    - Alternative return address.
- **freightPayer**
    - Alternative freightPayer party. Not to be mistaken for Receiver pays or Other payer addon services.
- **taxPayer**
- **customsPayer**


**Party properties**
- **quickId** *(string)*
    - Corresponds to party's *quickId* value in your account. If used, this is the only value that needs to be present in the request. The rest of party's information will automatically be fetched from your account. Same principle can be applied when specifying pickup agent location, i.e. not all information returned from /addresses/agents lookup needs to be specified for a certain pickup agent, only *quickId* will be enough.
- **orgNo** *(string)*
- **vatNo** *(string)*
- **name** *(string)*
- **address1** *(string)*
- **address2** *(string)*
- **zipcode** *(string)*
- **city** *(string)*
- **state** *(string)*
- **country** *(string)*
- **contact** *(string)*
- **phone** *(string)*
- **fax** *(string)*
- **email** *(string)*
- **mobile** *(string)*
- **doorCode** *(string)*
- **serviceType** *(string)*
    - Not used in request, response only
- **serviceCode** *(string)*
    - Not used in request, response only
- **openingHours** *(string)*
    - Not used in request, response only


## Party - Partner information
Partner object contains infromation about sender's and/or receiver's partner related data such as customer number, EDI address etc.

- **id** *(string)*
    - Carrier ID. Please refer to Help -> Code Lists in your account for available carrier IDs.
- **agentNo** *(string)*
    - Not used.
- **custNo** *(string)*
    - Party's customer/contract number for provided carrier.
- **custNoIssuerCode** *(string)*
    - Customer/contract number issuer code, if provided by carrier.
- **palletRegNo** *(string)*
    - Pallet reg. number for EUR-pallet pool.
- **ediAddress** *(string)*
    - EDI address, if provided by carrier.
- **senderId** *(string)*
    - Used to specify domestic EDI prefix for DB Schenker Norway or GLS Customer ID, if provided by carrier. 
- **bookingId** *(string)*
    - Booking ID number, if provided by carrier.
- **bookingOffice** *(string)*
    - Booking office, if provided by carrier.
- **bookingEmail** *(string)*
    - Booking office, if provided by carrier.
- **sourceCode** *(string)*
    - Source code, if provided by carrier.
- **ediUserId** *(string)*
    - User ID for EDI transfer, if provided by carrier.
- **ediPassword** *(string)*
    - Password for EDI transfer, if provided by carrier.
- **ediKey** *(string)*
    - Key for EDI transfer, if provided by carrier.
- **externalIdentifier** *(string)*
    - Special identifier, if provided by carrier (DSV subaccount number, Post Norway commissionary number, MTD subaccount number, Posten Åland customer number for Posti).


# Shipment
- **favorite** *(string)*
    - Defines the print favorite preset in your account which is used to auto-complete the request if necessary.
- **profileGroup** *(string)*
    - Defines the profile group where the shipment is to be stored in your account.
- **note** *(string)*
    - Internal value that is searchable in Stored printings and is also saved in shipment history. Not printed on any documents.
- **printer** *(string)*
    - Sends the print job to corresponding printer mapping set in Unifaun OnlinePrinter.
- **test** *(boolean)*
    - Used for testing. Prints out TEST on label and disables EDI forwarding. Note: Does not disable pre-notification e-mail if such is specified.
- **linkPrintKey** *(string)*
    - An attribute used by Link to Print feature. If used, system can send an e-mail message to a recipient containing a link from which the recipient can print shipping documents at his/hers convenience. Link to print can be used for both normal and return shipments.
- **orderNo** *(string)*
    - Internal value that is searchable in Stored printings and is also saved in shipment history. Not printed on any documents. 
- **mergeId** *(string)*
    - Mandatory consolidation key used only for Consolidation feature.
- **freeText1** *(string)*
    - Free text field that can be used for delivery instructions, for example. Recommended length 30 characters. Printed on shipping documents.
- **freeText2** *(string)*
    - Free text field that can be used for delivery instructions, for example. Recommended length 30 characters. Printed on shipping documents.
- **freeText3** *(string)*
    - Free text field that can be used for delivery instructions, for example. Recommended length 30 characters. Printed on shipping documents.
- **freeText4** *(string)*
    - Free text field that can be used for delivery instructions, for example. Recommended length 30 characters. Printed on shipping documents.
- **senderReference** *(string)*
    - Shipment reference. Recommended length 17 characters, without blank spaces.
- **receiverReference** *(string)*
    - Receiver's reference. Recommended length 17 characters, without blank spaces.
- **goodsDescription** *(string)*
    - Goods description used by certain carrier services.
- **bulkId** *(string)*
    - Bulk ID used by certain carrier services.
- **totalEurPallets** *(integer, minimum: 0)*
    - Total number of EUR pallets in shipment.
- **totalHalfPallets** *(integer, minimum: 0)*
    - Total number of half pallets in shipment.
- **totalQuarterPallets** *(integer, minimum: 0)*
    - Total number of quarter pallets in shipment.
- **totalWeight** *(number, minimum: 0)*
    - Total shipment weight.
- **totalVolume** *(number, minimum: 0)*
    - Total shipment volume.
- **totalLoadingMeters** *(number, minimum: 0)*
    - Total amount of loading meters for shipment.
- **totalSortCode** *(string)*
    - Sort code for sort/quant (DHL).
- **totalQuantity** *(integer, minimum: 0)*
    - Quantity for sort/quant (DHL).
- **totalPieces** *(integer, minimum: 0)*
    - Total number of pieces for shipment.
- **totalPallets** *(integer, minimum: 0)*
    - Total number of pallets in shipment.
- **waybillFreeText1** *(string)*
    - Free text field that can be used for delivery instructions, for example. Recommended length 30 characters. Printed only on waybill documents.
- **waybillFreeText2** *(string)*
    - Free text field that can be used for delivery instructions, for example. Recommended length 30 characters. Printed only on waybill documents.
- **waybillFreeText3** *(string)*
    - Free text field that can be used for delivery instructions, for example. Recommended length 30 characters. Printed only on waybill documents.
- **waybillFreeText4** *(string)*
    - Free text field that can be used for delivery instructions, for example. Recommended length 30 characters. Printed only on waybill documents.
- **waybillFreeText5** *(string)*
    - Free text field that can be used for delivery instructions, for example. Recommended length 30 characters. Printed only on waybill documents.
- **waybillSpecialAgreement** *(string)*
    - Free text field for Special Agreement information on waybill. Recommended length 30 characters.
- **waybillDocuments1** *(string)*
    - Free text field for Waybill Documents information on waybill. Recommended length 30 characters.
- **waybillDocuments2** *(string)*
    - Free text field for Waybill Documents information on waybill. Recommended length 30 characters.
- **waybillCondition** *(string)*
    -  Free text field for Waybill Condition information on waybill. Recommended length 30 characters.
- **termsCode** *(string)*
    - Specifies delivery terms. Refer to Help -> Code lists in your account for available delivery terms.
- **termsLocation** *(string)*
    - Defines the location where takeover for the specified delivery term is done.
- **termsLocationIdentifier** *(string)*
    - Defines the location identifier where takeover for the specified delivery term is done.
- **shipDate** *(string)*
    - Sets the shipdate and delays EDI transfer until this date. Supplied as YYYY-MM-DD. Default: Current/shipment creation date.
- **pickupTime** *(string)*
    - Desired pickup time. Supplied as HH:MM.
- **deliveryDate** *(string)*
    - Desired delivery date. Supplied as YYYY-MM-DD.
- **deliveryTimeEarliest** *(string)*
    - Desired earliest delivery time. Supplied as HH:MM.
- **deliveryTimeLastest** *(string)*
    - Desired latest delivery time. Supplied as HH:MM.
- **shipmentNo** *(string)*
    - Shipment ID. Used only if instructed by carrier.
- **ediForward** *(boolean)*
    - Specifies whether electronic pre-advice (EDI) should be sent to carrier.
- **tplFormat** *(boolean)*
    - Feature used by third party logistics companies. Switches sender's and dispatch address on label.
- **pdfInsert** *(string)*
    - Specifies PDF filename that is to be used for OneDoc (Integrated Document) feature.
- **deliveryInstruction** *(string)*
    - Delivery instuction field used by certain services.
- **customLabelText1** *(string)*
    - Custom label text field. Used only for customer specific layouts.
- **customLabelText2** *(string)*
    - Custom label text field. Used only for customer specific layouts.
- **customLabelText3** *(string)*
    - Custom label text field. Used only for customer specific layouts.
- **customLabelText4** *(string)*
    - Custom label text field. Used only for customer specific layouts.
- **customLabelText5** *(string)*
    - Custom label text field. Used only for customer specific layouts.
- **customLabelText6** *(string)*
    - Custom label text field. Used only for customer specific layouts.

## Shipment - Close
Used only to close consolidated shipments.

- **mergeId** *(string)*
    - Corresponds to specified mergeId for shipment.

## Shipment - Printset
The printSet array specifies what documents should be printed, if applicable. By default, all necessary shipment documents are printed, printSet array is used only if certain documents are not desired. An exception to this is the printSet array under Customs declaration object where it is required to specify what kind of customs declaration documents are requested.

- Available options shipping documents:
    - **label** (parcel labels)
    - **dngdecl** (dangerous goods declaration)
    - **sis** (SIS/SFS/CMR waybill. Actual printed type depends on sender and receiver country.)
    - **\*** (None)
 
- Available options customs declaration documents:
    - **proforma** (Commercial/proforma invoice)
    - **proformaplabedi** (Proforma invoice incl. EDI - PostNord only)
    - **plabedi** (Customs information via EDI only - PostNord only)
    - **edoc** (ED-document)
    - **cn22** (CN22)
    - **cn23** (CN23)
    - **proformaups** (Commercial invoice - UPS)
    - **upsedi** (Paperless invoice - UPS)
    - **upschild** (UPS World Ease Child shipment)
    - **proformatnt** (Proforma for TNT)
    - **notetnt** (TNT Note)
    - **pnlwaybilledi** (Separate custom docs for PNL are sent via EDI, not from this system)
    - **fedexp** (commercial invoice for FedEx)
    - **fedexe** (Electronic trade documents - ETD, for FedEx)


## Shipment - Service
- **id** *(string)*
    - Desired carrier service. Refer to Help -> Code lists in your account for available services.
- **subId** *(string)* 
    - Used with Neutral carrier feature and defines the custom specified neutral carrier's ID.
- **normalShipment** *(boolean)* 
    - Specifies wheteher the shipment is an outbound shipment.
- **returnShipment** *(boolean)* 
    - Specifies whether the shipment is a return shipment.
- **referenceAsBarcode** *(boolean)* 
    - Prints reference value as barcode on label. Used only for certain services.
- **nonDeliveryType** *(string)* 
    - Instrucion to carrier in case the shipment is not delivarable. Used only for certain services. Available options: **return**, **abandon**.
- **valueAmount** *(string)*
    - Specifies shipment's value. Used only for certain services.
- **valueCurrencyCode** *(string)* 
    - Specifies shipment's value currency. Used only for certain services.
- **paymentMethodType** *(string)* 
    - Payment method. Used only for certain services. Available options: **invo** (credit without delivery note), **invodn** (credit with delivery note) and **metered** (domestic franking).
- **sortPos** *(string)* 
    - Sorting position, if provided by carrier.
- **destinationLocation** *(string)* 
    - Destination location, if provided by carrier.
- **notifyCode1** *(string)* 
    - Not used.
- **notifyCode2** *(string)* 
    - Not used.
- **notifyCode3** *(string)* 
    - Not used.
- **bookingId** *(string)* 
    - Booking ID, if provided by carrier.
- **bookingOffice** *(string)* 
    - Booking office, if provided by carrier.
- **infoCode** *(string)* 
    - Info code, if provided by carrier.
- **contractVersion** *(string)* 
    - Contract version, if provided by carrier.
- **terminal** *(string)* 
    - Destination terminal, if provided by carrier.
- **handOverCode** *(string)* 
    - Handover code, if provided by carrier.
- **externalIdentifier** *(string)* 
    - External identifier, if provided by carrier.
- **waybillInvoice** *(integer, minimum 0)* 
    - Waybill invoice.
- **waybillEurCertificate** *(integer, minimum 0)* 
    - Waybill EUR certificate.
- **waybillExportNotification** *(integer, minimum 0)* 
    - Waybill export notification.
- **waybillUnits332** *(integer, minimum 0)* 
    - Number of 332 units on waybill.
- **waybillWeight332** *(number, minimum 0)* 
    - Weight of 332 units on waybill.
- **waybillUnits334** *(integer, minimum 0)* 
    - Number of 334 units on waybill-
- **waybillWeight334** *(number, minimum 0)* 
    - Weight of 334 units on waybill.
- **waybillUnits336** *(integer, minimum 0)* 
    - Number of 336 units on waybill.
- **waybillWeight336** **(number, minimum 0)* 
    - Weight of 336 units on waybill.
- **waybillUnits342** *(integer, minimum 0)* 
    - Number of 342 units on waybill.
- **waybillWeight342** *(number, minimum 0)* 
    - Weight of 342 units on waybill.
- **waybillCod** *(integer, minimum 0)*  
    - Cash on delivery amount on waybill.
- **waybillCod342** *(integer, minimum 0)*
    - Cash on delivery amount for 342 on waybill.
- **waybillHomeDelivery342** *(integer, minimum 0)* 
    - Number of Home Delivery 342 units on waybill.
- **shipperLoadAndCount** *(integer, minimum 0)* 
    - Shipper load an count.
- **pickupBooking** *(boolean)* 
    - Request pickup.
- **pickupDate** *(string)* 
    - Pickup date. Supplied as YYYY-MM-DD.
- **pickupTimeFrom** *(string)* 
    - Earliest pickup time. Supplied as HH:MM.
- **pickupTimeTo** *(string)* 
    - Latest pickup time. Supplied as HH:MM.
- **pickupText1** *(string)* 
    - Custom pickup instruction.
- **pickupMisc** *(string)* 
    - Miscellaneous pickup instruction.


## Shipment - Addons
- **id** *(string)* 
    - Desired additional service. Refer to Help -> Code lists in your account for available additional services.
- **amount** *(number, minimum 0)*
    - Amount used for cash on delivery shipments.
- **account** *(string)* 
    - Account used for cash on delivery shipments.
- **accountType** *(string)* 
    - Account type used for cash on delivery shipments. Refer to Help -> Code lists in your account for available account types.
- **bank** *(string)* 
    - Bank, used for cash on delivery shipments.
- **currencyCode** *(string)* 
    - Currency code, used for cash on delivery shipments.
- **custNo** *(string)* 
    - Customer/contract number. Used for Receiver pays and Other payer addons.
- **custNoIssuerCode** *(string)* 
    - Customer/contract number issuer code. Used for Receiver pays and Other payer addons.
- **misc** *(string)* 
    - Miscellaneous value used by various addons. Refer to Help -> Code lists in your account for more information.
- **miscType** *(string)* 
    - Type of miscellaneous value. Refer to Help -> Code lists in your account for available types.
- **contact** *(string)* 
    - Contact person.
- **reference** *(string)* 
    - Reference.
- **referenceType** *(string)* 
    - Reference type.  Available options: **txt**, **ocr**. The OCR type has checkdigit calculation.
- **tempMin** *(number)* 
    - Minimum tempetarure, used for certain addons. Refer to Help -> Code lists in your account for more information.
- **tempMax** *(number)* 
    - Maximum temperature, used for certain addons. Refer to Help -> Code lists in your account for more information.
- **email** *(string)* 
    - E-mail.
- **text1** *(string)* 
    - Usage varies, depending on addon. Refer to Help -> Code lists in your account for more information.
- **text2** *(string)* 
    - Usage varies, depending on addon. Refer to Help -> Code lists in your account for more information.
- **text3** *(string)* 
    - Usage varies, depending on addon. Refer to Help -> Code lists in your account for more information.
- **text4** *(string)* 
    - Usage varies, depending on addon. Refer to Help -> Code lists in your account for more information.
- **text5** *(string)* 
    - Usage varies, depending on addon. Refer to Help -> Code lists in your account for more information.
- **text6** *(string)* 
    - Usage varies, depending on addon. Refer to Help -> Code lists in your account for more information.
- **text7** *(string)* 
    - Usage varies, depending on addon. Refer to Help -> Code lists in your account for more information.
- **text8** *(string)* 
    - Usage varies, depending on addon. Refer to Help -> Code lists in your account for more information.
- **text9** *(string)* 
    - Usage varies, depending on addon. Refer to Help -> Code lists in your account for more information.
- **text10** *(string)* 
    - Usage varies, depending on addon. Refer to Help -> Code lists in your account for more information.
- **length** *(number, minimum 0)* 
    - Length, used for certain addons. Refer to Help -> Code lists in your account for more information.
- **width** *(number, minimum 0)* 
    - Width, used for certain addons. Refer to Help -> Code lists in your account for more information.
- **declarant** *(string)* 
    - Declarant, used for certain addons. Refer to Help -> Code lists in your account for more information.
- **passengerFlight** *(boolean)* 
    - Passenger flight, used for certain addons. Refer to Help -> Code lists in your account for more information.
- **cargoFlight** *(boolean)* 
    - Cargo flight, used for certain addons. Refer to Help -> Code lists in your account for more information.
- **documentType** *(string)*
    - Document type, used for certain addons. Refer to Help -> Code lists in your account for more information.


## Shipment - Parcels
- **valuePerParcel** *(boolean)*
    - **true** defines information for each parcel individually.
    - **false** defines information for an entire row of parcels.
- **copies** *(integer, minimum 1)*
    - Number of parcels.
- **marking** *(string)*
    - Goods marking.
- **packageCode** *(string)*
    - Package code. Refer to Help -> Code lists in your account for available package types.
- **packageText** *(string)*
    - Package text. Used for certain services.
- **weight** *(number, minimum 0)*
    - Weight.
- **volume** *(number, minimum 0)*
    - Volume.
- **length** *(number, minimum 0)*
    - Length.
- **width** *(number, minimum 0)*
    - Width.
- **height** *(number, minimum 0)*
    - Height.
- **loadingMeters** *(number, minimum 0)*
    - Load meters.
- **itemNo** *(string)*
    - Item number. Used for certain services.
- **contents** *(string)*
    - Contents.
- **reference** *(string)*
    - Parcel reference.
- **parcelNos** *(array of string)*
    - Parcel numbers. The array should have *copies* number of parcel numbers. *Note:* A special license key is required to use this value.


## Shipment - Parcels - Dangerous goods
- **unCode** *(string)*
    - UN code.
- **hazardCode** *(string)*
    - Hazard class/Sub label number.
- **packageCode** *(string)*
    - Package code.
- **packageType** *(string)*
    - Package type.
- **description** *(string)*
    - Description.
- **adrClass** *(string)*
    - ADR class.
- **mpCode** *(string)*
    - MP code.
- **ems** *(string)*
    - EmS.
- **note** *(string)*
    - Note.
- **netWeight** *(number)*
    - Net weight.
- **netVolume** *(number)*
    - Net volume.
- **trCode** *(string)*
    - Tunnel restriction code.
- **flashPoint** *(string)*
    - Flash point.
- **limitedQuantities** *(boolean)*
    - Limited quantities.
- **separation** *(string)*
    - Separation.
- **technicalDescr** *(string)*
    - Technical description
- **quantity** *(integer, minimum: 0)*
    - Quantity of package type


## Shipment - Parcels - Article
- **articleNo** *(string)*
    - Article number.
- **count** *(integer)*
    - Count.
- **name** *(string)*
    - Name.
- **enot** *(boolean)*
    - Display in pre-notification message.
- **price** *(number, minimum 0)*
    - Price.
- **currencyCode** *(string)*
    - Currency code.
- **weight** *(number, minimum 0)*
    - Weight.
- **volume** *(number, minimum 0)*
    - Volume.
- **loadingMeters** *(number, minimum 0)*
    - Load meters.
- **contents** *(string)*
    - Contents.
- **marking** *(string)*
    - Marking.
- **packageCode** *(string)*
    - Package code. Refer to Help -> Code lists in your account for available package types.
- **customsStatNo** *(string)*
    - Customs: HS Tariff Code (stat no).
- **customsSubStatNo1** *(string)*
    - Customs: Additional codes, substatno.
- **customsOtherUnit** *(string)*
    - Customs: Other unit.
- **customsOtherQuantity** *(number, minimum 0)*
    - Customs: Other quantity.
- **customsValue** *(number, minimum 0)*
    - Customs: Value.
- **customsContents** *(string)*
    - Customs: Contents.
- **customsNetWeight** *(number, minimum 0)*
    - Customs: Net weight.
- **customsSourceCountryCode** *(string)*
    - Customs: Source country code.


## Shipment - Customs declaration

- **parcelCount** *(integer, minimum 0)*
    - Parcel count.
- **reference** *(string)*
    - Reference.
- **sourceCountryCode** *(string)*
    - Source country code.
- **destinationCountryCode** *(string)*
    - Destination country code.
- **shippingCodeBorder** *(string)*
    - Means of transport (at the border). Available options: **sea**, **rail**, **road**, **air**, **post**, **fixed** (Fixed transport), **water** (Water transport on inner waterways), **own** (Own propulsion).
- **shippingCodeDomestic** *(string)*
    - Means of transport (domestic). Available options: **sea**, **rail**, **road**, **air**, **post**, **fixed** (Fixed transport), **water** (Water transport on inner waterways), **own** (Own propulsion).
- **finance1** *(string)*
    - Financial information.
- **finance2** *(string)*
    - Financial information.
- **declarantCity** *(string)*
    - Declarant city.
- **declarantDate** *(string)*
    - Declarant date.
- **declarant** *(string)*
    - Declarant.
- **jobTitle** *(string)*
    - Declarant job title.
- **edocNormal** *(boolean)*
    - Available options: **yes** (Export, normal procedure), **no** (Export, commercial item list attached).
- **representative1** *(string)*
    - Declarant's/agent's representative 1.
- **representative2** *(string)*
    - Declarant's/agent's representative 2.
- **representativeOrgNo** *(string)*
    - Declarant's/agent's organization number.
- **invoiceType** *(string)*
    - Invoice type. Available options: **proforma** (proforma invoice), **standard** (commercial invoice). 
- **invoiceNo** *(string)*
    - Invoice number.
- **discount** *(number)*
    - Discount that is automatically subtracted from other amounts. Should be a negative value.
- **freightCharges** *(number, minimum 0)*
    - Freight charges.
- **insuranceCharges** *(number, minimum 0)*
    - Insurance charges.
- **otherCharges** *(number, minimum 0)*
    - Other charges.
- **exportLicenseNo** *(string)*
    - Export license number.
- **exportDeclaration1** *(string)*
    - Default value: "I declare that of the best of my knowledge the information on this invoice is".
- **exportDeclaration2** *(string)*
    - Default value: "true and correct.".
- **generalNote1** *(string)*
    - General description of the contents, for customs.
- **generalNote2** *(string)*
    - General description of the contents, for customs.
- **generalNote3** *(string)*
    - General description of the contents, for customs.
- **generalNote4** *(string)*
    - General description of the contents, for customs.
- **currencyCode** *(string)*
    - Currency code.
- **importExportType** *(string)*
    - Import/export type. Available options: **temporary**, **reexport**, **gift**, **documents**, **sample**, **return**, **other** (requires the explanation value), **permanent**, **internal**.
- **invoiceDeclaration1** *(string)*
    - Default value: "The exporter of the products covered by this document declares that, except".
- **invoiceDeclaration2** *(string)*
    - Default value: "where otherwise clearly indicated, these products are of EU preferential origin.".
- **importLicenseNo** *(string)*
    - Import license number.
- **certificate** *(string)*
    - Certificate.
- **explanation** *(string)*
    - Explanation, only if *importExportType* is set to **other**.
- **termCode** *(string)*
    - Delivery terms.
- **termLocation** *(string)*
    - Defines the place where goods are taken over according to set delivery terms.


## Shipment - Customs declaration - Lines
- **valuesPerItem** *(boolean)*
    - Specifies if values provided apply per item or in total.
- **statNo** *(string)*
    - HS Tariff Code (stat no).
- **subStatNo1** *(string)*
    - Additional codes, substatno.
- **subStatNo2** *(string)*
    - Additional codes, substatno.
- **procedure** *(string)*
    - Procedure.
- **value** *(number)*
    - Customs value.
- **goodsMark1** *(string)*
    - Goods marking.
- **goodsMark2** *(string)*
    - Goods marking.
- **goodsMark3** *(string)*
    - Goods marking.
- **goodsMark4** *(string)*
    - Goods marking.
- **goodsMark5** *(string)*
    - Goods marking.
- **goodsMark6** *(string)*
    - Goods marking.
- **contents** *(string)*
    - Contents.
- **copies** *(integer, minimum 1)*
    - Copies.
- **netWeight** *(number, minimum 0)*
    - Net weight.
- **sourceCountryCode** *(string)*
    - Source country code.
- **otherUnit** *(string)*
    - Other unit. Available options: **gram**, **m2** (meters squared), **liter**, **pair**, **piece**.
- **otherQuantity** *(number, minimum 0)*
    - Quantity of *other unit*.


## Shipment - Options
Options are carrier-neutral additional services provided by Unifaun.

**Properties**
- **id** *(string)*
    - Available options:
         - **prenot** (Pre-notification e-mail)
         - **lnkprtn** (Link to Print, normal)
         - **lnkprtr** (Link to Print, return)
         - **consolidation** (Consolidation)
- **from** *(string)*
    - E-mail: Reply-to address.
- **to** *(string)*
    - E-mail: Receiver.
- **cc** *(string)*
    - E-mail: Carbon copy.
- **bcc** *(string)*
    - E-mail: Blind carbon copy.
- **errorTo** *(string)*
    - E-mail: Error message receiver.
- **message** *(string)*
    - Message in pre-notification e-mail and Link to Print.
- **languageCode** *(string)*
    - Language code for pre-notification e-mail and Link to Print. Available options: **se** (Swedish), **en** (English), **dk** (Danish), **fi** (Finnish).
- **sendEmail** *(boolean)*
    - Send Link to Print e-mail message.

## Shipment - PDF Config
Media availability depends on carrier service. Following media types are available:
- **laser-a5** (Single A5 label on A4 paper)
- **laser-2a5** (Two A5 labels on A4 paper)
- **laser-ste** (Two STE labels (107x251 mm) on A4 paper)
- **laser-a4** (Normal A4 used for waybills, customs declaration documents etc.)
- **thermo-se** (107 x 251 mm thermo STE label)
- **thermo-190** (107 x 190 mm thermo label)
- **thermo-brev3** (107 x 72 mm thermo label)

Four target medias can be specified. Target offset is used to adjust label positioning on paper to compensate for printer margins.

# Response
Schema for response messages is similar for POST and GET. GET returns an array.

- **href** *(string)* 
    - URL to object.
- **id** *(string)* 
    - Shipment ID in database.
- **status** *(string)* 
    - Statuses returned by /shipments:
	    - **printed** (Shipment is printed. Intial status).
		- **delivering** (Shipment has arrived to a pickup location).
		- **dispatching** (Shipment is en route).
		- **outfordelivery** (Shipment is loaded on truck, en route to final destination).
		- **delivered** (Shipment has been delivered).
		- **partdelivered** (Shipment has been partly delivered).
		- **cancelled** (Shipment is cancelled).
		- **returned** (Shipment is returned to sender).
	- Statuses returned by /stored-shipments and /consolidated-shipments
	    - **invalid** (Shipment is invalid, data incorrect or missing).
		- **warned** (Shipment has an error that can be fixed or ignored).
		- **ready** (Shipment is ready for printing).
		- **failed** (Shipment has failed, view shipment details for more information).
		- **printed** (Shipment has been printed).
		- **open** (Shipment has the status Open, returned only by /consolidated-shipments).
- **orderNo** *(string)* 
    - Order number.
- **reference** *(string)* 
    - Reference.
- **serviceId** *(string)* 
    - Service ID.
- **parcelCount** *(integer)* 
    - Parcel count.
- **sndName** *(string)* 
    - Sender's name.
- **sndZipcode** *(string)* 
    - Sender's zip code.
- **sndCity** *(string)* 
    - Sender's city.
- **sndCountry** *(string)* 
    - Sender's country.
- **rcvName** *(string)* 
    - Receiver's name.
- **rcvZipcode** *(string)* 
    - Receiver's zip code.
- **rcvCity** *(string)* 
    - Receiver's city.
- **rcvCountry** *(string)* 
    - Receiver's country.
- **created** *(string, format: date-time)*
    - Created date- and timestamp.
- **changed** *(string, format: date-time)* 
    - Changed date- and timestamp.
- **shipDate** *(string, format: date-time)* 
    - Shipping date.
- **returnShipment** *(boolean)* 
    - Return shipment.
- **normalShipment** *(boolean)* 
    - Normal shipment.
- **consolidated** *(boolean)*
    - Returned only by /consolidated-shipments method.

**Parcels**
Returned only for /consolidated-shipments and /shipments methods.
- **parcelNo** *(string)*
    - Assigned parcel number.
- **reference** *(string)*
    - Parcel reference.

**PDFs**
Returned only for /consolidated-shipments and /shipments methods.
- **href** *(string)*
    - URL to PDF file.
- **id** *(string)*
    - Database ID of PDF file.
- **description** *(string)*
    - Description of returned document.

**PreviousPDFs**
Returned only for /consolidated-shipments and /shipments methods. Contains information about already created PDF documents for current shipment.
- **href** *(string)*
    - URL to PDF file.
- **id** *(string)*
    - Database ID of PDF file.
- **description** *(string)*
    - Description of returned document.

**Statuses**
- **type** *(string)*
    - Status type. Can be **ignorable** or **critical**.
- **field** *(string)* 
    - Specifies the field where the error is found.
- **location** *(string)* 
    - Specifies the location where the error is found.
- **messageCode** *(string)* 
    - System message code.
- **message** *(string)*
    - System message.

### Response - GET pdfs methods
Response to /consolidated-shipments/{consolidatedId}/pdfs and /shipments/{shipmentId}/pdfs GET methods.
- **href** *(string)*
    - URL to PDF file.
- **id** *(string)*
    - Database ID of PDF file.
- **description** *(string)*
    - Description of returned document.
- **pdf** *(string)*
    - Base64 encoded PDF. Requires that **inlinePdf** is set to **TRUE** in the request.
