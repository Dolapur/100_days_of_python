#!/usr/bin/python3
"""Creating a Snake Game"""
import turtle as t
import time
from snake import Snake


screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=400)
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick
