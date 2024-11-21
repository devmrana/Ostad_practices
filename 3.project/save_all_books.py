import csv


def save_all_books(all_books):
    fields = ["Title", "Author", "ISBN", "Year", "Price", "Quantity"]

    with open("Class practices/3.project/all_books.csv", "w", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=fields)
        writer.writeheader()

        for book in all_books:
            writer.writerow(
                {
                    "Title": book["title"],
                    "Author": book["author"],
                    "ISBN": book["isbn"],
                    "Year": book["year"],
                    "Price": book["price"],
                    "Quantity": book["quantity"],
                }
            )
