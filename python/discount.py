def discount(price, percentage):
    discount_amount = price * (percentage / 100)
    discounted_price = price - discount_amount
    return discounted_price
og= float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))
final_price = discount(og, discount_percentage)
print("The discounted price is:", final_price)
