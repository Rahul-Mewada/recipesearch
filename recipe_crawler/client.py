import requests

class Client:
    def __init__(self, endpoint):
        self.endpoint = endpoint
    
    def get(self, endpoint):
        response = requests.get(endpoint)
        return response

    def post(self, json):
        response = requests.post(self.endpoint, json=json)
        return response
