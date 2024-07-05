# Snake Game
# By Marco Redulla
# Day 20 (04/07/2024)
from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height = 600, width = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# initialize classes
snake = Snake()
food = Food()
scoreboard = Scoreboard()

segments = []



screen.listen()
# movement commands
screen.onkeypress(key = "w", fun = snake.move_up)
screen.onkeypress(key = "a", fun = snake.move_left)
screen.onkeypress(key = "s", fun = snake.move_down)
screen.onkeypress(key = "d", fun = snake.move_right)

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15: # set to 15 as a buffer
        food.refresh()
        scoreboard.increment()
        snake.generate_part(pos=snake.get_part(snake.length() - 1).pos())
    
    # detect collision with wall
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        game_is_on = False
        scoreboard.game_over()

    #detect collision with tail
    for seg in snake.segments[1::]:
        if snake.head.distance(seg) == 0:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()