# Name validation
def validate_name(name):

    if not isinstance(name, str) and name.strip():
        return False

    if not all(part.isalpha() for part in name.split()):
        return False
    return True


# Phone number validation
def validate_phone(phone, contacts):
    if phone in [contact["phone"] for contact in contacts]:
        print("Error: Phone number already exists.")
        return False
    if not phone.isdigit():
        print("Error: Phone number must be a numeric value.")
        return False
    if len(phone) != 11:
        print("Error: Phone number must be exactly 11 digits.")
        return False
    return True


# Email validation
def validate_email(email):
    if "@" not in email or "." not in email:
        print("Error: Please provide a valid email address.")
        return False
    return True
