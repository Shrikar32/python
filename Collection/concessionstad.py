# concession stand program 
stall = { "Popcorn" : 1.56,
         "Hotdog" : 2.54,
         "Giant Pretzel" : 2.23,
         "Assist Candy" : 1.89,
         "Soda" : 1.84,
         "Bottled water" : 1.897
         }
Cart = []
total = 0
items = stall.items()
print("----This is our Menu----------")
for key, value in stall.items():
    print(f"{key:10} : ${value:.2f}")
print("------------------------------")
while True:
    food = input("Select an item you want to buy (Press q to quit)")
    if food.lower() == "q":
     print("Thank you for Shopping with us")
     print("Here is your Bill")
     break 
    elif stall.get(food) is None:
       print("We are sorry, This item is not availiable in our Cart")
       print("Would you like something else : ")
    else:
       print("Thank you, would you like to get something else too? ")
       Cart.append(food)
       total = total + stall[food]
for carts in Cart:
    print(carts, end=" ")
print()    
print("total : ",end=" ")
for cart in Cart:
    print(cart, end=" ")

print()
print(f"Total: ${total:.2f}")    
       


