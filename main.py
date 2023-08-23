import turtle, pandas
data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("Data-Analysis-US-States-Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


for answer in range(50):
    answer_in = screen.textinput(title="Guess the State", prompt="What's the next state").lower()
    print(answer_in)

turtle.mainloop()
