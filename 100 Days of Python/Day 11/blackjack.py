# Blackjack
# By Marco Redulla
# Day 11 (22/06/2024)
import blackjack_art
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def start():
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n'. ").lower()
    if play == 'y':
        os.system('cls')
        blackjack()

def tally(player_cards, computer_cards):
    print(f"Your final cards: {player_cards}, final total: {sum(player_cards)}")
    print(f"Computer's final cards: {computer_cards}, final total: {sum(computer_cards)}")

    if sum(player_cards) > 21:
        print("You went over. You lost.")
    elif sum(computer_cards) > 21:
        print("The dealer went over. You won!")
    elif sum(player_cards) == sum(computer_cards):
        print("It's a draw.")
    elif sum(player_cards) > sum(computer_cards):
        print("You won!")
    else:
        print("You lost.")

def blackjack():
    print(blackjack_art.logo)

    player_cards = [random.choice(cards) for _ in range(2)]
    computer_cards = [random.choice(cards) for _ in range(2)]

    print(f"Your cards: {player_cards}, current total: {sum(player_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

    hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    while hit == 'y':
        player_cards.append(random.choice(cards))
        if sum(player_cards) > 21:
            tally(player_cards, computer_cards)
            start()
        else:
            hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    
    computer_hit = True
    while computer_hit == True:
        computer_cards.append(random.choice(cards))
        if sum(computer_cards) > 21:
            tally(player_cards, computer_cards)
            start()
        computer_hit = random.choice([True, False])
    
    tally(player_cards, computer_cards)
    start()

os.system('cls')
start()