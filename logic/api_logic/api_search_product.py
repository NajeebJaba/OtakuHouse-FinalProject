from infra.api_infra.api_wrapper import APIWrapper

class SearchProduct(APIWrapper):
    def __init__(self):
        super().__init__()

    def search_product_in_home_page(self, keyword):
        print(f"Searching for product with keyword: {keyword}")
        return self.api_get_request(f'{self.url[:-2]}api/products/?keyword={keyword}')
