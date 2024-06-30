# Coffee Machine Project
# By Marco Redulla
# Day 15 (26/06/2024)
import os
from menu import MENU
from resources import resources


def order_up(coffee):
    ingredients = MENU[coffee]['ingredients']

    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return 0
        
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    money = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    if money < MENU[coffee]['cost']:
        print("Sorry, that's not enough money. Money refunded.")
        return 0
    else:
        for item in ingredients:
            resources[item] -= ingredients[item]
        change = round(money - MENU[coffee]['cost'], 2)

        if change > 0:
            print(f"Here is ${change} dollars in change.")
        print(f"Here is your {coffee}. Enjoy!")
    return 1

on = True
profit = 0
while on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'report':
        print(f"Water: {resources['water']}mL")
        print(f"Milk: {resources['milk']}mL")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice == 'off':
        on = False
    elif choice == 'refill':
        for item in resources:
            try:
                resources[item] += int(input(f"How much {item} will you refill?: "))
            except:
                print("Error. Please put a valid integer.")
    elif choice in ['espresso', 'latte', 'cappuccino']:
        if order_up(choice) == 1:
            profit += MENU[choice]['cost']
    else:
        print("That is not a valid option. Try again.")