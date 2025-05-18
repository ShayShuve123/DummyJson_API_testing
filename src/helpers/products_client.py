from src.utilities.requests_utility import RequestsUtility


class ProductHelper:
    _EP_PRODUCTS = "products"
    _EP_SEARCH = "products/search"
    _EP_PRODUCT = f"products/"
    _EP_ADD = "products/add"

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_all_products(self):
        products_response = self.requests_utility.get(self._EP_PRODUCTS)

        try:
            return products_response["products"]
        except KeyError:
            raise KeyError("Expected key 'products' not found in the response.")

    def search_product(self, txt_product_to_search):
        params = {'q': txt_product_to_search}

        if not isinstance(txt_product_to_search, str) or len(txt_product_to_search) <= 1:
            raise ValueError("Invalid search text; text must be a string longer than one character.")

        products_response = self.requests_utility.get(endpoint=self._EP_SEARCH, params=params)

        try:
            return products_response["products"]
        except KeyError:
            raise KeyError("Expected key 'products' not found in the response.")

    def add_new_product(self, payload):
        product_response = self.requests_utility.post(endpoint=self._EP_ADD, payload=payload)
        return product_response

    def update_product(self, payload, product_id):
        endpoint_product_id = self._EP_PRODUCT + str(product_id)
        update_product = self.requests_utility.put(endpoint=endpoint_product_id, payload=payload)
        return update_product

    def delete_product(self, product_id):
        endpoint_product_id = self._EP_PRODUCT + str(product_id)

        deleted_product = self.requests_utility.delete(endpoint_product_id)
        return deleted_product
