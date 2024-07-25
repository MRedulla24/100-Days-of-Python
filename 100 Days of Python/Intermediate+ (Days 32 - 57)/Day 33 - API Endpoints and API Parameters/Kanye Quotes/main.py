# Kanye Quote Machine
# By Marco Redulla
# Day 32 (25/07/2024)
import requests as req
from tkinter import *


def get_quote():
    res = req.get('https://api.kanye.rest/')
    res.raise_for_status()
    canvas.itemconfig(quote_text, text=res.json()['quote'])



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=r"100 Days of Python\Intermediate+ (Days 32 - 57)\Day 33 - API Endpoints and API Parameters\Kanye Quotes\background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=r"100 Days of Python\Intermediate+ (Days 32 - 57)\Day 33 - API Endpoints and API Parameters\Kanye Quotes\kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()