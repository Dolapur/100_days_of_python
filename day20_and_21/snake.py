#!/usr/bin/python3
"""Creating a Snake class"""
import turtle as t


POSITIONS = [(0, 0), (-20, 0), (-40, 0)]                                           
MOVE_POSITION = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake_body()

    def create_snake_body(self):
        for position in POSITIONS:
            obj = t.Turtle("square")
            obj.color("white")
            obj.penup()
            obj.goto(position)
            self.turtles.append(obj)

    def move(self):
        for turt in range((len(turtles) - 1), 0, -1):
            new_x = self.turtles[turt - 1].xcor()
            new_y = self.turtles[turt - 1].ycor()
            self.turtles[turt].goto(new_x, new_y)
        self.turtles[0].forward(MOVE_POSITION)   

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
