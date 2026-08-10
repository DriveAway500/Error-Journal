from error_journal import Journal

def main():
    error= "Error: Something went wrong!"
    identifier = "TestError"
    db_path = "error_journal_db/"

    journal = Journal()
    journal.home(db_path)
    journal.log(identifier, error)

if __name__ == "__main__":
    main()