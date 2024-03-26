import unittest
from logic.api_logic.api_login_page import LoginAPI


class TestLoginAPI(unittest.TestCase):

    def setUp(self):
        self.login_api = LoginAPI()

    def test_login_successful(self):
        response = self.login_api.login_with_credentials(self.login_api.UserEmail, self.login_api.UserPassword)

        self.assertEqual(response.status_code, 200)
        print("Test for successful login passed.")

    def test_login_unsuccessful(self):
        response = self.login_api.login_with_credentials("incorrect_email@example.com", "wrongpassword")

        self.assertNotEqual(response.status_code, 200)
        print("Test for unsuccessful login passed.")



if __name__ == '__main__':
    unittest.main()
