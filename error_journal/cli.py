import argparse
import json
import os
from colorama import Fore, Style, init
from .db import (
    get_errors_by_identifier,
    get_identifiers_with_counts,
    set_db_path,
)

# Automatically resets color back to default after each print statement
init(autoreset=True)


def handle_list(args):
    """Displays all identifiers and their counts."""
    identifiers = get_identifiers_with_counts()
    if not identifiers:
        print(f"{Fore.YELLOW}No identifiers found.")
        return

    for identifier, count in identifiers:
        print(f"{Fore.CYAN}{identifier}{Style.RESET_ALL}: {Fore.GREEN}{count}{Style.RESET_ALL} error(s)")


def handle_show(args):
    """Displays errors for a specific identifier."""
    errors = get_errors_by_identifier(args.identifier)
    if not errors:
        print(f"{Fore.YELLOW}No errors found for identifier '{args.identifier}'.")
        return

    for error_id, message, created_at in errors:
        print(
            #f"{Style.BRIGHT}[{error_id}]{Style.RESET_ALL} "
            f"{Fore.CYAN}{created_at}{Style.RESET_ALL} - "
            f"{Fore.RED}{message}"
        )


def main():
    parser = argparse.ArgumentParser(description="Error Log Manager")
    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Available subcommands"
    )

    # Subcommand: list
    parser_list = subparsers.add_parser(
        "list", help="List all identifiers and total error counts"
    )
    parser_list.set_defaults(func=handle_list)

    # Subcommand: show
    parser_show = subparsers.add_parser(
        "show", help="Show registered errors for an identifier"
    )
    parser_show.add_argument("identifier", help="Identifier name")
    parser_show.set_defaults(func=handle_show)

    # Parse CLI arguments
    args = parser.parse_args()

    # Load database configuration
    config_path = os.path.join(os.getcwd(), "finns_address.json")
    with open(config_path) as file:
        config = json.load(file)

    set_db_path(config["db_path"])

    # Execute the handler function for the selected subcommand
    args.func(args)


if __name__ == "__main__":
    main()