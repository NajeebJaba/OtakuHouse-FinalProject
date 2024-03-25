import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.ui_infra.browser_wrapper import BrowserWrapper
from logic.ui_logic.base_page.home_page import HomePage
from logic.ui_logic.login_page import LoginPage
from infra.ui_infra.config_handler import ConfigHandler
import time


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config_handler = ConfigHandler()
        cls.config = cls.config_handler.config

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        self.driver = self.browser_wrapper.initialize_driver()
        self.driver.get(self.config['url'])

    def login(self, email, password):
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        wait = WebDriverWait(self.driver, 10)

        login_button = wait.until(EC.element_to_be_clickable(home_page.LOGIN_BUTTON))
        login_button.click()
        time.sleep(5)

        email_field = wait.until(EC.element_to_be_clickable(login_page.EMAIL))
        email_field.send_keys(email)
        time.sleep(2)

        password_field = wait.until(EC.element_to_be_clickable(login_page.PASSWORD))
        password_field.send_keys(password)
        time.sleep(3)

        sign_in_button = wait.until(EC.element_to_be_clickable(login_page.SIGNIN_BUTTON))
        sign_in_button.click()
        time.sleep(3)

    def test_login_first_user(self):
        self.login(self.config["email"], self.config["password"])

    def test_login_second_user(self):
        self.login(self.config["email_two"], self.config["password_two"])

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
