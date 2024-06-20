# Blind Auction
# By Marco Redulla
# Day 9 (20/06/2024)

import os
import blind_auction_art


bids = []
def add_bid():
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))

    bids.append({"name": name, "bid": bid})
    reset = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if reset == 'yes':
        os.system('cls')
        add_bid()
    else:
        highest_bidder = {"name": None, "bid": 0}
        for bidder in bids:
            if bidder["bid"] > highest_bidder["bid"]:
                highest_bidder = bidder
        os.system('cls')
        print(f"The winner is {highest_bidder['name']} with a bid of ${highest_bidder['bid']}")

print(blind_auction_art.logo)
print("Welcome to the secret auction program.")

add_bid()