import requests

BASE_URI = 'https://api.unifaun.com/rs-extapi/v1'

class BaseClient(object):

    def __init__(self, base_uri=BASE_URI, user=None, password=None):
        self.base_uri = base_uri
        self.session = requests.Session()
        if user and password:
            self.session.auth = (user, password)

    def _get(self, url, **kwargs):
        return self.session.get(self.base_uri + url, **kwargs).json()

    def _post(self, url, data=None, json=None, **kwargs):
        return self.session.post(self.base_uri + url, data=data, json=json, **kwargs).json()

class UnifaunClient(BaseClient):
    '''Unifaun-specific logic'''

    def get_agents(self, type, zip, countryCode, street=''):
        query_parameters = {
            'type': type,
            'zip': zip,
            'street': street,
            'countryCode': countryCode,
        }
        return self._get('/addresses/agents', params=query_parameters)

    def create_address_validation_status(self):
        '''post /addresses/status'''
        raise NotImplemented

    def get_zipcode_info(self, zip, countryCode):
        query_parameters = {
            'zip': zip,
            'countryCode': countryCode,
        }
        return self._get('/addresses/zipcodes', params=query_parameters)

    def get_stored_shipments(self):
        '''get /stored-shipments'''
        raise NotImplemented

    def create_stored_shipment(self):
        '''post /stored-shipments'''
        raise NotImplemented

    def delete_stored_shipment(self):
        '''delete /stored-shipments/{storedId}'''
        raise NotImplemented

    def create_shipment_from_stored(self):
        '''post /stored-shipments/{storedId}/shipments'''
        raise NotImplemented

    def get_consolidated_shipments(self):
        '''get /consolidated-shipments'''
        raise NotImplemented

    def create_consolidated_shipment(self):
        '''post /consolidated-shipments'''
        raise NotImplemented

    def delete_consolidated_shipment(self):
        '''delete /consolidated-shipments/{consolidatedId}'''
        raise NotImplemented

    def get_consolidated_shipment_pdfs(self):
        '''get /consolidated-shipments/{consolidatedId}/pdfs'''
        raise NotImplemented

    def get_consolidated_shipment_pdf(self):
        '''get /consolidated-shipments/{consolidatedId}/pdfs/{pdfId}'''
        raise NotImplemented

    def add_to_consolidated_shipments(self):
        '''post /consolidated-shipments/{consolidatedId}/shipments'''
        raise NotImplemented

    def get_shipments(self):
        '''get /shipments'''
        raise NotImplemented

    def create_shipment(self, pdfConfig, shipment):
        json = {
            'pdfConfig': pdfConfig,
            'shipment': shipment,
        }
        return self._post('/shipments', json=json)

    def delete_shipment(self):
        '''delete /shipments/{shipmentId}'''
        raise NotImplemented

    def get_shipment_pdfs(self):
        '''get /shipments/{shipmentId}/pdfs'''
        raise NotImplemented

    def get_shipment_pdf(self):
        '''get /shipments/{shipmentId}/pdfs/{pdfId}'''
        raise NotImplemented
