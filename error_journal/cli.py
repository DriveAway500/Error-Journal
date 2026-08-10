import argparse
import json
import os

from .db import get_errors_by_identifier, set_db_path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("identifier")
    args = parser.parse_args()

    config_path = os.path.join(os.getcwd(), "finns_address.json")

    with open(config_path) as file:
        config = json.load(file)

    set_db_path(config["db_path"])

    errors = get_errors_by_identifier(args.identifier)

    for error_id, message, created_at in errors:
        print(f"[{error_id}] {created_at} - {message}")