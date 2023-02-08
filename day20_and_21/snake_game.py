#!/usr/bin/python3
"""Creating a Snake Game"""
import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard



screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    #Detect collision with food
    if self.head.distance(food) < 12:
        food.refresh()
        snake.extend_obj()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    #Detect collision with snake tail
    for obj in snake.turtles[1:]:
        if snake.head.distance(obj) < 10:
            game_on = False
            scoreboard.game_over()


screen.exitonclick
