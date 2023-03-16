#!/usr/bin/env python3
'''Draw  diffrent shapes repeatedly using turtle python'''
from turtle import Turtle, Screen

tommy = Turtle()
tommy.shape("turtle")
tommy.color("green")

def draw_shape(num_of_side):
    angle = 360 / num_of_sides
    for _ in range(num_oof_sides):
        tommy.forward(100)
        tommy.right(angle)

for shape_sides in range(3, 11):
    draw_shape(shape_sides)


screen = Screen()
screen.exitonclick()
