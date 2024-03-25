import unittest
from infra.ui_infra.browser_wrapper import BrowserWrapper
from logic.ui_logic.base_page.home_page import HomePage
from logic.ui_logic.login_page import LoginPage
from logic.ui_logic.register_page import RegisterPage
from infra.ui_infra.config_handler import ConfigHandler
import time

class TestRegisterPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = ConfigHandler().config
        cls.browser_wrapper = BrowserWrapper()
        cls.driver = cls.browser_wrapper.initialize_driver()
        cls.home_page = HomePage(cls.driver)
        cls.login_page = LoginPage(cls.driver)
        cls.register_page = RegisterPage(cls.driver)

    def setUp(self):
        self.driver.get(self.config['url'])
        self.home_page.click_on_sign_in_link()
        time.sleep(1)  # Adjust based on your application's response time

    def test_register_with_correct_data(self):
        # Navigate to the registration page
        self.login_page.click_register()
        self.register_page.fill_registration_form(
            name=self.config["name_for_register"],
            email=self.config["email_for_register"],
            password=self.config["password_for_register"],
            confirm_password=self.config["password_for_register"]
        )
        self.register_page.submit_registration()
        # Additional assertions to verify successful registration can be included here

    def test_register_with_incorrect_data(self):
        # Navigate to the registration page
        self.login_page.click_register()
        self.register_page.fill_registration_form(
            name=self.config["name_for_register"],
            email=self.config["incorrect_email_for_register"],
            password=self.config["incorrect_password_for_register"],
            confirm_password=self.config["incorrect_password_for_register"]
        )
        self.register_page.submit_registration()
        # Additional assertions to verify handling of incorrect data can be included here

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
