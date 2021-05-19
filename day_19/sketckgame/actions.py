"""
created by Nagaj at 19/05/2021
"""

from game import tim, screen


def move_forwards():
    tim.forward(10)


def move_backwards():
    print("You are moving back")
    tim.backward(10)


def turn_left():
    print("You are turning left")
    tim.setheading(tim.heading() + 10)


def turn_right():
    print("you are turning right")
    tim.setheading(tim.heading() - 10)


def clear():
    print("clearing the screen and retry again")
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def close():
    print("You are closing the window")
    screen.bye()
