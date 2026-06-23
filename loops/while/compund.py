# Compound Interest Calculator



Principal = float(input("Enter the amount of money borrowed: "))
while Principal <= 0:
    print("Invalid amount, must be greater than 0.")
    Principal = float(input("Enter the amount of money borrowed: "))
Rate = float(input("Enter the interest rate as a percentage: "))
while Rate < 0:
    print("Invalid rate, must be non-negative.")
    Rate = float(input("Enter the interest rate as a percentage: "))
Time = float(input("Enter the time in years: "))
while Time < 0:
    print("Invalid time, must be non-negative.")
    Time = float(input("Enter the time in years: "))
N = float(input("Enter the number of times the interest is compounded per year: "))
while N <= 0:
    print("Invalid number, must be greater than 0.")
    N = float(input("Enter the number of times the interest is compounded per year: "))

Rate = Rate / 100

Final_amount = Principal * (1 + (Rate / N)) ** (N * Time)

print(f"The final amount after {Time} years is: ₹{Final_amount:.2f}")