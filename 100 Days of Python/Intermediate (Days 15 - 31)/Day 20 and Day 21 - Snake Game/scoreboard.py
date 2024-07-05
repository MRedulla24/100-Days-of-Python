from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier" , 24, "normal")
SCORE_INCREMENT = 1

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x = 0, y = 260)
        self.score_update()
    
    def score_update(self):
        self.clear()
        self.write(arg = f"Score: {self.score}", align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.goto(x = 0, y = 0)
        self.write(arg = f"Game Over", align = ALIGNMENT, font = FONT)
        
    def increment(self):
        self.score += SCORE_INCREMENT
        self.score_update()  
        