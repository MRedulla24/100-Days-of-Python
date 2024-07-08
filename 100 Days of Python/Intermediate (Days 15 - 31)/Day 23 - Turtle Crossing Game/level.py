from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
POS = (-220, 250)
class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1    
        self.hideturtle()
        self.penup()
        self.goto(POS)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(arg = f"Level: {self.level}", align = ALIGNMENT, font = FONT)

    def increment(self):
        self.level += 1
        self.update_level()
    
    def game_over(self):
        self.goto((0,0))
        self.write(arg = "GAME OVER.", align = ALIGNMENT, font = FONT)