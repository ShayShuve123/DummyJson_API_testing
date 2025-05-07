import json
import random
import os


def load_random_product_payload():
    file_name = "product_payloads.json"

    file_path = os.path.join(os.path.dirname(__file__), "..", "..", "data", file_name)
    file_path = os.path.abspath(file_path)

    try:
        with open(file_path) as json_file:
            payload = json.load(json_file)

    except FileNotFoundError as e:
        raise FileNotFoundError(f"The file :{file_name} was not found.\nError message: {e}")

    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid json file :{file_name}.\nError message: {e}")

    if not payload or isinstance(payload, dict):
        raise ValueError("Invalid payload, payload is empty or not a dictionary")

    return random.choice(payload)
