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
            'add_recipe': 'recipies/add',
            'add_url': 'urls/create'
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
        print("GET request to urls")
        print(url)
        url_hash = crc_hash(url)
        url_data = {
            "url" : url,
            "url_hash": url_hash
        }
        endpoint = self.base_endpoint + self.paths['get_url']
        try:
            response = requests.get(endpoint, json=url_data)
            if response.status_code == 200:
                "Url already visited"
        except:
            print("Could not establish connection")
        
        return response.status_code == 200

    def add_url(self, url):
        """
        Called to explicitly add a url to the visitedurl table. Called when there is no 
        recipe returned from a url
        """
        print("Adding url")
        url_hash = crc_hash(url)
        url_data = {
            "url" : url,
            "url_hash" : url_hash
        }
        endpoint = self.base_endpoint + self.paths['add_url']
        response = requests.post(endpoint, json = url_data)
        return response.status_code

    def add_recipe(self, recipe:recipe.Recipe):
        """
        Takes a recipe with an unvisited url and sends a post request
        to the recipe api, adding a recipe and url 
        """
        print("POST request to recipies")
        endpoint = self.base_endpoint + self.paths['add_recipe']
        response = requests.post(endpoint, json=recipe.to_json())

        return response.status_code