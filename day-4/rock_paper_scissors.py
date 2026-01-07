# Day 4 - Rock Paper Scissors Game
# Topics covered:
# - Random Module
# - Understanding Offset and Appending Items to Lists
# - IndexErrors and Working with Nested Lists

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
choices = ["Rock", "Paper", "Scissors"]

print("Welcome to Rock Paper Scissors!")
print("=" * 35)

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n")

# Validate user input
if not user_choice.isdigit() or int(user_choice) not in [0, 1, 2]:
    print("Invalid input! Please enter 0, 1, or 2.")
else:
    user_choice = int(user_choice)
    computer_choice = random.randint(0, 2)
    
    print(f"\nYou chose {choices[user_choice]}:")
    print(game_images[user_choice])
    
    print(f"Computer chose {choices[computer_choice]}:")
    print(game_images[computer_choice])
    
    # Determine the winner
    print("=" * 35)
    if user_choice == computer_choice:
        print("It's a draw! 🤝")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win! 🎉")
    else:
        print("You lose! 😢")