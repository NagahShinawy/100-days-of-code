"""
created by Nagaj at 18/05/2021
"""
import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
turtle.colormode(255)
# directions = [tim.left, tim.right]
directions = [0, 90, 180, 270]  # north, east, south, west
speeds = ["fastest", "fast", "normal", "slow", "slowest"]
# colors = [
#     "deep sky blue",
#     "dodger blue",
#     "green yellow",
#     "crimson",
#     "dark magenta",
#     "dark violet",
#     "blue violet",
#     "olive drab",
#     "gray",
#     "olive drab",
#     "medium orchid",
#     "dark orange",
# ]


def random_rgb_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue


def random_move():
    moves = random.randint(20, 50)
    direction = random.choice(directions)
    speed = random.choice(speeds)
    # tim.color(random.choice(colors))
    tim.color(
        random_rgb_color()
    )  # you must use "turtle.colormode(255)" when you need to use RGB colors mode.
    tim.pensize(random.randint(1, 5))
    tim.setheading(direction)
    tim.forward(moves)
    tim.speed(speed)


def random_walk():
    for _ in range(100):
        random_move()


def draw_spirograph():
    def draw_single_circle(size_of_gap):
        # speed = random.choice(speeds)
        tim.pensize(random.randint(1, 5))
        tim.color(random_rgb_color())
        tim.speed("fastest")
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)  # current position + shifting
        tim.circle(100)

    size_of_gap = 10
    # size_of_gap = 36
    for _ in range(
        360 // size_of_gap
    ):  # to complete one circle  iteration. 10 degree between each single drawn circle. means 36 single circle: 360/10
        draw_single_circle(size_of_gap)


# random_walk()
tim.reset()  # clear the screen
draw_spirograph()
print(tim.heading())
Screen().exitonclick()
