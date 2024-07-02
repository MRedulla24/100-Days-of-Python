# Hirst Painting
# By Marco Redulla
# Day 18 (01/07/2024)
from turtle import Turtle, Screen
import random
import colorgram

IMAGE_PATH = '100 Days of Python\Intermediate (Days 15 - 31)\Day 18 - Turtle Graphics\Hirst Painting\hirst_painting.jpeg'
colors = colorgram.extract(IMAGE_PATH, 30)

color_list = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]


pen = Turtle()
pen.pensize(10)
pen.hideturtle()
pen.speed('fastest')

length = 10
height = 10
gap = 50

pen.up()
pen.setheading(220)
pen.fd(300)
pen.setheading(0)
pen.down()

def generate_row(length, gap, color_list):
    count = 0
    while count < length:
        pen.down()
        pen.dot(20, random.choice(color_list))
        pen.up()
        count += 1
        if count < length:
            pen.fd(gap)

screen = Screen()
screen.colormode(255)

for i in range(height):
    generate_row(length = length, gap = gap, color_list = color_list)
    if i % 2 == 0:
        pen.left(90)
        pen.fd(gap)
        pen.left(90)
    else:
        pen.right(90)
        pen.fd(gap)
        pen.right(90)


screen.exitonclick()