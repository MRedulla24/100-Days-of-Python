# Miles to Kilometers Converter
# By Marco Redulla
# Day 27 (12/07/2024)
from tkinter import *

def convert():
    converted["text"] = float(input.get()) * 1.609

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300,height=100)

input = Entry(width=10)
input.grid(column=1,row=0)

miles = Label(text="Miles")
miles.grid(column=2,row=0)

equal_to = Label(text="is equal to")
equal_to.grid(column=0,row=1)

converted = Label(text=0)
converted.grid(column=1,row=1)

km = Label(text="Km")
km.grid(column=2,row=1)

calculate = Button(text="Calculate", command=convert)
calculate.grid(column=1,row=2)

window.mainloop()