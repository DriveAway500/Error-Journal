# Error Journal

A lightweight Python library for storing and retrieving application errors using SQLite.

Error Journal lets you associate errors with an identifier, store them in a local database, and retrieve them later through the library or its CLI.

## Installation

```bash
pip install error-journal
```

## Usage

```python
from error_journal import Journal

journal = Journal()

journal.home("./data")

journal.log(
    "crawler",
    "Failed to fetch https://example.com"
)
```

The database will be stored as:

```text
./data/finns_house.db
```

The database path is also saved in `finns_address.json`, allowing the CLI to locate the database later.

## CLI

After installing the package, use:

```bash
error-journal crawler
```

This retrieves all errors stored under the `crawler` identifier.

Example output:

```text
[1] 2026-08-09 14:32:10 - Failed to fetch https://example.com
[2] 2026-08-09 14:35:42 - Connection timed out
```

## Identifiers

Identifiers are used to group related errors.

For example:

```python
journal.log("crawler", "Request failed")
journal.log("crawler", "Connection timed out")
journal.log("database", "Failed to open database")
```

You can then retrieve only the errors associated with a specific identifier:

```bash
error-journal crawler
```

## Database

Error Journal uses SQLite and creates a database named:

```text
finns_house.db
```

The database contains the stored error information, including:

* Error ID
* Identifier
* Error message
* Creation timestamp

## License

This project is licensed under the MIT License.
