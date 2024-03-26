import unittest
from infra.ui_infra.browser_wrapper import BrowserWrapper
from logic.ui_logic.base_page.home_page import HomePage
from logic.ui_logic.login_page import LoginPage
from logic.ui_logic.product_page import ProductPage
from infra.ui_infra.config_handler import ConfigHandler
import time

"""FOR REVIEW"""
class TestProductPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = ConfigHandler().config
        cls.browser_wrapper = BrowserWrapper()
        cls.driver = cls.browser_wrapper.initialize_driver()

    def setUp(self):
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.home_page.navigate_to(self.config["url"])
        self.login()

    def login(self):
        """method to encapsulate login steps"""
        self.home_page.click_on_sign_in_link()
        self.login_page.enter_username(self.config["email"])
        self.login_page.enter_password_and_login(self.config["password"])
        time.sleep(3)

    def test_interact_with_products(self):
        # interact with the first product
        self.home_page.click_product_1()
        self.product_page.update_quantity(2)
        self.product_page.select_review_rate("5")
        self.product_page.add_review_comment(self.config["review_comment_product_1"])
        self.product_page.submit_review()
        time.sleep(3)
        self.product_page.go_back()

        """"navigate back to the home page before interacting with the second product"""
        self.home_page.navigate_to(self.config["url"])
        self.home_page.click_product_2()
        self.product_page.update_quantity(5)
        time.sleep(3)
        self.product_page.select_review_rate("4")
        self.product_page.add_review_comment(self.config["review_comment_product_2"])
        self.product_page.submit_review()
        time.sleep(3)
        self.product_page.go_back()

        """need product 3 """

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
