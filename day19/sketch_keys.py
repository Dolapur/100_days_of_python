#!/usr/bin/env python3
"""Constructing my sketch keys"""


import turtle as t


tom = t.Turtle()
tom.speed("fastest")

def forwards():
    tom.forward(10)


def backwards():
    tom.backward(10)


def counter_clockwise():
    tom.left(10)


def clockwise():
    tom.right(10)
    

def clear():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


screen = t.Screen()
screen.listen()
screen.onkey(forwards, key="w")
screen.onkey(backwards, key="s")
screen.onkey(counter_clockwise, key="a")
screen.onkey(clockwise, key="d")
screen.onkey(clear, key="c")
screen.exitonclick()
