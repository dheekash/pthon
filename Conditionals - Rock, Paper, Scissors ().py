import random

options = ("rock", "paper", "scissors")

computer = options[random.randint(0, 2)]

print("====== Welcome to the game ======")
player = input("Please enter Rock, Paper, or Scissors below:\n")

if player.lower() == computer:
    print("It's a tie! Try again.")
elif player.lower() == "rock":
    if computer == "paper":
        print("You lose! Your opponent chose 'Paper'")
    else:
        print("You win! Your opponent chose 'Scissors'") 
elif player.lower() == "paper":
    if computer == "scissors":
        print("You lose! Your opponent chose 'Scissors'")
    else:
        print("You win! Your opponent chose 'Rock'")
elif player.lower() == "scissors":
    if computer == "rock":
        print("You lose! Your opponent chose 'Rock'")
    else:
        print("You win! Your opponent chose 'Paper'")
else:
    print("Please enter a valid option.")
