def calculate_discounted_price(original_price, discount_percentage):
    # Calculate the discounted amount
    discount_amount = (original_price * discount_percentage) / 100
    # Calculate the final price after applying the discount
    final_price = original_price - discount_amount
    return final_price

# Input: Original price and discount percentage
original_price, discount_percentage = map(int, input().split())

# Calculate final price
final_price = calculate_discounted_price(original_price, discount_percentage)

# Output the result rounded to two decimal places
print(f"Price: {final_price:.2f}")
