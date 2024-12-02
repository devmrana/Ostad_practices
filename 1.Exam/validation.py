def validate_name(name):
    return isinstance(name, str) and name.strip() != ""


def validate_phone(phone, contacts):
    
    if phone in [contact["phone"] for contact in contacts]:
        print("Error: Phone number already exists.")
        return
    return phone.isdigit()


def validate_email(email):
    if "@" in email and "." in email:
        return True
    print("Error: Please provide a valid email address.")
    return False
