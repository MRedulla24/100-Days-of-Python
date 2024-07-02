# Turtle Challenge 3
# By Marco Redulla
# Day 18 (01/07/2024)

from turtle import Turtle, Screen
from random import randint

tim = Turtle()

def generate_polygon(turtle, sides):
    turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
    angle = 360/sides

    for _ in range(sides):
        turtle.fd(100)
        turtle.right(angle)

screen = Screen()
screen.colormode(255)

for i in range(3,11):
    generate_polygon(turtle = tim, sides = i)

screen.exitonclick()