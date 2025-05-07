# 🧪 DummyJSON API Testing Framework

A Pytest-based automation framework for testing the [DummyJSON](https://dummyjson.com/) public REST API.

## 🚀 Project Overview

This framework was built to simulate real-world QA practices in API testing:
- Modular structure for easy scaling
- Centralized request logic and reusable helpers
- Separation between test logic and API logic
- Negative & positive testing
- Support for configuration and dynamic payloads
- **Automatic HTML test reports** with `pytest-html`

## 📁 Project Structure

```
.
├── data/
│   └── product_payloads.json           # Sample product data for testing
├── reports/
│   └── __init__.py                     # Init file for reports module (reserved for future reporting tools)
├── src/
│   ├── configs/
│   │   ├── __init__.py
│   │   └── hosts_config.py             # Environment-specific base URLs
│   ├── helpers/
│   │   ├── __init__.py
│   │   └── products_helper.py          # Business logic for product API operations
│   └── utilities/
│       ├── __init__.py
│       ├── requests_utility.py         # Generic HTTP methods (GET, POST, PUT, DELETE)
│       └── generic_utils.py            # Shared utility functions (e.g. payload loader)
├── tests/
│   ├── products/
│   │   ├── __init__.py
│   │   └── test_products.py            # Test suite for product-related API endpoints
│   ├── __init__.py
│   ├── conftest.py                     # Global fixtures for test execution
├── .env                                # Environment variable definitions
├── .gitignore                          # Files/directories ignored by Git
├── pytest.ini                          # Pytest configuration and marker registration
├── README.md                           # Project overview and setup instructions
└── requirements.txt                    # Python dependencies
```

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/dummyjson-api-tests.git
cd dummyjson-api-tests
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## 🧪 Running Tests

Run all tests:
```bash
pytest
```

Run only negative tests:
```bash
pytest -m negative
```

Run test by ID:
```bash
pytest -m tid9
```

Run tests using shell script:
```bash
bash run_tests.sh
```

## ✅ Test Types

- **Smoke tests** – Ensure the basic functionality (e.g., fetch all products)
- **Positive tests** – Validate expected behaviors (create, update, delete)
- **Negative tests** – Validate error handling (invalid payloads, wrong IDs)

## 📦 Notes

- The framework uses `requests` for HTTP interactions.
- Tests are fully modular and easy to expand.
- Logging and assertions are clearly implemented.
- Tests use centralized payload loading (`product_payloads.json`) for flexibility.
- HTML reports are generated automatically in the reports/ folder when running tests.

