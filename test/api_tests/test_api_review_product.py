import unittest
from logic.api_logic.api_login_page import LoginAPI
from logic.api_logic.api_review_product import ReviewProduct


class TestReviewProduct(unittest.TestCase):

    def setUp(self):
        self.review_product_in_page = ReviewProduct()
        self.from_login_page = LoginAPI()
        self.response = None
        self.data = None

    def test_get_product_page(self):
        print("\nStarting test for fetching product page...")
        self.response = self.review_product_in_page.get_product_page(self.review_product_in_page.product_id)
        self.assertEqual(self.response.status_code, 200, "Failed to fetch product page with status code 200")

    def test_review_product_in_page(self):
        print("\nStarting test for adding a product review...")
        self.response = self.review_product_in_page.add_product(self.review_product_in_page.rate, self.review_product_in_page.review_comment, self.review_product_in_page.product_id)
        # Check if a review was already added, expect a 400 error
        if 'Product already reviewed' in self.response.json().get('detail', ''):
            self.assertEqual(self.response.status_code, 400, "Expected failure when adding duplicate review")
        else:
            self.assertEqual(self.response.status_code, 201, "Failed to add product review with status code 201")


if __name__ == "__main__":
    unittest.main()
