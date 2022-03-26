from pprint import pprint
import requests
from utils import crc_hash

class Client:
    def __init__(self, base_endpoint):
        self.base_endpoint = base_endpoint
        self.paths = {
            'get_url' : 'urls/',
            'add_recipe': 'recipies/add'
        }

    def get(self, endpoint):
        response = requests.get(endpoint)
        return response

    def post(self, json):
        response = requests.post(self.endpoint, json=json)
        return response

    def is_visited(self, url):
        """
        Pings the database with the url data and returns true if the url
        exists in the Visited Url table
        """
        url_hash = crc_hash(url)
        url_data = {
            "url" : url,
            "url_hash": url_hash
        }
        endpoint = self.base_endpoint + self.paths['get_url']
        response = requests.get(endpoint, json=url_data)

        return response.status_code == 200
