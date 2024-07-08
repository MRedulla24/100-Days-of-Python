from turtle import Turtle

DISTANCE = 10
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset()

    def reset(self):
        self.goto((0,-280))
    
    def move(self):
        self.forward(DISTANCE)