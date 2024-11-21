import add_books as addBooks
import view_all_books as viewAllBooks
import update_books as updateBook
import remove_book as removeBook


options = ["Exit", "Add Books", "Update Book", "Remove Book", "View All Books"]
all_books = []


def greeting():
    print("\n Library Management System \n-------------------------")

    for index, value in enumerate(options, start=1):
        print(f"{index}. {value}")


def choose_option(choice):
    if choice == 1:
        print("Thanks for using Library Management System ")
    elif choice == 2:
        addBooks.add_books(all_books)
    elif choice == 3:
        updateBook.update_book(all_books)
    elif choice == 4:
        removeBook.remove_book(all_books)
    elif choice == 5:
        viewAllBooks.view_all_books(all_books)
    else:
        print("Invalid choice. Please select a number from the list.")


while True:
    try:
        greeting()
        choice = int(input("Choose an option (1-5): "))  # Convert input to integer
        print("-----------------------------------")
        choose_option(choice)
    except Exception as e:
        pass
    finally:
        print("Thanks for using Library Management System.")
