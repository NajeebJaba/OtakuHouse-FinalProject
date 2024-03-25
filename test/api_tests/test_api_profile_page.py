import unittest
from infra.api_infra.api_browser_wrapper import APIBrowserWrapper
from logic.api_logic.api_profile_page import APIProfilePage

class TestAPIProfilePage(unittest.TestCase):
    def setUp(self):
        self.api_browser_wrapper = APIBrowserWrapper()
        self.profile_page = APIProfilePage(self.api_browser_wrapper)

    def test_update_profile(self):
        user_id = 24
        profile_data = {
            "name_for_profile": "najeeeeeb",
            "email_for_profile": "jabanaj33@gmail.com",
            "password_for_profile": "112233",
            "confirm_password_for_profile": "112233"
        }
        headers = {
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzOTEzMzgyLCJqdGkiOiIyNDIzNzg5Y2E2NWE0ODVlYTJhNGI0MWUxN2UwOWI5NSIsInVzZXJfaWQiOjh9.HBTVOkFtSK9wsAKcGbEl-YeRMCswsouwlb9aQusbBlY"
        }
        response = self.profile_page.update_profile(user_id, profile_data, headers)
        self.assertTrue(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()