#shopping cart
item = input("Enter the item you want to buy: ")
quantity = int(input("Enter the quantity:"))
price = float(input("Enter the price of the item: "))
total_cost = quantity * price
print(f"the total cost of {quantity} {item}(s) is {total_cost}")