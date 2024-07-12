from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I am a label.", font=("Arial", 20, "normal"))
my_label.pack()

my_label["text"] = "New Text"

# Button

def button_click():
    print("I got clicked!")
    my_label["text"] = input.get()

button = Button(text="Click me!", command=button_click)
button.pack()

# Entry
input = Entry(width=10)
input.pack()

window.mainloop()