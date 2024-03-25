from infra.api_infra.api_wrapper import APIWrapper


class RegisterAPI(APIWrapper):
    def __init__(self):
        super().__init__()

    def register_user(self, name, email, password):
        registration_payload = {"name": name, "email": email, "password": password}
        self.response = self.request.post(f'{self.url[:-2]}api/users/register/', json=registration_payload)
        return self.response.status_code
