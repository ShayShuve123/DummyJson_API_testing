import requests
import os
from dotenv import load_dotenv, dotenv_values

from src.configs.hosts_config import DUMMY_JSON_API_BASE_URL

load_dotenv()


class RequestsUtility:
    def __init__(self):
        self.env = os.getenv("ENV", "test")
        self.base_url = DUMMY_JSON_API_BASE_URL[self.env]

    def get(self, endpoint, params=None, headers=None, expected_status_code=200):
        assert isinstance(endpoint, str), f"Invalid endpoint, endpoint must be a string\nendpoint:{endpoint}"
        url = self.base_url + endpoint
        response = requests.get(url=url, params=params, headers=headers)
        self.validate_status_code(expected_status_code, response.status_code)
        # add logger
        return response.json()

    @staticmethod
    def validate_status_code(expected_status_code, status_code):
        assert expected_status_code == status_code, f"Unmatched status code, expected:{expected_status_code} actual:{status_code}"
