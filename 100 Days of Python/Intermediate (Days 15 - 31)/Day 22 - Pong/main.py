# Pong Game
# By Marco Redulla
# Day 20 (04/07/2024)
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

from time import sleep

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

partition = Turtle()
partition.hideturtle()
partition.color("white")
partition.penup()
partition.goto((0, 290))
partition.setheading(270)

for _ in range(12):
    partition.pendown()
    partition.fd(25)
    partition.penup()
    partition.fd(25)

# initialize elements
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

r_score = Scoreboard(2, (20, 250))
l_score = Scoreboard(1, (-20, 250))

screen.listen()

screen.onkeypress(key = "Up", fun = r_paddle.move_up)
screen.onkeypress(key = "Down", fun = r_paddle.move_down)

screen.onkeypress(key = "w", fun = l_paddle.move_up)
screen.onkeypress(key = "s", fun = l_paddle.move_down)

#if ever you randomly press all caps
screen.onkeypress(key = "W", fun = l_paddle.move_up)
screen.onkeypress(key = "S", fun = l_paddle.move_down)

game_is_on = True
ball_hitcount = 0
game_speed = 0.05
allow = 1
while game_is_on:
    sleep(game_speed)
    screen.update()

    # Check ball hitcount for speed increase
    if ball_hitcount in [10,20,30,40] and game_speed > 0.01 and allow == 1:
        game_speed -= 0.01
        allow = 0

    # Check if ball goes past paddles
    if ball.xcor() > 400:
        ball_hitcount = 0
        game_speed = 0.05
        ball.reset("left")
        l_score.increment()
        if l_score.score == 7:
            l_score.game_over()
            game_is_on = False
    elif ball.xcor() < -400:
        ball_hitcount = 0
        game_speed = 0.05
        ball.reset("right")
        r_score.increment()
        if r_score.score == 7:
            r_score.game_over()
            game_is_on = False
    
    # Detect collision with wall
    if abs(ball.ycor()) > 290:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()
        ball_hitcount += 1
        allow = 1
    
    # Detect collision with left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        ball_hitcount += 1
        allow = 1

    ball.move()
screen.exitonclick()