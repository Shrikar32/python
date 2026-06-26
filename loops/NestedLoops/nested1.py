rows = int(input("Enter the number of rows: "))
coloums = int(input("Enter the number of coloumns: "))
symbol = input("Enter the symbol you want to use: ")
for x in range(rows):
    for y in range(coloums):
        print(symbol, end = "")
    print(symbol)
