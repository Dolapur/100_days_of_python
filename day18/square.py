#!/usr/bin/env python3
"""Draw a square using turtle python"""
from turtle import Turtle, Screen

tommy = Turtle()
tommy.shape("turtle")
tommy.color("green")

for _ in range(4):
    tommy.forward(100)
    tommy.right(90)

screen = Screen()
screen.exitonclick

