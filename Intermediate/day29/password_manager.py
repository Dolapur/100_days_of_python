#!/usr/bin/env python3
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# CONSTANTS
FONT_NAME = "Courier"

#-----------GENERATE PASSWORD------------
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l',    
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    passwd_letters = [choice(letters) for _ in range(randint(8, 10))]    
    passwd_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    passwd_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    passwd_list = passwd_symbols + passwd_numbers + passwd_letters
    shuffle(passwd_list)
    password = "".join(passwd_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    
#-------------SAVE BUTTON SETUP---------------

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Warning", message="Please do not leave the fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the messages entered: \nEmail: {email}"                                                      f"\nPassword: {password}\nIs it okay to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                email_entry.delete(0, END)

#-------------UI SETUP----------
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

canvas = Canvas(width=200, height=200)
canvas.config(highlightthickness=1, highlightcolor="black")
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

#labels
website_label = Label(text = "Website", font = (FONT_NAME, 15, 'normal'))
email_label = Label(text = "Email", font = (FONT_NAME, 15, 'normal'))
password_label = Label(text = "Password", font = (FONT_NAME, 15, 'normal'))

#entries
website_entry = Entry(width=51)
email_entry = Entry(width=51)
password_entry = Entry(width=33)

# Button
generate_passwd_button = Button(text = "Generate Password", width=14)
add_button = Button(text = 'Add', width=43, command=save)

# Layout
canvas.grid(row = 0, column = 1)
website_label.grid(row=1, column=0)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "example@gmail.com")
password_label.grid(row=3, column=0, columnspan=1)
password_entry.grid(row=3, column=1)
generate_passwd_button.grid(row=3,  column=2)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
