"""
created by Nagaj at 19/05/2021
"""
from turtle import Turtle, Screen
from constants import keys


def move_forwards():
    tim.setheading(0)
    tim.forward(10)


def move_back():
    tim.setheading(180)
    tim.forward(10)


def move_up():
    tim.setheading(90)
    tim.forward(10)


def move_down():
    tim.setheading(270)
    tim.forward(10)


def close():
    screen.bye()


def clear():
    screen.reset()


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def multi(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


def calc(n1, n2, func):
    return func(n1, n2)


if __name__ == "__main__":
    tim = Turtle()
    screen = Screen()
    screen.listen()
    screen.onkey(
        fun=move_forwards, key=keys.FORWARD
    )  # run function "move_forwards" when click on "s"
    screen.onkey(
        fun=move_back, key=keys.BACK
    )  # run function "move_back" when click on "a"
    screen.onkey(fun=move_up, key=keys.UP)  # run function "move_up" when click on "w"
    screen.onkey(
        fun=move_down, key=keys.DOWN
    )  # run function "move_down" when click on "z"
    screen.onkey(fun=close, key=keys.CLOSE)
    screen.onkey(fun=clear, key=keys.CLEAR)
    screen.exitonclick()
    n1 = 12
    n2 = 2
    for func in [add, sub, multi, division]:
        print(calc(n1, n2, func))
