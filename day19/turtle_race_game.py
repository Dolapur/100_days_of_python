#!/usr/bin/env python3
import turtle as t
import random


race_on = False
screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
color = ["red", "pink", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for turtles in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.speed("fastest")
    new_turtle.color(color[turtles])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtles])
    all_turtles.append(new_turtle)


if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:                  
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:                             
                print(f"you've won! The {winning_color} turtle is the winner!")  
            else:          
                print(f"you've lost! The {winning_color} turtle is the winner !")

         
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
