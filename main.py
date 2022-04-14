

import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States:")
image = "image.gif"
screen.addshape(image)
turtle.shape(image)
result = turtle.Turtle()
result.penup()
result.hideturtle()


states = pandas.read_csv("50_states.CSV")

all_states = []

# checks if all states are correctly entered
while len(all_states) < 50:
    user_input = screen.textinput(
        title=f"{len(all_states)}/50 U.s States:", prompt="Enter any state you know").title()

    if user_input == "Exit":
        break
    for st in states.state:

        # checks if user input matches any of the state in US
        if st == user_input:
            all_states.append(user_input)
            x_cor = int(states[states.state == st].x)
            y_cor = int(states[states.state == st].y)
            coor = (x_cor, y_cor)
            result.goto(coor)
            result.write(f"{user_input}")
            

# creates a file to show all missed states

st_list = states.state.to_list()

missed_states = []
for element in st_list:
    if element not in all_states:
        missed_states.append(element)

pd = pandas.Series(missed_states)
pd.to_csv("Missed States.CSV")
   

