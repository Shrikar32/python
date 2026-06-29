import random
import time

choices = ("rock", "paper", "scissors")

print("Welcome to the Rock-Paper-Scissors Game!")
print("First to 3 points wins!")

points = 0
computer_points = 0
game = True

while game:

    computer = random.choice(choices)

    player = input("Enter your choice (Rock, Paper or Scissors): ").lower()

    if player not in choices:
        print("Invalid input! Please enter Rock, Paper or Scissors.")
        continue

    print(f"\nYour choice: {player.capitalize()}")

    print("Computer's choice will be displayed in...")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    print(f"Computer chose: {computer.capitalize()}")

    if player == computer:
        print("Draw!")

    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):

        print("Player wins this round!")
        points += 1

    else:
        print("Computer wins this round!")
        computer_points += 1

    print(f"\nScore")
    print(f"Player: {points}")
    print(f"Computer: {computer_points}")

    if points == 3 or computer_points == 3:

        print("\nGame Over!")

        if points == 3:
            print("🎉 Congratulations! You won the game!")
        else:
            print("💻 Computer won the game!")

        play_again = input("\nDo you want to play again? (y/n): ").lower()

        if play_again == "y":
            points = 0
            computer_points = 0
            print("\nStarting a new game...\n")
        else:
            print("Thanks for playing!")
            game = False