import unittest
from infra.api_infra.api_browser_wrapper import APIBrowserWrapper
from logic.api_logic.api_place_order import APIOrderPage
from infra.api_infra.api_config_handler import APIConfigHandler


class TestAPIOrderPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #cls.api_config = APIHandler().read_config_data()
        cls.api_browser_wrapper = APIBrowserWrapper()
        cls.order_page = APIOrderPage(cls.api_browser_wrapper)

    def test_place_order(self):
        order_data = self.api_config['order_place']
        headers = {"Authorization": self.api_config['auth_token_order_place']}
        response = self.order_page.place_order(order_data, headers)
        self.assertTrue(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()