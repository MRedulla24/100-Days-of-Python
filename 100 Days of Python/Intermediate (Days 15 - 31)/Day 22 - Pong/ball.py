from turtle import Turtle
from random import randint

DISTANCE = 10
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.reset("right")
    
    def move(self):
        self.fd(DISTANCE)
        
    def adjust(self):
        self.setheading(self.current_heading)
        self.settiltangle(-self.current_heading)

    def reset(self, direction):
        self.goto((0,0))
        if direction == "right":
            self.current_heading = randint(2,16) * 5 
        elif direction == "left":
            self.current_heading = randint(20,43) * 5
        self.adjust()

    def bounce_y(self):
        self.current_heading *= -1
        self.adjust()
    
    def bounce_x(self):
        self.current_heading = 180 - self.current_heading
        self.adjust()