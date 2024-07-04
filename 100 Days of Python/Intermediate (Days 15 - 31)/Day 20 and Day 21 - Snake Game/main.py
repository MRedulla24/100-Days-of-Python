# Snake Game
# By Marco Redulla
# Day 20 (04/07/2024)
from turtle import Turtle, Screen
from time import sleep
from snake import Snake

screen = Screen()
screen.setup(height = 600, width = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# initialize snake
snake = Snake()

segments = []



screen.listen()
screen.update()
game_is_on = True

while game_is_on:
    screen.update()
    sleep(0.1)
    
    screen.onkeypress(key = "w", fun = snake.move_up)
    screen.onkeypress(key = "a", fun = snake.move_left)
    screen.onkeypress(key = "s", fun = snake.move_down)
    screen.onkeypress(key = "d", fun = snake.move_right)
    
    snake.move()

    # movement commands
    

screen.exitonclick()