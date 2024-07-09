from turtle import Turtle

FILEPATH = r'C:\Users\Intel NUC\Documents\GitHub\100-Days-of-Python\100 Days of Python\Intermediate (Days 15 - 31)\Day 24 - Files, Directories, and Paths\Snake Game Leaderboard\highscore.txt'
ALIGNMENT = "center"
FONT = ("Courier" , 20, "normal")
SCORE_INCREMENT = 1

with open(FILEPATH, "r") as file:
    HIGHSCORE = int(file.read())

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = HIGHSCORE
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x = 0, y = 260)
        self.score_update()
    
    ## Original score_update code (Day 20 and 21)
    # def score_update(self):
    #     self.clear()
    #     self.write(arg = f"Score: {self.score}", align = ALIGNMENT, font = FONT)

    ## New score_update code for Day 24
    def score_update(self):
        self.clear()
        self.write(arg = f"Current Score: {self.score} High Score: {self.highscore}", align = ALIGNMENT, font = FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(FILEPATH, "w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.score_update()
    
    def game_over(self):
        self.goto(x = 0, y = 0)
        self.write(arg = f"Game Over", align = ALIGNMENT, font = FONT)
        
    def increment(self):
        self.score += SCORE_INCREMENT
        self.score_update()
        