# Turtle Challenge 4
# By Marco Redulla
# Day 18 (01/07/2024)

from turtle import Turtle, Screen
from random import randint

tim = Turtle()
tim.speed("fastest")
tim.pensize(15)

def walk(turtle):
    turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
    turtle.setheading(randint(0,3) * 90)
    turtle.fd(50)

screen = Screen()
screen.colormode(255)

for _ in range(500):
    walk(turtle = tim)

screen.exitonclick()