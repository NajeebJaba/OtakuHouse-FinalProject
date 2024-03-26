import unittest
from infra.ui_infra.browser_wrapper import BrowserWrapper
from logic.ui_logic.base_page.home_page import HomePage
from logic.ui_logic.login_page import LoginPage
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

    def setUp(self):
        self.driver.get(self.config['url'])
        time.sleep(2)

    def test_navigate_to_profile_page(self):
        # click on login button
        self.home_page.click_on_sign_in_link()
        time.sleep(2)

        """login page"""
        # enter username and password then click signin
        self.login_page.enter_username(self.config["email"])
        self.login_page.enter_password_and_login(self.config["password"])
        time.sleep(3)

        # from home page click on the dropdown and then click on profile button
        self.home_page.click_profile_button()

        # in profile page, wait for 15 seconds and don't do anything
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
