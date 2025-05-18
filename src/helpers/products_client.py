from src.paths.products import ProductsPath
from src.utilities.requests_utility import RequestsUtility


class ProductHelper:

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_all_products(self):
        products_response = self.requests_utility.get(ProductsPath.get_root_path())

        try:
            return products_response["products"]
        except KeyError:
            raise KeyError("Expected key 'products' not found in the response.")

    def search_product(self, txt_product_to_search):
        params = {'q': txt_product_to_search}

        if not isinstance(txt_product_to_search, str) or len(txt_product_to_search) <= 1:
            raise ValueError("Invalid search text; text must be a string longer than one character.")

        products_response = self.requests_utility.get(endpoint=ProductsPath.get_search_path(), params=params)

        try:
            return products_response["products"]
        except KeyError:
            raise KeyError("Expected key 'products' not found in the response.")

    def add_new_product(self, payload):
        assert isinstance(payload, dict), "payload must be dict"
        product_response = self.requests_utility.post(endpoint=ProductsPath.get_add_path(), payload=payload)
        return product_response

    def update_product(self, payload, product_id):
        update_product = self.requests_utility.put(endpoint=ProductsPath.get_product_by_id_path(product_id),
                                                   payload=payload)
        return update_product

    def delete_product(self, product_id):

        deleted_product = self.requests_utility.delete(endpoint=ProductsPath.get_product_by_id_path(product_id))
        return deleted_product
