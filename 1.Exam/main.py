from contacts_manage import (
    add_contact,
    update_contact,
    view_contacts,
    remove_contact,
    search_contacts,
)
from file_handler import load_contacts, save_contacts


def main():
    contacts = load_contacts()  # previously saved contact data is loaded
    while True:
        print("\n### Welcome to Contact Management System ###")
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Update Contact")
        print("4. Remove Contact")
        print("5. Search Contacts")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            update_contact(contacts)
            save_contacts(contacts)
        elif choice == "4":
            if view_contacts(contacts) != "":
                remove_contact(contacts)
                save_contacts(contacts)
        elif choice == "5":
            search_contacts(contacts)
        elif choice == "6":
            print("Exit. Thanks for using Contact Management System")
            break
        else:
            print(
                "Invalid choice. Please try again. Please select a number from the list."
            )


if __name__ == "__main__":
    main()
