from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier New", 30, "normal")
SCORE_INCREMENT = 1
class Scoreboard(Turtle):
    def __init__(self,number, pos):
        self.number = number
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(pos)
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(arg = f"{self.score}", align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.goto((0,0))
        self.write(f"Game over. Player {self.number} won!")

    def increment(self):
        self.score += SCORE_INCREMENT
        self.score_update()  