from infra.api_infra.api_browser_wrapper import APIBrowserWrapper

class APIOrderPage:
    def __init__(self, api_browser_wrapper):
        self.api_browser_wrapper = api_browser_wrapper

    def place_order(self, order_data, headers):
        endpoint = "api/orders/add/"
        response = self.api_browser_wrapper.post(endpoint, order_data, headers)
        return response
