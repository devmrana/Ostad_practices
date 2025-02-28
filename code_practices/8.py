# Read three floating-point numbers from the user
a, b, c = map(float, input("Enter three numbers:\n").split())

# Calculate the average
average = (a + b + c) / 3

# Print the result with exactly two decimal places
print(f"Average: {average:.2f}")
