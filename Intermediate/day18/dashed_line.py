#!/usr/bin/env python3
'''Draw a dashed line using turtle python'''
from turtle import Turtle, Screen

tommy = Turtle()
tommy.shape("turtle")
tommy.color("green")

for _ in range(15):
    tommy.penup()
    tommy.forward(10)
    tommy.pendown()
    tommy.forward(10)

screen = Screen()
screen.exitonclick()
