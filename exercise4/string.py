# validate user input 1) No more than 10 characters, 2) No numbers allowed
#  3) No special characters allowed and digits
# 4) Must no contain spaces
username = input("Enter a username: ")
if len(username) > 10:
    print("Error; Username cannot have more than 10 characters.")
elif not username.isalpha(): #checks if every character is a letter
    print("Error: Username cannot contain numbers.")
elif not username.isalnum(): #checks if every character is a number
    print("Error: Username cannot contain special characters.")
elif " " in username: #checks if there is blank character
    print("Error: Username cannot contain spaces.") 
else:
    print(f"Hello {username}!, welcome to the program.")
    
