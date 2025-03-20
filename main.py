# Now We create snake water gun game in python
'''
1 for Rock
0 for Paper
-1 for Scissor
'''
import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
        (user == "scissors" and computer == "paper") or \
        (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'quit' to exit the game.\n")
    
    while (True):
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        
        if user_choice == "quit":
            print("Thanks for playing!")
            break
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = get_winner(user_choice, computer_choice)
        print(result + "\n")

play_game()
