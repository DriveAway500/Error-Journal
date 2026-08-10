from error_journal import Journal

journal = Journal("error_journal_db/")

@journal.catch(identifier="PaymentSystem")
def process_payment():
    return 10 / 0


@journal.catch()
def calculate_discount():
    return int("invalid")

@journal.catch(identifier="BackgroundWorker", reraise=False)
def non_critical_task():
    raise KeyError("Missing config key")

def main():
    non_critical_task()
    process_payment()
    calculate_discount()

if __name__ == "__main__":
    main()