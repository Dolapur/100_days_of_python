#!/usr/bin/env python3
"""Draw a spirograph using turtle python"""
import random
import turtle as t


tommy = t.Turtle()
tommy.speed("fastest")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


def draw_spirograph(sizes):
    for _ in range(int(360 / sizes)):
        tommy.color(random_color())
        tommy.circle(100)
        tommy.setheading(tommy.heading() + 10)
        tommy.circle(100)


draw_spirograph(6)

screen = t.Screen()
screen.bgcolor("black")
screen.exitonclick()
