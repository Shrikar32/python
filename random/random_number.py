import random

# number = random.randint(1, 20)  # Generates a random integer between 1 and 20
# print(number)

# low = 1
# high = 100
# number = random.randint(low, high)  # Generates a random integer between low and high
# print(number)

# choices = ("Rock", "Paper", "Scissors")
# options = random.choice(choices)  # Selects one random item from the tuple
# print(options)

# Shuffle the cards into a random order
cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
random.shuffle(cards)
print(cards)