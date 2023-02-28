from tkinter import *

# What is GUI?
# Graphical User Interface -> important, because its predecessor is Command Line Interface
# Windows -> first GUI by Microsoft, led conflict with Apple (mac lisa), when both of them stole it from Xeroc
# Xerox Parc -> the first creator of GUI, OOP, LAN, Mouse
# No longer using CLI or Turtle

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx = 100, pady=200)

#label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")

#button
def button_clicked():
    print("I got clicked")
    my_label.config(text="button clicked")


button = Button(text="click-me", command=button_clicked)
button2 = Button(text="Another Button", command = button_clicked)

my_label.grid(row=0, column = 0)
button.grid(row = 1, column = 1)
button2.grid(row=0, column=2)

window.mainloop()
