import csv
from datetime import datetime

LENDERS_CSV = './5.project/lenders.csv'

# Ensure CSV file creation for lenders
def create_lenders_file():
    try:
        with open(LENDERS_CSV, mode='r') as file:
            pass  # If file exists, do nothing
    except FileNotFoundError:
        with open(LENDERS_CSV, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Borrower Name', 'Phone', 'Book Title', 'Return Due Date'])

# Load lent books from CSV
def load_lended_books():
    lended_books = []
    try:
        with open(LENDERS_CSV, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                lended_books.append({
                    'borrower_name': row[0],
                    'borrower_phone': row[1],
                    'book_title': row[2],
                    'due_date': datetime.strptime(row[3], "%Y-%m-%d %H:%M")
                })
    except FileNotFoundError:
        print("Lenders file not found.")
    return lended_books

# Save lent books to CSV
def save_lended_books(lended_books):
    with open(LENDERS_CSV, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Borrower Name', 'Phone', 'Book Title', 'Return Due Date'])
        for record in lended_books:
            writer.writerow([
                record['borrower_name'], 
                record['borrower_phone'], 
                record['book_title'], 
                record['due_date'].strftime("%Y-%m-%d %H:%M")
            ])
