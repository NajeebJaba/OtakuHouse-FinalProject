import json
from os.path import dirname, join

class APIConfigHandler:
    def read_config_data(self, file="api_config.json"):
        here = dirname(__file__)
        filename = join(here, file)
        with open(filename, 'r') as file:
            config = json.load(file)
            return config
