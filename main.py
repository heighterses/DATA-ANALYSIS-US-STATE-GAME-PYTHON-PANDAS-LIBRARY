import turtle, pandas

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("Data-Analysis-US-States-Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = []
counter = 0

for answer in range(50):
    answer_in = screen.textinput(title=f"{counter + 1 } / 50 Guess the State", prompt="What's the next state").title()
    if answer_in in data["state"].tolist():
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_d = data[data.state == answer_in]
        t.goto(int(state_d.x), int(state_d.y))
        t.write(state_d.state)
        states.append(answer_in)
        counter += 1
        print(data[data.state == answer_in])

    else:
        print("irrelevant entry")

screen.exitonclick()