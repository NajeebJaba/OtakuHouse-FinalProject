import unittest
from infra.ui_infra.browser_wrapper import BrowserWrapper
from logic.ui_logic.base_page.home_page import HomePage
from logic.ui_logic.login_page import LoginPage
from logic.ui_logic.register_page import RegisterPage
from logic.ui_logic.profile_page import ProfilePage
from infra.ui_infra.config_handler import ConfigHandler
import time


class TestProfilePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = ConfigHandler().config
        cls.browser_wrapper = BrowserWrapper()
        cls.driver = cls.browser_wrapper.initialize_driver()
        cls.home_page = HomePage(cls.driver)
        cls.login_page = LoginPage(cls.driver)
        cls.register_page = RegisterPage(cls.driver)
        cls.profile_page = ProfilePage(cls.driver)

    def setUp(self):
        self.driver.get(self.config['url'])
        self.home_page.click_on_sign_in_link()
        time.sleep(3)
        self.login_page.click_register()
        time.sleep(3)

    def test_profile_update(self):
        self.driver.get(self.config['url'])
        self.home_page.click_on_sign_in_link()
        time.sleep(3)

        self.login_page.click_register()
        time.sleep(3)

        self.register_page.fill_registration_form(
            name=self.config["register_name_for_profile"],
            email=self.config["register_email_for_profile"],
            password=self.config["register_password_for_profile"],
            confirm_password=self.config["register_confirm_password_for_profile"]
        )
        time.sleep(3)
        self.register_page.submit_registration()
        time.sleep(3)
        self.home_page.click_profile_button()
        time.sleep(3)
        self.profile_page.update_profile(
            self.config["updating_name_on_profile"],
            self.config["register_email_for_profile"],
            self.config["register_password_for_profile"],
            self.config["register_confirm_password_for_profile"]
        )
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
