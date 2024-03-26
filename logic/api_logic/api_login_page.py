from infra.api_infra.api_wrapper import APIWrapper


class LoginAPI(APIWrapper):
    def __init__(self):
        super().__init__()
        self.json = None

    def login_with_credentials(self, email, password):
        self.json = {
            "username": email,
            "password": password
        }

        print(f"Attempting to login with email: {email}")
        self.response = self.request.post(f'{self.url[:-2]}api/users/login/', json=self.json)

        if self.response.ok:
            print("Login successful")
        else:
            print(f"Login failed with status code: {self.response.status_code}")
            print(f"Response: {self.response.json()}")

        return self.response
