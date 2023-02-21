#!/usr/bin/env python3
import turtle


screen = turtle.Screen()
screen.title("U.S States Game")
image = "states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 states Correct", prompt="What's another state's name").title()

    if answer_state == "Exit":
        missing_state = [state for state in all_state if state not in guessed_state]
        new_data =pandas.DataFrame(missing_state)        
        new_data.to_csv("state_to_learn.csv")                
        break
                                             
    if answer_state in all_state:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))        
        t.write(answer_state)
                              

screen.exitonclick()
