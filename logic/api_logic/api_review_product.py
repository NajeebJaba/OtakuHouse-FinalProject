from infra.api_infra.api_wrapper import APIWrapper


class ReviewProduct(APIWrapper):
    def __init__(self):
        super().__init__()
        self.json = None

    def get_product_page(self, id_product):
        return self.api_get_request(f'{self.url}api/products/{id_product}/')

    def add_product(self, rating_product, review_comment, id_product):
        self.json = {"rating": rating_product, "comment": review_comment}

        self.response = self.request.post(f'{self.url[:-2]}api/products/{id_product}/reviews/', json=self.json,
                                          headers=self.headers)
        print(f'Data is correct JSON: {self.response.json()}')
        return self.response