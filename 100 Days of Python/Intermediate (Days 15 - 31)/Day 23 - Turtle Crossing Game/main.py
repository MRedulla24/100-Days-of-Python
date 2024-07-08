# Turtle Crossing Game
# By Marco Redulla
# Day 20 (04/07/2024)

# imports
from turtle import Screen
from time import sleep
from random import randint

from player import Player
from level import Level
from car import Car

# game variables
game_is_on = True
GAME_SPEED = 2
SPEED_INCREMENT = 0.2
INITIAL_CAR_COUNT = 20
CAR_INCREMENT = 5

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.colormode(255)
screen.tracer(0)
# initialize objects on screen

player = Player()
level = Level()
cars_list = [Car(first = True) for _ in range(INITIAL_CAR_COUNT)]

# game inputs
screen.listen()
screen.onkeypress(key="w", fun=player.move)
screen.onkeypress(key="W", fun=player.move)



while game_is_on:
    sleep(0.1)
    screen.update()

    for car in cars_list:
        # detect car collision
        if car.distance(player) < 20:
            game_is_on = False
            level.game_over()
        
        # reset car position if reached edge of screen
        if car.xcor() < -290:
            car.reset()

        car.move(GAME_SPEED)
    
    if player.ycor() == 290:
        for _ in range(CAR_INCREMENT):
            new_car = Car()
            cars_list.append(new_car)
        
        player.reset()
        level.increment()
        GAME_SPEED += SPEED_INCREMENT

    
screen.exitonclick()