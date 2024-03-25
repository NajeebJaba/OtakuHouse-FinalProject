import json
import os


class APIHandler:
    def __init__(self, config_path=None):
        self.config_path = config_path or 'api_config.json'

    def read_config_data(self):
        if not os.path.isabs(self.config_path):
            base_path = os.path.dirname(__file__)
            self.config_path = os.path.join(base_path, self.config_path)
        with open(self.config_path, 'r') as file:
            config_data = json.load(file)
        return config_data




