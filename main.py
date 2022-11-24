import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

state_data = pandas.read_csv('50_states.csv')
timmy = turtle.Turtle()
timmy.penup()
timmy.hideturtle()
score = 0
states = state_data.state
guessed_states = []
while score < 50:
    answer = screen.textinput(title="Guess the State", prompt="What is the name of next state?").title()
    if answer == 'Exit':
        break
    state_row = state_data[state_data['state'] == answer]
    if state_row.empty:
        continue
    # print(state_row)
    guessed_states.append(answer)
    x_cor = float(state_row.x)
    y_cor = float(state_row.y)
    timmy.goto(x_cor, y_cor)
    timmy.write(f"{answer}")
    score += 1
    screen.title(f'{score}/50 Guessed')
# screen.mainloop()
if len(guessed_states) == 50:
    screen.title('Guessed all correct!')
else:
    states_to_learn = [state for state in states if state not in guessed_states]
    data_dict = {
        'state': states_to_learn
    }
    state_df = pandas.DataFrame(data_dict)
    state_df.to_csv('states_to_learn.csv')
