from infra.api_infra.api_wrapper import APIWrapper


class APIBrowserWrapper(APIWrapper):
    def __init__(self):
        super().__init__()


    def post(self, endpoint, json_data):
        full_url = f"{self.url.strip('/')}/{endpoint.lstrip('/')}"
        self.response = self.request.post(full_url, json=json_data)
        return self.response

    def get(self, endpoint, headers=None):
        headers = headers or {}
        full_url = f"{self.url.rstrip('/')}/{endpoint.lstrip('/')}"
        return self.request.get(full_url, headers=headers)


    #i used put for profile , it's return PUT when fill the form
    def put(self, endpoint, json_data, headers=None):
        headers = headers or {'Content-Type': 'application/json'}
        full_url = f"{self.url.strip('/')}/{endpoint.lstrip('/')}"
        self.response = self.request.put(full_url, json=json_data, headers=headers)
        return self.response

    def post(self, endpoint, json_data, headers=None):
        headers = headers or {'Content-Type': 'application/json'}
        full_url = f"{self.url.strip('/')}/{endpoint.lstrip('/')}"
        self.response = self.request.post(full_url, json=json_data, headers=headers)
        return self.response