import pytest

from src.helpers.products_helper import ProductHelper
from src.utilities.generic_utils import load_random_product_payload


# pass to conftest
@pytest.fixture
def products_helper():
    return ProductHelper()


@pytest.fixture
def product_payload_factory():
    """Factory fixture to create a flexible payload of product."""

    def _factory(**kwargs):
        payload = {
            "title": kwargs.get("title", None) or "default title",
            "price": kwargs.get("price", None) or 50,
            "category": kwargs.get("category", None) or "default category"
        }

        return payload

    return _factory


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


@pytest.mark.tid5
def test_add_new_product_successfully(products_helper, product_payload_factory):
    # generate a random payload
    random_payload = load_random_product_payload()
    title = random_payload["title"]
    price = random_payload["price"]
    category = random_payload["category"]

    # creat a product payload
    product_payload = product_payload_factory(**random_payload)

    # make a post call to add a new product
    product_response = products_helper.add_new_product(product_payload)

    # validate the response without get the product id from the server Note: "Adding a new product will not add it into the server."
    assert isinstance(product_response["id"], int), "Invalid id, id must be an integer."
    assert product_response[
               "title"] == title, f"The product was created with a title different from the expected one.\nExpected:{title} actual:{product_response['title']}"
    assert product_response[
               "price"] == price, f"The product was created with a price different from the expected one.\nExpected:{price} actual:{product_response['price']}"
    assert product_response[
               "category"] == category, f"The product was created with a category different from the expected one.\nExpected:{category} actual:{product_response['category']}"


@pytest.mark.tid6
def test_add_new_product_successfully_with_empty_payload(products_helper):
    empty_payload = {}

    # make a post call to add a new product
    product_response = products_helper.add_new_product(empty_payload)

    # validate the response without get the product id from the server Note: "Adding a new product will not add it into the server."
    assert len(product_response) == 1
    assert isinstance(product_response["id"], int)


@pytest.mark.negative
@pytest.mark.tid7
def test_add_new_product_with_invalid_keys(products_helper, product_payload_factory):
    """A negative test that verifies that when attempting to add a product with keys that don't exist as valid product keys, the product is still created while the invalid keys are ignored."""

    product_payload = {
        "pricee":1,
        "":"empty"
    }

    # make a post call to add a new product
    product_response = products_helper.add_new_product(product_payload)

    # validate the response without get the product id from the server Note: "Adding a new product will not add it into the server."
    assert len(product_response) == 1
    assert "pricee" not in product_response
    assert "" not in product_response

