from .db import set_db_path, insert_error

class Journal:

    def home(self, db_path: str):
        """Initializes the journal with database path."""
        if db_path:
            set_db_path(db_path)

    def log(self, identifier: str, error_message: str):
        """Logs an error with the given identifier and error message."""
        if not identifier or not identifier.strip():
            raise ValueError("Identifier cannot be empty.")

        if not error_message or not error_message.strip():
            raise ValueError("Error message cannot be empty.")

        insert_error(identifier.strip(), error_message.strip())
        