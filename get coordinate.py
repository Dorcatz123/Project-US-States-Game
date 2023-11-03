#This file is to collect the coordinates of different states in USA:

import turtle
tim = turtle.Turtle()

#We will use this image to collect the coordinates of different states in USA:

image = "./blank_states_img.gif"

screen = turtle.Screen()

screen.addshape(image)

#Using the US image as the shape of the turtle to obtain coordinates.

turtle.shape(image)

new_coordinates = []

#The coordinates are obtained when a click is made at a particular point on the screen.

def get_coordinates(x,y):
    new_coordinates.append((x,y))
    print(new_coordinates)


screen.onscreenclick(get_coordinates)



turtle.mainloop()

print(new_coordinates)