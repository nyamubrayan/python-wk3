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
    print(f"The final price after applying {discount_percentage}% discount is: {final_price}" )

else:

   print(f"No discount applied. The price remains: {final_price}")