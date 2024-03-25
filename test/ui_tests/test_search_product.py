import unittest
from infra.ui_infra.browser_wrapper import BrowserWrapper
from logic.ui_logic.search_product import SearchPage
from infra.ui_infra.config_handler import ConfigHandler


class TestSearchProduct(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config_handler = ConfigHandler()
        cls.config = cls.config_handler.config
        cls.browser_wrapper = BrowserWrapper()
        cls.driver = cls.browser_wrapper.initialize_driver()

    def test_search_existing_product(self):
        search_page = SearchPage(self.driver)
        search_page.search_for_product(self.config["search_product"])
        search_page.click_search_button()
        search_page.go_back_to_home_page_click_logo()

    def test_search_nonexistent_product(self):
        search_page = SearchPage(self.driver)
        search_page.search_for_product(self.config["search_product_didnt_exist"])
        search_page.click_search_button()
        search_page.go_back_to_home_page_click_logo()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()