# Tip Calculator
# By Marco Redulla
# Day 2 (13/06/2024)

def tip_calculator():
    print("Welcome to the tip calcualtor!")

    total_bill = float(input("How much was the total bill? $"))
    tip = int(input("What much tip would you like to give? 10, 12, or 15? "))

    if tip not in [10, 12, 15]:
        print("Tips should only be 10, 12, or 15. Try again.\n")
        tip_calculator()
    else:
        people = int(input("How many people to split the bill? "))
        split_bill = "{:.2f}".format(round((1 + (tip/100)) * total_bill/people, 2))
        
        print(f"Each person should pay: ${split_bill}")

tip_calculator()

