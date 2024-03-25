from infra.api_infra.api_browser_wrapper import APIBrowserWrapper


class APIReviewPage:
    def __init__(self):
        self.api_browser_wrapper = APIBrowserWrapper()

    def post_review(self, product_id, review_data):
        endpoint = f"api/products/{product_id}/reviews/"
        response = self.api_browser_wrapper.post(endpoint, review_data)
        return response