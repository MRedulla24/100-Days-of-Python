# Number Guessing Game
# By Marco Redulla
# Day 12 (23/06/2024)
import guessing_game_art
import random
import os

def restart(prompt):
    retry = input(f"{prompt} Type 'y' or 'n'. ").lower()
    if retry == 'y':
        guessing_game()
    else:
        return

def guessing_game():
    os.system('cls')

    print(guessing_game_art.logo)
    print("\nWelcome to the number guessing game!")
    print("I'm thinking of a number between 1  and 100.")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard'. ").lower()
    if difficulty == 'easy':
        lives = 10
    elif difficulty == 'hard':
        lives = 5
    else:
        restart("Invalid choice. Try again?")
        return
    
    answer = random.randint(1,100)
    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == answer:
            restart(f"You got it right! The number was {answer}. Do you want to play again?")
            return
        elif guess < answer:
            print("Too low.")
        else:
            print("Too high.")
        lives -= 1
        if lives > 0:
            print("Guess again.")
            
    if lives == 0:
        restart(f"You lost. The number was {answer}. Do you want to play again?")
        return

guessing_game()
