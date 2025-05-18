import requests
import os
from dotenv import load_dotenv

from src.configs.hosts_config import DUMMY_JSON_API_BASE_URL

load_dotenv()


class RequestsUtility:
    def __init__(self):
        self.env = os.getenv("ENV", "test")
        self.base_url = DUMMY_JSON_API_BASE_URL[self.env]
        self.response = None

    def get(self, endpoint, params=None, headers=None, expected_status_code=200):
        assert isinstance(endpoint, str), f"Invalid endpoint, endpoint must be a string\nendpoint:{endpoint}"
        url = self.base_url + endpoint
        self.response = requests.get(url=url, params=params, headers=headers)
        self.validate_status_code(expected_status_code, self.response.status_code)
        return self.response.json()

    def post(self, endpoint, payload=None, headers=None, expected_status_code=201):
        assert isinstance(endpoint, str), f"Invalid endpoint, endpoint must be a string\nendpoint:{endpoint}"
        url = self.base_url + endpoint
        self.response = requests.post(url=url, json=payload, headers=headers)
        self.validate_status_code(expected_status_code, self.response.status_code)
        return self.response.json()

    def put(self, endpoint, payload=None, headers=None, expected_status_code=200):
        assert isinstance(endpoint, str), f"Invalid endpoint, endpoint must be a string\nendpoint:{endpoint}"
        url = self.base_url + endpoint
        self.response = requests.put(url=url, json=payload, headers=headers)
        self.validate_status_code(expected_status_code, self.response.status_code)
        return self.response.json()

    def delete(self, endpoint, headers=None, expected_status_code=200):
        assert isinstance(endpoint, str), f"Invalid endpoint, endpoint must be a string\nendpoint:{endpoint}"
        url = self.base_url + endpoint
        self.response = requests.delete(url=url, headers=headers)
        self.validate_status_code(expected_status_code, self.response.status_code)
        return self.response.json()

    def validate_status_code(self, expected_status_code, status_code):
        if expected_status_code != status_code:
            raise requests.exceptions.HTTPError(
                f"Expected {expected_status_code}, got {status_code}. Response body: {self.response.text}"
            )
