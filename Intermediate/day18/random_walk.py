#!/usr/bin/env python3
"""A random walk using turtle python"""
import random
import turtle as t

tommy = t.Turtle()
directions = [0, 90, 180, 270]
tommy.pensize(13)
tommy.speed("fastest")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color

for _ in range(200):
    tommy.color(random_color())
    tommy.forward(30)
    tommy.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
