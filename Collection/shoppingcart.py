# Shopping Cart

print("Welcome to the shopping cart program!")

items = []
prices = []
total = 0

while True:
    food = input("Enter a food you'd like to buy (press q to quit): ")

    if food.lower() == "q":
        print("That's all you'd like to buy.")
        break

    price = float(input(f"Enter the price of {food}: $"))

    items.append(food)
    prices.append(price)
    total += price

print("\nYour cart:")

for i in range(len(items)):
    print(f"{items[i]} - ${prices[i]:.2f}")

print(f"\nTotal = ${total:.2f}")