# Higher or Lower
# By Marco Redulla
# Day 14 (25/06/2024)

import art
import game_data
import random
import os

game_data = game_data.data

def game():
    
    score = 0
    correct = True

    while correct == True:
        if score > 0:
            print(f"Correct! Your current score is now {score}.")

        if score == 0:
            A = random.choice(game_data)

        B = random.choice(game_data)

        # safety check whenever B == A
        while B == A:
            B = random.choice(game_data)

        A_follow, B_follow = [A['follower_count'], B['follower_count']]
                
        if A_follow > B_follow:
            answer = 'A'
        else:
            answer = 'B'

        print(f"Compare A: {A['name']}, a {A['description']} from {A['country']}.")
        print(f"\n{art.vs}\n")
        print(f"Compare B: {B['name']}, a {B['description']} from {B['country']}.")
        choice = input("Who has more followers? Type 'A' or 'B'. ").upper()

        while choice != 'A' and choice != 'B':
            print("That is not a choice. Try again.")
            choice = input("Who has more followers? Type 'A' or 'B'. ").upper()
                
        if choice == answer:
            score += 1
            A = B
        else:
            correct = False
        os.system('cls')
    print(f"Sorry, that's wrong. Your final score is {score}.")
    retry = input("Do you want to play again? Type 'y' or 'n'. ").lower()
    if retry == 'y':
        os.system('cls')
        game()    

def start():
    os.system('cls')
    print(art.logo)
    print("Welcome to Higher or Lower! Do you want to play?")
    play = input("Type 'y' or 'n'. ").lower()
    if play == 'y':
        os.system('cls')
        game()


start()