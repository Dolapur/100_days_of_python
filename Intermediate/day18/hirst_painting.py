#!/usr/bin/env python3
import turtle as t
import random


color_list = [(198, 159, 103), (45, 29, 17), (21, 36, 50), (47, 107, 141), (133, 87, 64), (18, 43, 32), (48, 121, 91), (48, 24, 34), (138, 72, 95), (191, 89, 119), (117, 167, 186), (122, 180, 159), (201, 91, 75), (194, 134, 159), (167, 159, 61), (64, 164, 133), (47, 159, 180), (24, 89, 69), (98, 44, 60), (37, 58, 106), (212, 199, 125), (207, 218, 213), (208, 215, 221), (216, 208, 196), (101, 47, 39), (79, 73, 31), (110, 115, 169), (26, 80, 90), (220, 205, 212), (157, 207, 196), (216, 173, 194), (230, 170, 159), (155, 205, 211), (186, 185, 207), (196, 209, 38)]
tom = t.Turtle()
t.colormode(255)
tom.speed("fastest")
tom.penup()
tom.hideturtle()

tom.setheading(230)
tom.forward(300)
tom.setheading(0)

num_dots = 100
for dots in range(1, (num_dots + 1)):
    tom.dot(15, random.choice(color_list))
    tom.forward(40)

    if dots % 10 == 0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(400)
        tom.setheading(0)


screen = t.Screen()
screen.bgcolor("black")
screen.exitonclick()
