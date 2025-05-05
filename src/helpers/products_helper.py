from src.utilities.requests_utility import RequestsUtility


class ProductHelper:
    def __init__(self):
        self.requests_utils = RequestsUtility()

    def get_all_products(self):
        endpoint = "products"
        products_response = self.requests_utils.get(endpoint)

        try:
            return products_response["products"]
        except KeyError:
            raise KeyError("Expected key 'products' not found in the response.")

    def search_product(self, txt_product_to_search):
        endpoint = "products/search"
        params = {'q': txt_product_to_search}

        if not isinstance(txt_product_to_search, str) or len(txt_product_to_search) <= 1:
            raise ValueError("Invalid search text; text must be a string longer than one character.")

        products_response = self.requests_utils.get(endpoint=endpoint, params=params)

        try:
            return products_response["products"]
        except KeyError:
            raise KeyError("Expected key 'products' not found in the response.")

