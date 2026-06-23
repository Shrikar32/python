# #while loop executes code While a condition is true
# name = input("Enter your name: ")
# while name == "":
#     print("Name cannot be empty, Please enter your name.")
#     name = input("Enter your name: ")

# print(f"Hello, {name}!") 

age = int(input("Enter your age: "))
while age < 0:
    print("Age cannot be negative, Please enter your age again.")
    age = int(input("Enter your age: "))
print(f"You are {age} years old.")    