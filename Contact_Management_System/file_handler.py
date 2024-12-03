import csv

FILENAME = "1.Exam/contacts.csv"


def load_contacts():
    try:
        with open(FILENAME, mode="r") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(FILENAME, mode="w", newline="") as file:
        fieldnames = ["name", "phone", "email", "address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)
