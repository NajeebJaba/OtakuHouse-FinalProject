from infra.api_infra.api_browser_wrapper import APIBrowserWrapper

class LoginPage:
    def __init__(self):
        self.browser_wrapper = APIBrowserWrapper()

    def login_page(self, email, password):
        json_data = {"username": email, "password": password}
        response = self.browser_wrapper.post('api/users/login/', json_data)
        return response.status_code

