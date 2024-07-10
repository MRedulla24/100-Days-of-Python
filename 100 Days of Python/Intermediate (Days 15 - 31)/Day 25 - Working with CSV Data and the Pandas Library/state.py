from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")
class State(Turtle):
    def __init__(self, name, pos):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(pos)
        self.write(arg = name, align = ALIGNMENT, font = FONT)
