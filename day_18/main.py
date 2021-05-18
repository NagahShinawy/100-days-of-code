"""
created by Nagaj at 18/05/2021
"""
import random
from turtle import Turtle, Screen

import heroes

colors = [
    "deep sky blue",
    "dodger blue",
    "green yellow",
    "crimson",
    "dark magenta",
    "dark violet",
    "blue violet",
    "olive drab",
    "gray",
    "olive drab",
    "medium orchid",
    "dark orange",
]


class Timmy:
    def __init__(self, shape, color):
        self.timmy = Turtle()
        self.timmy.color(color)
        self.timmy.shape(shape)


tim = Timmy("turtle", "red")


def square_to_up():
    for i in range(4):
        tim.timmy.forward(100)
        tim.timmy.left(90)
        if i == 3:
            tim.timmy.left(45)
            tim.timmy.forward(130)


def square_to_down():
    for i in range(4):
        tim.timmy.forward(100)
        tim.timmy.right(90)
        if i == 3:
            tim.timmy.right(45)
            tim.timmy.forward(130)


squares = [square_to_up, square_to_down]


# for i in range(10):
#     squares[1]()
#     # square = random.choice(squares)
#     # print(square)
#     # square()


def draw_square():
    s = int(input("Enter the length of the side of squre: "))

    for _ in range(4):
        tim.timmy.forward(s)  # Forward turtle by s units
        tim.timmy.left(90)  # Turn turtle by 90 degree


def draw_dashed_line():
    tim.timmy.pensize(3)

    def draw_empty():
        tim.timmy.forward(10)
        tim.timmy.penup()

    def draw_line():
        tim.timmy.forward(10)
        tim.timmy.pendown()

    for i in range(15):
        draw_empty()
        draw_line()


# todo : use use decorator to change direction from default(left) to right


def draw_shape(num_sides, direction="l"):
    direction_moves = tim.timmy.left
    if direction == "r":
        direction_moves = tim.timmy.right
    tim.timmy.color(random.choice(colors))
    angle = 360 // num_sides
    for i in range(num_sides):
        tim.timmy.forward(100)
        direction_moves(angle)


# draw_square()
# draw_dashed_line()
for dgr in range(3, 10):
    draw_shape(dgr, "r")


for side in range(3, 10):
    draw_shape(side, "l")


print(heroes.gen())
# tim.timmy.home()
screen = Screen()

screen.exitonclick()
