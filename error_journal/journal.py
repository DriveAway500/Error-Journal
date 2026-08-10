from .db import(
    set_db_path,
    insert_error,
    )

from functools import wraps
import traceback


class Journal:

    def __init__(self, db_path: str = None):
        """Initializes the journal, optionally setting the database path."""
        if db_path:
            self.home(db_path)

    def home(self, db_path: str):
        """Sets the database directory path and prepares the database."""
        if not db_path or not db_path.strip():
            raise ValueError("Database path cannot be empty.")

        set_db_path(db_path.strip())

    def log(self, identifier: str, error_message: str):
        """Logs an error with the given identifier and error message."""
        if not identifier or not identifier.strip():
            raise ValueError("Identifier cannot be empty.")

        if not error_message or not error_message.strip():
            raise ValueError("Error message cannot be empty.")

        try:
            insert_error(identifier.strip(), error_message.strip())
        except ValueError as e:
            raise RuntimeError(
                "Journal is not initialized. Call home(db_path) first."
            ) from e

    def catch(self, identifier: str = None, reraise: bool = True):
        """Decorator that catches exceptions, logs full traceback, and optionally reraises them."""

        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    # Uses custom identifier or defaults to the function name
                    tag = identifier or func.__name__
                    full_trace = traceback.format_exc()
                    self.log(tag, full_trace)

                    if reraise:
                        raise

            return wrapper

        return decorator
        