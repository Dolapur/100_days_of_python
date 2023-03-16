#!/usr/bin/python3
"""Animate the snake body"""
import turtle as t
import time


screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=400)
screen.title("My Snake Game")
screen.tracer(0)

positions = [(0, 0), (-20, 0), (-40, 0)]
turtles = []

for position in positions:
    obj = t.Turtle("square")
    obj.color("white")
    obj.penup()
    obj.goto(position)
    turtles.append(obj)


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for turt in range((len(turtles) - 1), 0, -1):
        new_x = turtles[turt - 1].xcor()
        new_y = turtles[turt - 1].ycor()
        turtles[turt].goto(new_x, new_y)
    turtles[0].forward(20)


screen.exitonclick()    
