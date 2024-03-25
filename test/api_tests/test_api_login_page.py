import unittest
from logic.api_logic.api_login_page import LoginPage


class TestAPILoginPage(unittest.TestCase):
    def setUp(self):
        self.login_page = LoginPage()
        self.email = "jabnaj33@gmail.com"
        self.password = "123456"
        self.invalid_email = "wrongemail@gmail.com"
        self.invalid_password = "wrongpassword"

    def test_login_with_valid_credentials(self):
        response = self.login_page.login_page(self.email, self.password)
        self.assertEqual(response, 200)

    def test_login_with_invalid_credentials(self):
        response = self.login_page.login_page(self.invalid_email, self.invalid_password)
        # Since it's an invalid login, we expect a status other than 200
        self.assertNotEqual(response, 200)


if __name__ == '__main__':
        unittest.main()


