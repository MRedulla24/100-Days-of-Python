# Flash Card Application
# By Marco Redulla
# Day 31 (18/07/2024)

# Constants
BACKGROUND_COLOR = "#B1DDC6"
CARD_FRONT_FILEPATH = r"100 Days of Python\Intermediate (Days 15 - 31)\Day 31 - Flash Card App\images\card_front.png"
CARD_BACK_FILEPATH = r"100 Days of Python\Intermediate (Days 15 - 31)\Day 31 - Flash Card App\images\card_back.png"
CHECK_FILEPATH = r"100 Days of Python\Intermediate (Days 15 - 31)\Day 31 - Flash Card App\images\right.png"
CROSS_FILEPATH = r"100 Days of Python\Intermediate (Days 15 - 31)\Day 31 - Flash Card App\images\wrong.png"
TO_LEARN_FILEPATH = r"100 Days of Python\Intermediate (Days 15 - 31)\Day 31 - Flash Card App\data\words_to_learn.csv"

# Imports
from tkinter import *
import pandas as pd
import random

# Card Class
QUESTIONS_FILEPATH = r"100 Days of Python\Intermediate (Days 15 - 31)\Day 31 - Flash Card App\data\french_words.csv"

try:
    french_words = pd.read_csv(TO_LEARN_FILEPATH)
except FileNotFoundError:
    french_words = pd.read_csv(QUESTIONS_FILEPATH)

class Card:
    def __init__(self):
        self.reset()
    
    def reset(self):
        rand_index = random.randint(0, len(french_words) - 1)
        french, english = french_words.iloc[rand_index]
        self.french = french
        self.english = english


# Functions

def flip():
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(question, text=new_card.english)
    wrong.config(state=NORMAL)
    right.config(state=NORMAL)

def countdown():
    wrong.config(state=DISABLED)
    right.config(state=DISABLED)
    window.after(3000, flip)
    
def generate():
    new_card = Card()
    canvas.itemconfig(card, image=card_front_img)
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(question, text=new_card.french)
    countdown()

def incorrect():
    incorrect_words.append([new_card.french, new_card.english])
    to_learn = pd.DataFrame(incorrect_words)
    to_learn.to_csv(TO_LEARN_FILEPATH)

# Main Code

incorrect_words = [["French","English"]]

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

card_front_img = PhotoImage(file=CARD_FRONT_FILEPATH)
card_back_img = PhotoImage(file=CARD_BACK_FILEPATH)

check_img = PhotoImage(file=CHECK_FILEPATH)
cross_img = PhotoImage(file=CROSS_FILEPATH)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# Card
card = canvas.create_image(400,263, image=card_front_img)
new_card = Card()
title = canvas.create_text(400,150, text="French", font=("Arial", 35, "italic"))
question = canvas.create_text(400,263, text=new_card.french, font=("Arial", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong = Button(image=cross_img, highlightthickness=0, bd=0, command=incorrect)
wrong.grid(row=1, column=0)

right = Button(image=check_img, highlightthickness=0, bd=0, command=generate)
right.grid(row=1, column=1)

countdown()

window.mainloop()