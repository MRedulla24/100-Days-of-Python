# Turtle Race
# By Marco Redulla
# Day 19 (03/07/2024)
import os
from turtle import Turtle, Screen
import random

is_race_on = False
os.system('cls')
screen = Screen()
screen.setup(height=400,width=500)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Choose a color: ").lower()

colors = ["red","orange","yellow","green","blue","purple"]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230,y = -70 + turtle_index * 30)
    
    all_turtles.append(new_turtle)

if user_bet in colors:
    is_race_on = True
    print(f"Your bet is on the {user_bet} turtle.")
else:
    print("Invalid Input. Try again.")

while is_race_on:
    distance = random.randint(0,10)
    random_turtle = random.choice(all_turtles)
    random_turtle.forward(distance)

    if random_turtle.xcor() > 230:
        is_race_on = False
        winning_color = random_turtle.pencolor()
        print((f"You lost. The {winning_color} turtle is the winner.", f"You've won! The {winning_color} turtle is the winner!")[winning_color == user_bet])

screen.exitonclick()