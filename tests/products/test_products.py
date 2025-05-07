import pytest
import requests.exceptions
from src.utilities.generic_utils import load_random_product_payload


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
        "pricee": 1,
        "": "empty"
    }

    # make a post call to add a new product
    product_response = products_helper.add_new_product(product_payload)

    # validate the response without get the product id from the server Note: "Adding a new product will not add it into the server."
    assert len(product_response) == 1, f"The response continue more the one filed.\nResponse: {product_response}"
    assert "pricee" not in product_response
    assert "" not in product_response


@pytest.mark.negative
@pytest.mark.tid8
def test_update_product_with_non_existent_id(products_helper):
    random_payload = load_random_product_payload()
    product_id = random_payload["id"]

    with pytest.raises(requests.exceptions.HTTPError) as e:
        products_helper.update_product(product_id=product_id, payload=random_payload)

    assert f"'{product_id}' not found" in str(e.value)


@pytest.mark.tid9
def test_delete_product_successfully(products_helper):
    # creat a new product and add it
    random_payload = load_random_product_payload()
    product_id = random_payload["id"]
    product_title = random_payload["title"]
    product_response = products_helper.add_new_product(random_payload)

    assert isinstance(product_response["id"], int), "Invalid id, id must be an integer."
    assert product_response["title"] == product_title

    # make a call to delete the product
    deleted_product = products_helper.delete_product(product_id)

    # verify the response: 1)"isDeleted" should be "true" 2)the same id in the request
    assert deleted_product
    assert deleted_product["isDeleted"] == True, "Product deletion failed."
    assert "deletedOn" in deleted_product, "Product deletion date is missing."
    assert deleted_product[
               "id"] == product_id, "The ID of the product to be deleted does not match the ID of the deleted product."


@pytest.mark.negative
@pytest.mark.tid10
def test_delete_product_non_existent_id(products_helper):
    product_id = -10

    with pytest.raises(requests.exceptions.HTTPError) as e:
        products_helper.delete_product(product_id)
        assert f"'{product_id}' not found" in str(e)

    assert f"'{product_id}' not found" in str(e.value)
