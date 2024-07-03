# Etch-A-Sketch
# By Marco Redulla
# Day 19 (03/07/2024)
from turtle import Turtle, Screen

tim = Turtle()

def move_forward():
    tim.fd(10)
def move_backward():
    tim.bk(10)
def move_clockwise():
    tim.seth(tim.heading() + 10)
def move_counter_clockwise():
    tim.seth(tim.heading() - 10)
def clear():
    tim.reset()

screen = Screen()
screen.listen()

screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=move_clockwise)
screen.onkeypress(key="d", fun=move_counter_clockwise)
screen.onkeypress(key="c", fun=clear)

screen.exitonclick()