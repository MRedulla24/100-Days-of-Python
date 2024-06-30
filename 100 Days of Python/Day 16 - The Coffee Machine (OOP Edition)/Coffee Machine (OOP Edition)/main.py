# Coffee Machine (OOP Edition)
# By Marco Redulla
# Day 16 (27/06/2024)
import os

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

on = True

coffee_machine = CoffeeMaker()
menu_list = Menu()
money_machine = MoneyMachine()

os.system('cls')
while on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        coffee_machine.report()
        money_machine.report()
    elif choice == "off":
        on = False
    else:
        coffee = menu_list.find_drink(choice)
        if coffee:
            if coffee_machine.is_resource_sufficient(coffee):
                if money_machine.make_payment(coffee.cost):
                    coffee_machine.make_coffee(coffee)