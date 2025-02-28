def calculate_remainder(a, b):
    # Perform modulo operation
    return a % b

# Input: Two integers
a, b = map(int, input("Enter two numbers: ").split())

# Check for division by zero
if b == 0:
    print("Error: Division by zero is not allowed.")
else:
    # Calculate remainder
    remainder = calculate_remainder(a, b)
    # Output the remainder
    print(remainder)
