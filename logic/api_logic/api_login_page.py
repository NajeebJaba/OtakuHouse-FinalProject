from infra.api_infra.api_wrapper import APIWrapper


class LoginAPI(APIWrapper):
    def __init__(self):
        super().__init__()

    def login_user(self, email, password):
        login_payload = {"email": email, "password": password}
        self.response = self.request.post(f'{self.url[:-2]}api/users/login/', json=login_payload)
        return self.response.status_code
