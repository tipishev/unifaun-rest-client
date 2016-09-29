import requests

BASE_URI = 'https://api.unifaun.com/ufoweb-prod-201609231347/rs-extapi/v1'


class Api(object):

    def __init__(self, base_uri=BASE_URI, user=None, password=None):
        self.base_uri = base_uri
        self.session = requests.Session()
        if user and password:
            self.session.auth = (user, password)

    def get_agents(self):
        '''get /addresses/agents'''

    def create_address_validation_status(self):
        '''post /addresses/status'''

    def get_zipcode_info(self):
        '''get /addresses/zipcodes'''

    def get_stored_shipments(self):
        '''get /stored-shipments'''

    def create_stored_shipment(self):
        '''post /stored-shipments'''

    def delete_stored_shipment(self):
        '''delete /stored-shipments/{storedId}'''

    def create_shipment_from_stored(self):
        '''post /stored-shipments/{storedId}/shipments'''

    def get_consolidated_shipments(self):
        '''get /consolidated-shipments'''

    def create_consolidated_shipment(self):
        '''post /consolidated-shipments'''

    def delete_consolidated_shipment(self):
        '''delete /consolidated-shipments/{consolidatedId}'''

    def get_consolidated_shipment_pdfs(self):
        '''get /consolidated-shipments/{consolidatedId}/pdfs'''

    def get_consolidated_shipment_pdf(self):
        '''get /consolidated-shipments/{consolidatedId}/pdfs/{pdfId}'''

    def add_to_consolidated_shipments(self):
        '''post /consolidated-shipments/{consolidatedId}/shipments'''

    def get_shipments(self):
        '''get /shipments'''

    def create_shipment(self):
        '''post /shipments'''

    def delete_shipment(self):
        '''delete /shipments/{shipmentId}'''

    def get_shipment_pdfs(self):
        '''get /shipments/{shipmentId}/pdfs'''

    def get_shipment_pdf(self):
        '''get /shipments/{shipmentId}/pdfs/{pdfId}'''
