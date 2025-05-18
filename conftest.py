import pytest

from src.helpers.products_client import ProductHelper
from src.utilities.requests_utility import RequestsUtility


@pytest.fixture(scope="session")
def products_helper():
    return ProductHelper()


@pytest.fixture
def product_payload_factory():
    """Factory fixture to create a flexible payload of product."""

    def _factory(**kwargs):
        payload = {}
        payload.update(kwargs)

        required_payload = {
            "title": kwargs.get("title", None) or "default title",
            "price": kwargs.get("price", None) or 50,
            "category": kwargs.get("category", None) or "default category"
        }

        payload.update(required_payload)

        return payload

    return _factory
