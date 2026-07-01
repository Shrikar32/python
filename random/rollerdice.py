# Write a Python program that simulates rolling one or more six-sided dice.

# Requirements
# Display a welcome message.
# Ask the user how many dice they would like to roll.
# Generate a random value between 1 and 6 for each die.
# Display each die using ASCII art.
# Display the numerical value of each die.
# Calculate and display the total of all dice rolled.
import random
import time
#● ┌ ─ ┐ │ └ ┘
print("Welcome to Dice roller program !!! ")
dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),

    2: (
        "┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"
    ),

    3: (
        "┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"
    ),

    4: (
        "┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"
    ),

    5: (
        "┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"
    ),

    6: (
        "┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"
    )
}
while True:
    roll = input("Enter how many dice would you like to roll: ")

    if roll.isdigit():
        roll = int(roll)

        if roll > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    else:
        print("That is not a valid number. Please enter a whole number.")
total = 0

for i in range(roll):
    number = random.randint(1, 6)
    total += number

    print(f"\nDie {i + 1} rolled: {number}")

    for line in dice_art[number]:
        time.sleep(1)
        print(line)

print(f"\nTotal = {total}")

        
