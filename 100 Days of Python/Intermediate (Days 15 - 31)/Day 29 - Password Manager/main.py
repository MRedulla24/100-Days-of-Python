# Password Generator
# By Marco Redulla
# Day 29 (16/07/2024)
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)


    selected_letters = [random.choice(letters) for _ in range(nr_letters)]
    selected_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    selected_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    characters = selected_letters + selected_numbers + selected_symbols
    random.shuffle(characters)

    password = ''.join(characters)

    pyperclip.copy(password)
    
    password_prompt.insert(index=0, string=password)
    confirm["text"] = "Random password has been generated"

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_prompt.get()
    user = user_prompt.get()
    password = password_prompt.get()

    details = {"website": website, "user": user, "password": password}
    empty = []
    for key in details:
        if len(details.get(key)) == 0:
            empty.append(key)

    if len(empty) == 1:
        messagebox.showinfo(title="Error", message=f"The {empty} field is not completed. Please complete all fields.")
        return
    elif len(empty) > 1:
        messagebox.showinfo(title="Error", message=f"The {', '.join(empty[:-1])}, & {empty[-1]} fields are not completed. Please complete all fields.")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered\nEmail: {user} \nPassword: {password} \n\nIs it okay to save?")
    
    if is_ok:
        with open(FILEPATH, "a") as file:
            file.write(f"website: {website} | user: {user} | password: {password}\n")
    
        website_prompt.delete(0,END)
        password_prompt.delete(0,END)

        confirm["text"] = f"Password for {website} has been added!"

# ---------------------------- UI SETUP ------------------------------- #
PADLOCK_FILEPATH = r"100 Days of Python\Intermediate (Days 15 - 31)\Day 29 - Password Manager\logo.png"
FILEPATH = r"100 Days of Python\Intermediate (Days 15 - 31)\Day 29 - Password Manager\data.txt"


window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

padlock_image = PhotoImage(file=PADLOCK_FILEPATH)
canvas = Canvas(width=200,height=200)
canvas.create_image(100, 100, image=padlock_image)
canvas.grid(column=1,row=0)

# Labels
website_text = Label(text="Website:")
website_text.grid(column=0, row=1)

user_text = Label(text="Email/Username:")
user_text.grid(column=0, row=2)

password_text = Label(text="Password:")
password_text.grid(column=0, row=3)

# Prompts
website_prompt = Entry(width=35)
website_prompt.grid(column=1, row=1, columnspan=2)
website_prompt.focus()

user_prompt = Entry(width=35)
user_prompt.grid(column=1, row=2, columnspan=2)
user_prompt.insert(index=0, string="test.email@gmail.com")

password_prompt = Entry(width=21)
password_prompt.grid(column=1, row=3)

# Generate Password Button
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

# Add button
add = Button(text="Add", command=save, width=36)
add.grid(column = 1, row = 4, columnspan=2)

# Confirmation text
confirm = Label()
confirm.grid(column = 1, row = 5, columnspan = 2)

window.mainloop()