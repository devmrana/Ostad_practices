import csv
from datetime import datetime

BOOKS_CSV = './5.project/books.csv'


def create_books_file():
    try:
        with open(BOOKS_CSV, mode='r') as file:
            pass  
    except FileNotFoundError:
        with open(BOOKS_CSV, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Author', 'Quantity'])

# Load books from CSV
def load_books():
    books = []
    try:
        with open(BOOKS_CSV, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                books.append({
                    'title': row[0],
                    'author': row[1],
                    'quantity': int(row[2])
                })
    except FileNotFoundError:
        print("Books file not found.")
    return books

# Save books to CSV
def save_books(books):
    with open(BOOKS_CSV, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Author', 'Quantity'])
        for book in books:
            writer.writerow([book['title'], book['author'], book['quantity']])
