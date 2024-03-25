import unittest
from logic.api_logic.api_search_product import SearchProduct


class TestSearchProduct(unittest.TestCase):
    def setUp(self):
        self.existing_product = SearchProduct("DRAGON BALL SUPER - SON GOKU & VEGETA FIGURE")
        self.nonexistent_product = SearchProduct("aaaaaaaaaa")

    def test_search_existing_product(self):
        response = self.existing_product.search()
        self.assertEqual(response.status_code, 200)

    def test_search_nonexistent_product(self):
        response = self.nonexistent_product.search()
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
