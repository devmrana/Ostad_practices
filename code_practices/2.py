def calculate_quotient(a, b):
    # Perform integer division
    return a // b

# Input: Two integers
a, b = map(int, input("Enter two numbers: ").split())

# Check for division by zero
if b == 0:
    print("Error: Division by zero is not allowed.")
else:
    # Calculate quotient
    quotient = calculate_quotient(a, b)
    # Output the quotient
    print(quotient)
