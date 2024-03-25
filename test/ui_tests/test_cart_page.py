import unittest
from infra.ui_infra.browser_wrapper import BrowserWrapper
from logic.ui_logic.base_page.home_page import HomePage
from logic.ui_logic.login_page import LoginPage
from logic.ui_logic.register_page import RegisterPage
from logic.ui_logic.search_product import SearchPage
from logic.ui_logic.cart_page import CartPage
from infra.ui_infra.config_handler import ConfigHandler
import time

class TestCartPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = ConfigHandler().config
        cls.browser_wrapper = BrowserWrapper()
        cls.driver = cls.browser_wrapper.initialize_driver()
        cls.home_page = HomePage(cls.driver)
        cls.login_page = LoginPage(cls.driver)
        cls.register_page = RegisterPage(cls.driver)
        cls.search_page = SearchPage(cls.driver)
        cls.cart_page = CartPage(cls.driver)

    def setUp(self):
        self.driver.get(self.config['url'])
        self.home_page.click_on_sign_in_link()
        time.sleep(3)
        self.login_page.click_register()
        time.sleep(3)

        cart_data = self.config['cart']
        self.register_page.fill_registration_form(
            cart_data["register_name_for_cart"],
            cart_data["register_email_for_cart"],
            cart_data["register_password_for_cart"],
            cart_data["register_confirm_password_for_cart"]
        )
        time.sleep(3)
        self.register_page.submit_registration()
        time.sleep(3)

    def test_add_and_modify_cart(self):
        self.driver.get(self.config['url'])
        self.home_page.click_on_sign_in_link()
        time.sleep(3)

        self.login_page.click_register()
        time.sleep(3)

        cart_data = self.config['cart']
        self.register_page.fill_registration_form(
            name=cart_data["register_name_for_cart"],
            email=cart_data["register_email_for_cart"],
            password=cart_data["register_password_for_cart"],
            confirm_password=cart_data["register_confirm_password_for_cart"]
        )
        time.sleep(3)
        self.register_page.submit_registration()
        time.sleep(3)
        self.search_page.search_for_product(cart_data["search_product_for_cart"])
        self.search_page.click_search_button()
        time.sleep(3)
        self.cart_page.add_to_cart()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
