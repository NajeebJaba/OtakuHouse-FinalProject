from infra.api_infra.api_browser_wrapper import APIBrowserWrapper

class SearchProduct:
    def __init__(self, product_name):
        self.browser_wrapper = APIBrowserWrapper()
        self.product_name = product_name

    def search(self):
        endpoint = f"api/products/?q={self.product_name}"
        response = self.browser_wrapper.get(endpoint)
        return response