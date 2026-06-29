# Number Guessing Game
import random

lowest_val = 1
highest_value = 100
answer = random.randint(lowest_val, highest_value)

is_running = True
guesses = 0

print("Welcome to the Number Guessing Game!")

while is_running:
    guess = input(f"Enter a number between {lowest_val} and {highest_value}: ")

    if guess.isdigit():
        guess = int(guess)

        if guess < lowest_val or guess > highest_value:
            print("Invalid guess! Please stay within the range.")

        else:
            guesses += 1

            if guess > answer:
                print("Guess Lower!")

            elif guess < answer:
                print("Guess Higher!")

            else:
                print(f"Correct! The number was {answer}.")
                print(f"You guessed it in {guesses} attempts.")
                is_running = False

    else:
        print("Invalid input! Please enter a whole number.")