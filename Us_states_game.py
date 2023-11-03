#This is the main file for US states game:

import turtle
import pandas
tim = turtle.Turtle()
screen = turtle.Screen()
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Tex the turtle will move to different locations on the screen and display the name of the state in US;

tex = turtle.Turtle()

#We need to hide him to make it more fun!:

tex.hideturtle()

#This list stores all the guessed states:

guessed_states = []

i=0

#Its a while loop since we need the user to guess all the 50 states:

while i < 50:
    #This will prompt the user to input a new state or 'exit' to exit the program.
    answer_state = screen.textinput(title=f"{i}/50 states found",prompt= "Enter the US state?").title()
    states = pandas.read_csv("./50_states.csv")

    if answer_state == "Exit":
        missed_states = pandas.DataFrame([num for num in list(states.state) if num not in guessed_states])

        #Missed states are collected as a csv file:
        missed_states = missed_states.to_csv("./missed_states.csv")

        #Display all the missed states:
        print(pandas.read_csv("./missed_states.csv"))

        break

    elif answer_state in list(states.state):

        i+=1

        guessed_states.append(answer_state.title())

        #Tex's pen should be up:
        tex.penup()
        #Tex will go to the coordinate and print the name:
        tex.goto(int(states[states.state == answer_state.title()].x), int(states[states.state == answer_state.title()].y) )

        tex.write(answer_state.title())





screen.mainloop()

