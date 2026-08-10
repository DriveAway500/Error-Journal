import sqlite3
import json
import os

DB_NAME = "finns_house.db"
db_path = None

def save_path(path: str):
    global db_path
    db_path = path

    with open("finns_address.json", "w") as file:
        json.dump({"db_path": path}, file, indent=4)

def set_db_path(path: str):
    """Sets the path for the database and creates the directory if needed."""
    if not path or not path.strip():
        raise ValueError(
            "Finn needs a house to live in. "
            "Please provide a valid path for the database."
        )

    clean_path = path.strip()
    os.makedirs(clean_path, exist_ok=True)

    global db_path
    db_path = clean_path
    save_path(clean_path)


def get_db_path():
    """Returns the current database directory path."""
    if not db_path:
        raise ValueError(
            "Finn needs a house to live in. "
            "Please provide a valid path for the database."
        )

    return db_path


def get_db_file():
    """Returns the full path to the database file safely."""
    return os.path.join(get_db_path(), DB_NAME)


def init_db():
    """Creates the errors table if it does not already exist."""
    with sqlite3.connect(get_db_file()) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS errors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                identifier TEXT NOT NULL,
                error_message TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)


def insert_error(identifier: str, error_message: str):
    """Inserts an error using the provided identifier."""
    init_db()
    with sqlite3.connect(get_db_file()) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO errors (identifier, error_message) VALUES (?, ?)",
            (identifier, error_message),
        )


def get_errors_by_identifier(identifier: str):
    """Returns all errors registered under the given identifier."""
    init_db()
    with sqlite3.connect(get_db_file()) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT id, error_message, created_at
            FROM errors
            WHERE identifier = ?
            ORDER BY id ASC
            """,
            (identifier,),
        )
        return cursor.fetchall()