from turtle import Turtle
from random import randint

class Car(Turtle):
    def __init__(self, first = False):
        super().__init__()
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_wid=1, stretch_len=2)
        if first == True:
            self.color((randint(0,255),randint(0,255),randint(0,255)))
            self.goto(x = randint(-280, 280), y = randint(-240, 240))
        else:
            self.reset()
        
    
    def move(self, speed):
        new_x = self.xcor() - speed
        self.goto(x = new_x, y = self.ycor())
    
    def reset(self):
        self.color((randint(0,255),randint(0,255),randint(0,255)))
        self.goto(x = randint(29, 40) * 10, y = randint(-240, 240))