from books import create_books_file, load_books, save_books
from lenders import create_lenders_file, load_lended_books, save_lended_books
from datetime import datetime

def lend_book():
    books = load_books()
    lended_books = load_lended_books()

    borrower_name = input("Enter borrower's name: ")
    borrower_phone = input("Enter borrower's phone: ")
    book_title = input("Enter book title to lend: ")
    due_date_str = datetime.now().strftime("%d-%m-%Y %H:%M")
    
    try:
        due_date = datetime.strptime(due_date_str, "%d-%m-%Y %H:%M")
    except ValueError:
        print("Invalid date format.")
        return

    book = next((book for book in books if book['title'].lower() == book_title.lower()), None)
    if not book:
        print(f"Book '{book_title}' not found.")
        return

    if book['quantity'] > 0:
        book['quantity'] -= 1
        lended_books.append({
            'borrower_name': borrower_name,
            'borrower_phone': borrower_phone,
            'book_title': book_title,
            'due_date': due_date
        })
        print(f"Book '{book_title}' lent to {borrower_name}. Due: {due_date_str}")
    else:
        print("Book not available.")

    save_books(books)
    save_lended_books(lended_books)

def return_book():
    books = load_books()
    lended_books = load_lended_books()

    borrower_name = input("Enter borrower's name: ")
    book_title = input("Enter book title to return: ")

    lend_record = next((record for record in lended_books if record['borrower_name'].lower() == borrower_name.lower() and record['book_title'].lower() == book_title.lower()), None)

    if lend_record:
        lended_books.remove(lend_record)
        book = next((book for book in books if book['title'].lower() == book_title.lower()), None)
        if book:
            book['quantity'] += 1
        print(f"Book '{book_title}' returned by {borrower_name}.")
    else:
        print(f"No record found for {borrower_name} borrowing '{book_title}'.")

    save_books(books)
    save_lended_books(lended_books)

def add_book():
    books = load_books()
    title = input("Enter book title: ")
    author = input("Enter author: ")
    quantity = int(input("Enter quantity: "))

    books.append({'title': title, 'author': author, 'quantity': quantity})
    save_books(books)
    print(f"Book '{title}' added.")

def view_books():
    books = load_books()
    if not books:
        print("No books available.")
    else:
        print("Books:")
        for book in books:
            print(f"Title: {book['title']}, Author: {book['author']}, Quantity: {book['quantity']}")

def main():
    create_books_file()
    create_lenders_file()

    while True:
        print("\nLibrary Management System")
        print("1. Lend a book")
        print("2. Return a book")
        print("3. Add a book")
        print("4. View books")
        print("5. Exit")

        choice = input("Enter choice: ")
        if choice == '1':
            lend_book()
        elif choice == '2':
            return_book()
        elif choice == '3':
            add_book()
        elif choice == '4':
            view_books()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
