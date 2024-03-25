import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from infra.ui_infra.browser_wrapper import BrowserWrapper
from logic.ui_logic.base_page.home_page import HomePage
from logic.ui_logic.login_page import LoginPage
from infra.ui_infra.config_handler import ConfigHandler


class TestProductPageToSeeReview(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = ConfigHandler().config
        cls.browser_wrapper = BrowserWrapper()
        cls.driver = cls.browser_wrapper.initialize_driver()
        cls.home_page = HomePage(cls.driver)
        cls.login_page = LoginPage(cls.driver)

    def setUp(self):
        self.home_page.navigate_to(self.config["url"])

    def test_review_display_on_product_page(self):
        # from home page click login and navigate to login page
        self.home_page.click_on_sign_in_link()
        time.sleep(2)

        self.login_page.enter_username(self.config["email"])
        self.login_page.enter_password_and_login(self.config["password"])
        time.sleep(3)

        self.home_page.navigate_to(self.config["url"])
        time.sleep(2)

        # search for a product
        search_input = self.driver.find_element(By.XPATH, "//input[@name='q']")
        search_input.send_keys(self.config["search_product"])
        search_input.send_keys(Keys.ENTER)
        time.sleep(3)

        first_product_link = self.driver.find_element(By.XPATH, "//a[contains(@href, '/product/')]")
        first_product_link.click()
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
