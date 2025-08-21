# Discount Calculator

This is a simple Python program that calculates the final price of an item after applying a discount.  
If the discount percentage is **20% or higher**, the discount will be applied. Otherwise, the original price is returned.

## How it works
1. The user is prompted to enter:
   - The original price of the item.
   - The discount percentage.
2. The program checks:
   - If the discount is **20% or higher**, it subtracts the discount from the original price.
   - If the discount is less than 20%, the original price is returned.
3. The result is displayed to the user.

## Code Example
```python
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percentage)

if discount_percentage >= 20:
    print(f"The final price after applying {discount_percentage}% discount is: {final_price}")
else:
    print(f"No discount applied. The price remains: {final_price}")

Example Run
Enter the original price of the item: 1000
Enter the discount percentage: 25
The final price after applying 25.0% discount is: 750.0

Requirements

Python 3.x



Run the script in your terminal:

python discount_calculator.py
