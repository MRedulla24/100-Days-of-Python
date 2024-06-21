# Calculator
# By Marco Redulla
# Day 10 (21/06/2024)
import calculator_art
import os

def second(first_number):
    operation = input("Pick an operation: ")

    if operation not in ["+","-","*","/"]:
        retry = input("Invalid operation. Try again? (y/n): ").lower()
        if retry == 'y':
            second(first_number)

    else:
        second_number = float(input("What is the second number?: "))
        string = f"{str(first_number)} {operation} {str(second_number)}"
        result = eval(string)
        print(f"{string} = {result}")
        restart = input(f"Type 'y' to continue calculating with {result}, or else type 'n' to start a new calculation: ").lower()
        if restart == "y":
            os.system("cls")
            print(calculator_art.logo)
            print(f"Previous number: {result}")
            second(result)
        else:
            os.system("cls")
            first()

def first():
    print(calculator_art.logo)
    first_number = float(input("What is the first number?: "))
    print("+\n-\n*\n/")
    second(first_number)

first()