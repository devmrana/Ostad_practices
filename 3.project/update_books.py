import save_all_books as saveAllBoooks


def update_book(all_books):

    isbn_to_update = int(input("Enter the ISBN of the book to update: "))
    for book in all_books:
        if book["isbn"] == isbn_to_update:
            print("Book found! Enter new details, Now you can update data...")
            title = (
                input(f"Current Title: {book['title']} | New Title: ") or book["title"]
            )
            author = (
                input(f"Current Author: {book['author']} | New Author: ")
                or book["author"]
            )
            year = input(f"Current Year: {book['year']} | New Year: ") or book["year"]
            price = (
                input(f"Current Price: {book['price']} | New Price: ") or book["price"]
            )
            quantity = (
                input(f"Current Quantity: {book['quantity']} | New Quantity: ")
                or book["quantity"]
            )

            book.update(
                {
                    "title": title,
                    "author": author,
                    "year": int(year),
                    "price": int(price),
                    "quantity": int(quantity),
                }
            )
            saveAllBoooks.save_all_books(all_books)
            print("Book updated successfully!")
            return all_books
    print("Book not found!")
    return all_books
