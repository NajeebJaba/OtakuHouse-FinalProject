import unittest
from logic.api_logic.api_search_product import SearchProduct

class TestSearchProduct(unittest.TestCase):
    def setUp(self):
        self.search_api = SearchProduct()
        self.search_data = {
            'search_prod_one': "Dragon Ball Super - Son Goku & Vegeta Figure",
            # 'search_prod_two': "aaaaaaaaaaa",
            'search_prod_three': "Dragon Ball Super - Son Goku & Vegeta Figureaaaaaaaaaaa"
        }

    def test_successful_search(self):
        response = self.search_api.search_product_in_home_page(self.search_data['search_prod_one'])
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.json()), 0, "The response JSON should not be empty for a successful search.")
        print("Test for successful search passed.")


    def test_unsuccessful_search_but_show_result(self):
        response = self.search_api.search_product_in_home_page(self.search_data['search_prod_three'])
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.json()), 0, "The response JSON should not be empty due to a bug, even though it's an incorrect behavior.")
        print("Test for unsuccessful search but showing result passed (indicating a bug).")


if __name__ == '__main__':
    unittest.main()
