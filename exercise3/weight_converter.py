#weight converter
weight = float(input("Enter a weight: "))
unit = input("Enter a unit (kg or lbs): ")
if unit == "kg":
    converted_weight = weight*2.204
    print(f"The {weight} kg is equal to {converted_weight} lbs.")
elif unit == "lbs":
    converted_weight = weight/2.204
    print(f"The {weight} lbs is equal to {converted_weight} kg.")
else:
    print("Invalid unit. Please enter either 'kg' or 'lbs'.")
