

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
while len(all_states) < 50:
    user_input = screen.textinput(
        title=f"{len(all_states)}/50 U.s States:", prompt="Enter any state you know")

    for st in states.state:
        if st.lower() == user_input.lower():
            all_states.append(user_input)
            x_cor = int(states[states.state == st].x)
            y_cor = int(states[states.state == st].y)
            coor = (x_cor, y_cor)
            result.goto(coor)
            result.write(f"{user_input}")
            


turtle.mainloop()


# function to get coroutines from the screen
# def get_coor(x, y):
#     with open("coor.txt", "w") as f:
#         x_cor = str(x)
#         y_cor = str(y)
#         f.write(x_cor)
#         f.write(y_cor)
# turtle.onscreenclick(fun=get_coor)
