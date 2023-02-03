#!/usr/bin/env python3
"""Creating multiple objects(turtles) in the same program"""
import turtle as t


screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
color = ["red", "pink", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]

for turtles in range(0, 6):
    tom = t.Turtle(shape="turtle")
    tom.speed("fastest")
    tom.color(color[turtles])
    tom.penup()
    tom.goto(x=-230, y=y_positions[turtles])


screen.exitonclick()
