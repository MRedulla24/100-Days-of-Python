# Rock, Paper, Scissors
# By Marco Redulla
# Day 4 (15/06/2024)
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
choices = [rock, paper, scissors]

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

    print(f"You chose: {choices[player_choice]}")

    computer_choice = random.randint(0, len(choices) - 1)
    print(f"Computer chose:\n {choices[computer_choice]}")

    if player_choice == computer_choice:
        print("It's a tie. No one won.")
    elif player_choice == 0:
        if computer_choice == 1:
            print("Paper beats Rock. You lose.")
        else:
            print("Rock beats Scissors. You win!")
    elif player_choice == 1:
        if computer_choice == 2:
            print("Scissors beats Paper. You lose.")
        else:
            print("Paper beats Rock. You win!")
    elif player_choice == 2:
        if computer_choice == 0:
            print("Rock beats Scissors. You lose.")
        else:
            print("Scissors beats Paper. You win!")
    else:
        print("That's not a choice, sorry.")
        
    choice = input("Do you want to play again? (Y/N) ").lower()
    if choice == 'y':
        rock_paper_scissors()

rock_paper_scissors()
    