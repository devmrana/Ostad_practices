import save_all_books as saveAllBooks


def add_books(all_books):
    title = input("Enter book Title: ")
    author = input("Enter book Author: ")
    isbn = int(input("Enter book ISBN: "))
    year = int(input("Enter book Year: "))
    price = int(input("Enter book Price: "))
    quantity = int(input("Enter Quantity number: "))

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity,
    }

    all_books.append(book)
    saveAllBooks.save_all_books(all_books)
    print("Book added succesfully!!")
    return all_books
