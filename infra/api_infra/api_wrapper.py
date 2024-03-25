import requests
from infra.api_infra.api_config_handler import APIHandler

class APIWrapper:
    def __init__(self, config_path='api_config.json'):
        self.response = None
        self.myHandler = APIHandler(config_path)
        self.config = self.myHandler.read_config_data()
        self.url = self.config['url']
        self.request = requests

    def get(self, endpoint, headers=None):
        headers = headers or {}
        self.response = self.request.get(f"{self.url}{endpoint}", headers=headers)
        return self.response

    def post(self, endpoint, data, headers=None):
        headers = headers or {'Content-Type': 'application/json'}
        self.response = self.request.post(f"{self.url}{endpoint}", json=data, headers=headers)
        return self.response
