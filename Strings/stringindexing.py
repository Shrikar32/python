# String indexing is accessing elements of string using []
# [Start : end : step]
Credit_number = "1234-5678-9012-3450"
print(Credit_number[0]) 
print(Credit_number[5]) 
print(Credit_number[1:10])
print(Credit_number[::2])
print(Credit_number[::-1])
print(Credit_number[-1])
last_digits = Credit_number[-4:-1]
print(f"The last digits of the credit card are : 1234-5678-9012-{last_digits}")
