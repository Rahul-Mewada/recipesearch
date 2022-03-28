from pprint import pprint
import requests
from utils import crc_hash
from models import recipe
import json
from pprint import pprint

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
        try:
            response = requests.get(endpoint, json=url_data)
        except:
            print("Could not establish connection")

        return response.status_code == 200

    def add_recipe(self, recipe:recipe.Recipe):
        """
        Takes a recipe with an unvisited url and sends a post request
        to the recipe api
        """
        endpoint = self.base_endpoint + self.paths['add_recipe']
        response = requests.post(endpoint, json=recipe.to_json())

        print()
        pprint(recipe.to_json())
        print(response.status_code)
        print()

        return response.status_code