# Introduction
Unifaun REST API is an integration service provided by Unifaun making it easy to integrate your cloud-based business system with your online account resulting in simpler dispatch processing, safer transactions and a significant time savings.

The service uses a REST API framework for communication with JSON as data carrier offering a number of functions and methods for storing shipments, generate freight documents and also supporting services for address lookup, available pickup-points and more.
The REST API endpoints are only accessible via HTTPS and are located at api.unifaun.com

    https://api.unifaun.com/rs-extapi/v1

# How it works
In order to use the resources a system needs to authenticate towards the API using basic authentication providing username and password. Read more in the Getting started section below. The REST API offers a number of resources with functions and methods that can be used to perform certain actions. Below is a short description of different resources and the authentication. For a more detailed technical documentation, please refer to each method's page on this site.

**/addresses**
- The Addresses resource can be used to validate receiver's address data and zipcode and also to provide choice of available pick-up points in order to display them to end user in a webshop or similar. These functions do not create shipments but can be used as utilities to make sure that shipments created are correct.

**/stored-shipments**
- These functions are used to create shipments that do not require immediate printing of freight documents. Shipments can be stored for later printing, either by the API or manually from system's interface.

**/consolidated-shipments**
- This resource is only used in conjuction with Consolidation option offered separately by Unifaun. Consolidation feature offers continuous printing of freight documents while holding the EDI message thus creating fewer shipments that can contain multiple orders and by that reducing shipping costs. The Consolidation feature is primarily available for freight services.

**/shipments**
- The shipments-resource offers the possibility of direct printing of shipment documents as PDF-file that is either provided as an URL or Base64 encoded file. Once created, PDF-files are available for 1 hour and can be fetched multiple times. This resource also has functions and methods for history followup and possibility of discarding shipments, i.e. preventing the sending of EDI message to carrier.

# Getting started
Before you can start using the Unifaun REST API you need to apply for it. Log in to your account and order Unifaun APIConnect from the webshop. Once approved, the agreement gives you access to the REST API framework and also includes customer support free of charge.

**Creating API-key**
Once you have the access to APIConnect in your account, a new menu will emerge under the Maintenance section called API-keys.
API-keys are used to authenticate towards different modules and functions provided by Unifaun where APIConnect is one of them. To create an API-key do following:

1. Click on New API Key button.
2. Leave the status on Enabled and make sure that Type checked is Web Services (REST).
3. Note. As you can create multiple API-keys, you might want to write a short note on this particular API-key and what it will be used for.
4. IP-address restriction can be set if desired so that this particular API-key only can be used from certain IP-addresses or ranges.
5. E-mail field is not in use at this time.
6. Developer-ID is the ID of the account using this key. Normally this would be your own account's user ID but in some cases you might have a ERP-system, webshop provider or some other third party that will post data into your account on your behalf. If this is the case, enter your provider's account user ID.


Once you click on Finish, the system will automatically generate the key consisting of an ID, secret ID and combined ID. It is values ID and secret ID that you need to use to authenticate towards the APIConnect framework. 

# Authentication
At the moment you can only use the Basic Authentication security scheme when you use the Try it feature on this site.
Use the Id part of your API-key as the Username and use the Secret Id as the Password. If you have a combined API-key (16 + 24 characters separated by a dash) use the first part of your API-key (everything up to but not including the dash) as the Username and use the second part (everything after the dash) as the Password.
