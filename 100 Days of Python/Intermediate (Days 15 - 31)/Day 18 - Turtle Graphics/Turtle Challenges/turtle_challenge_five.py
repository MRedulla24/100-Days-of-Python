# Turtle Challenge 5
# By Marco Redulla
# Day 18 (01/07/2024)

from turtle import Turtle, Screen
from random import randint

tim = Turtle()
tim.speed("fastest")


screen = Screen()
screen.colormode(255)

angle = randint(1, 359)

for _ in range(randint(100,300)):
    tim.color(randint(0,255),randint(0,255),randint(0,255))
    tim.circle(100)
    tim.right(angle)

screen.exitonclick()