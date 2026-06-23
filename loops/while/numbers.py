num = float(input("Enter a number between 1 and 10: "))
while num < 1 or num > 10:
    print("Invalid Number, must be between 1 and 10.")
    num = float(input("Enter a number between 1 and 10: "))
  
print(f"You entered {num}.")