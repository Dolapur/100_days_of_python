#!/usr/bin/env python3
from turtle import Turtle


ALIGNMENT = 'center'
FONT = ('Courier', 80, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("pink")
        self.penup()
        self.hideturtle()
        self.right_score = 0        
        self.left_score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)
    
    def left_point(self):
        self.left_score += 1        
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()
