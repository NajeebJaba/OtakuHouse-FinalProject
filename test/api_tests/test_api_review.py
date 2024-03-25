import unittest
from infra.api_infra.api_browser_wrapper import APIBrowserWrapper
from logic.api_logic.api_review import APIReviewPage


class TestAPIReviewPage(unittest.TestCase):
    def setUp(self):
        self.review_page = APIReviewPage()

    def test_post_review(self):
        product_id = 24
        review_data = {
            "rating": "5",
            "comment": "Product is beautiful"
        }
        response = self.review_page.post_review(product_id, review_data)
        self.assertTrue(response.status_code, 200)
        # Optionally check the response body content
        # response_data = response.json()
        # self.assertTrue(response_data['comment'], review_data['comment'])
        # self.assertTrue(response_data['rating'], int(review_data['rating']))

    # Add more test cases if needed


if __name__ == '__main__':
    unittest.main()
