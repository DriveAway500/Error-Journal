from error_journal import Journal


def run_and_log(journal: Journal, identifier: str, action):
    try:
        action()
    except Exception as e:
        error_msg = f"{type(e).__name__}: {str(e)}"
        journal.log(identifier, error_msg)


def main():
    db_path = "error_journal_db/"
    journal = Journal()
    journal.home(db_path)

    test_cases = [
        ("ZeroDivision", lambda: 10 / 0),
        ("ValueError", lambda: int("invalid_number")),
        ("IndexError", lambda: [1, 2, 3][10]),
        ("KeyError", lambda: {}["missing_key"]),
        ("TypeError", lambda: "texto" + 50),
    ]

    for identifier, action in test_cases:
        run_and_log(journal, identifier, action)

if __name__ == "__main__":
    main()