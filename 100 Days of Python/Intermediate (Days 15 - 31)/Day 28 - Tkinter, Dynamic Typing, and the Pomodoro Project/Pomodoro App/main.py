# Pomodoro Timer
# By Marco Redulla
# Day 28 (16/07/2024)
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TOMATO_FILEPATH = r"100 Days of Python\Intermediate (Days 15 - 31)\Day 28 - Tkinter, Dynamic Typing, and the Pomodoro Project\Pomodoro App\tomato.png"

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def update(text):
    canvas.itemconfigure(time, text=text)

def reset():
    window.after_cancel(timer)
    update(text="00:00")
    status.config(text="Timer", fg=GREEN)
    checkmark["text"] = ""
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        status.config(text="Break", fg=RED)
        countdown(LONG_BREAK_MIN* 25)
        return
    elif reps % 2 == 1:
        status.config(text="Work", fg=GREEN)
        countdown(WORK_MIN * 60)
    else:
        status.config(text="Break", fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global reps
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec % 60}"
    update(text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        checkmark["text"] = "✔" * (reps//2)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

# Set Status
status = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
status.grid(column=1,row=0)

# Set Tomato
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file=TOMATO_FILEPATH)

canvas.create_image(100, 112, image=tomato_img)
time = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

# Start Button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0,row=2)

# Reset Button
reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=2,row=2)

# Checkmarks
checkmark = Label(fg=GREEN, bg=YELLOW)
checkmark.grid(column=1,row=3)


window.mainloop()