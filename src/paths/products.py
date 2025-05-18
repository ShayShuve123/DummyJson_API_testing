class ProductsPath:
    ROOT = "products"

    @classmethod
    def get_root_path(cls):
        return cls.ROOT

    @classmethod
    def get_search_path(cls):
        return f"{cls.ROOT}/search"

    @classmethod
    def get_add_path(cls):
        return f"{cls.ROOT}/add"

    @classmethod
    def get_product_by_id_path(cls, product_id):
        assert isinstance(product_id, int), "product_id must be int"
        return f"{cls.ROOT}/{product_id}"
