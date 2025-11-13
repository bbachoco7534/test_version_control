import random

print("Welcome to Rock-Paper-Scissors!")

choices = ["rock", "paper", "scissors"]

player_input = input("Choose rock, paper, or scissors: ").lower()

print(f"You chose: {player_input} ")

print("Computer: " + random.choice(choices))
