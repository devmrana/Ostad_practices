from validation import validate_name, validate_phone, validate_email


def add_contact(contacts):
    print("\n--- Add Contact ---")
    name = input("Enter name: ")
    if not validate_name(name):
        print("Error: Name must be a string.")
        return
    phone = input("Enter phone number: ")
    if not validate_phone(phone, contacts):
        print("Error: Phone number must be a numeric value.")
        return

    email = input("Enter email: ")
    if not validate_email(email):
        return
    address = input("Enter address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully!")


def view_contacts(contacts):
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.")
        return
    for index, contact in enumerate(contacts, start=1):
        print(
            f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}"
        )


def remove_contact(contacts):
    print("\n--- Remove Contact ---")
    phone = input("Enter the phone number of the contact to remove: ")
    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            print("Contact removed successfully!")
            return
    print("Error: Contact not found.")


def search_contacts(contacts):
    print("\n--- Search Contacts ---")
    keyword = input("Enter name, phone, email, or address to search: ").lower()
    results = [
        contact
        for contact in contacts
        if keyword in contact["name"].lower()
        or keyword in contact["phone"]
        or keyword in contact["email"].lower()
        or keyword in contact["address"].lower()
    ]
    if results:
        for contact in results:
            print(
                f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}"
            )
    else:
        print("No matching contacts found.")


def update_contact(contacts):
    print("\n--- Update Contact ---")
    phone = input("Enter the phone number of the contact to update: ")
    for contact in contacts:
        if contact["phone"] == phone:
            print(
                f"Current details: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}"
            )
            print("Leave a field blank to keep the current value.")
            new_name = input("Enter new name: ")
            # phone number is unique, that' why hide from phone update
            # new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")

            # Validate and update fields
            if new_name.strip():
                if not validate_name(new_name):
                    print("Error: Invalid name.")
                    return
                contact["name"] = new_name

            # phone number is unique, that' why hide from phone update
            # if new_phone.strip():
            #     if not validate_phone(new_phone):
            #         print("Error: Invalid phone number.")
            #         return
            #     if new_phone != phone and any(c['phone'] == new_phone for c in contacts):
            #         print("Error: Phone number already exists.")
            #         return
            #     contact['phone'] = new_phone

            if not validate_email(new_email):
                print("So, Email not updated!")
                return
            contact["email"] = new_email

            if new_address.strip():
                contact["address"] = new_address

            print("Contact updated successfully!")
            return
    print("Error: Contact not found.")
