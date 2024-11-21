import save_all_books as saveAllBoooks


def remove_book(all_books):
    isbn_to_remove = int(input("Enter the ISBN of the book to remove: "))
    for book in all_books:
        if book["isbn"] == isbn_to_remove:
            all_books.remove(book)
            saveAllBoooks.save_all_books(all_books)
            print("Book removed successfully!")
            return all_books
    print("Book not found!")
    return all_books
