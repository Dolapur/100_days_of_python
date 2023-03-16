#!/usr/bin/env python3
"""Screen setup and creating the snake body"""
import turtle as t


screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=400)
screen.title("My Snake Game")

positions = [(0, 0), (-20, 0), (-40, 0)]

for position in positions:
    turt= t.Turtle("square")
    turt.color("white")
    turt.goto(position)


screen.exitonclick()
