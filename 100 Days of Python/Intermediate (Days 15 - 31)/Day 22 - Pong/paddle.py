from turtle import Turtle

DISTANCE = 10
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
    
    def move_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + DISTANCE
            self.goto(x = self.xcor(), y = new_y)
    
    def move_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - DISTANCE
            self.goto(x = self.xcor(), y = new_y)
