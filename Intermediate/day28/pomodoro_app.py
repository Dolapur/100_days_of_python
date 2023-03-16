#!/usr/bin/env python3

from tkinter import *
import time
import math


# CONSTANTS
PINK = "#FF449F"
RED = "#BF1363"
GREEN = "#1eae98"
YELLOW = "#fff5b7"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 1
reps  = 0
timer = None

# TIMER RESET
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer",fg=GREEN)
    check_label.config(text='')
    global reps
    reps = 0
    
# TIMER MECHANISM
def work():
    countdown(WORK_MIN * 60)    
    timer_label.config(text="Work", fg=GREEN)

def short_break():
    countdown(SHORT_BREAK_MIN * 60)
    timer_label.config(text="Break", fg=PINK)
    
def long_break():
    countdown(LONG_BREAK_MIN * 60)
    timer_label.config(text="Break", fg=RED)
    
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        long_break()
    elif reps % 2 == 0:
        short_break()
    else:
        work()
                                                                                                                           
# COUNTDOWN MECHANISM
def countdown(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"                                                                                                                                             
    canvas.itemconfig(timer_text, text = f"{minutes}:{seconds}")
    
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        num_check = math.floor(reps / 2)
        for _ in range(num_check):
            marks += "✔"
        check_label.config(text=marks)

window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg=YELLOW)                                                                                                                                                                        
                            
canvas = Canvas(width=200, height=224)
canvas.config(bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

check_label = Label(bg = YELLOW, fg = GREEN, font = (FONT_NAME, 15, 'normal'))

timer_label = Label(text = "Timer", bg = YELLOW, fg = GREEN, font = [FONT_NAME, 35, 'bold'])

# Button
start_button = Button(text = "Start", highlightthickness=0, command=start_timer)
reset_button = Button(text = 'Reset', highlightthickness=0, command=reset_timer)

# Layout
timer_label.grid(row = 0, column = 1)
canvas.grid(row = 1, column = 1)
start_button.grid(row = 2, column = 0)
reset_button.grid(row = 2, column=2)
check_label.grid(row=3, column=1)


window.mainloop()
