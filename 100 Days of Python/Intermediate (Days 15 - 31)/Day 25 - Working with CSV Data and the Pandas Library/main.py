# States Guessing Game
# By Marco Redulla
# Day 20 (10/07/2024)
import os
import pandas as pd
import turtle
import string
from state import State

# filepaths
CSV_PATH = r"100 Days of Python\Intermediate (Days 15 - 31)\Day 25 - Working with CSV Data and the Pandas Library\50_states.csv"
IMAGE = r"100 Days of Python\Intermediate (Days 15 - 31)\Day 25 - Working with CSV Data and the Pandas Library\blank_states_img.gif"

# initializing data
dataframe = pd.read_csv(CSV_PATH)
state_list = dataframe.state.to_list()
correct_states = []

screen = turtle.Screen()
screen.setup(width=725, height=491)

screen.addshape(IMAGE)
turtle.shape(IMAGE)

initial = True
print(state_list)
while correct_states != len(state_list):
    TITLE = f"{len(correct_states)}/{len(state_list)} States Correct"

    if initial:
        answer = string.capwords(screen.textinput(title=TITLE, prompt="What's a state's name?"))
    else:
        answer = string.capwords(screen.textinput(title=TITLE, prompt="What's another state's name?"))

    if answer == "Exit":
        # creates list of states to learn
        incorrect_states = [state for state in state_list if state not in correct_states]
        new_data = pd.DataFrame(incorrect_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in state_list:
        initial = False
        correct_states.append(answer)

        x,y =  dataframe.iloc[state_list.index(answer), [1,2]]
        new_state = State(name=answer, pos=(x,y))
