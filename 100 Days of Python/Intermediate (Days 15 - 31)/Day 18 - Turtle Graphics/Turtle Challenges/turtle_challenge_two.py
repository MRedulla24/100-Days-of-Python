# Turtle Challenge 2
# By Marco Redulla
# Day 18 (01/07/2024)

from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("blue")

for _ in range(15):
    tim.down()
    tim.fd(10)
    tim.up()
    tim.fd(10)

screen = Screen()
screen.exitonclick()