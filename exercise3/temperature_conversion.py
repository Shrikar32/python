#temperature conversion
temp = float(input("Enter the temperature: "))
unit = input("Enter the unit (C or F): ")
if unit == "C":
    CONVERTED_TEMP = (temp * 9/5) + 32
    print(f"the {temp}°C is equal to {CONVERTED_TEMP}°F.")
elif unit == "F":
    CONVERTED_TEMP = (temp - 32) * 5/9
    print(f"the {temp}°F is equal to {CONVERTED_TEMP}°C.")
else:
    print("Invalid unit. Please enter either 'C' or 'F'.")