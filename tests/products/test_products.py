import pytest

from src.helpers.products_helper import ProductHelper


# pass to conftest
@pytest.fixture
def products_helper():
    return ProductHelper()


@pytest.mark.tid1
def test_get_all_products(products_helper):
    """smok test to get all products"""
    limit_per_page = 30

    # make a request and verify status code 200
    products = products_helper.get_all_products()

    products_amount = len(products)
    # the products are not empty
    assert products, f"Expected {limit_per_page} products but got {products_amount}"

    # number of items in products equal to the limit_per_page
    assert products_amount == limit_per_page


@pytest.mark.tid2
def test_search_product_by_text(products_helper):
    txt_to_search = "phone"
    # make a request and verify status code 200
    searched_products = products_helper.search_product(txt_to_search)

    # ensure that the result contains at least one item.
    assert len(searched_products) >= 1, "The response does not contain any products."

    # ensure all returned products contain the searched term.
    for product in searched_products:
        product_description = product.get("description", "").lower()
        assert txt_to_search in product_description, f"The product: {product['title']}, dose not contain the search text: {txt_to_search}"


@pytest.mark.negative
@pytest.mark.parametrize("txt_to_search",
                         [
                             pytest.param("f", marks=pytest.mark.tid3, id="tid3"),
                             pytest.param(25, marks=pytest.mark.tid4, id="tid4")
                         ]
                         )
def test_search_product_by_invalid_text(products_helper, txt_to_search):
    """Validate search fails for invalid inputs (non-string or too short)"""

    with pytest.raises(ValueError, match="Invalid search text; text must be a string longer than one character."):
        products_helper.search_product(txt_to_search)

def test_create_new_product_successfully():
    pass

def test_create_new_product_unsuccessfully():
    pass
