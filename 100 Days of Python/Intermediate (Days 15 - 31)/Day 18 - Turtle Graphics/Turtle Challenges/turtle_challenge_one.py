# Turtle Challenge 1
# By Marco Redulla
# Day 18 (01/07/2024)

from turtle import Turtle, Screen

# Creates a red turtle
tim = Turtle()
tim.shape("turtle")
tim.color("red")

# Draw a square
for _ in range(4):
    tim.fd(100)
    tim.right(90)


screen = Screen()
screen.exitonclick()