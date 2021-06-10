"""
created by Nagaj at 20/05/2021
"""
import time
from turtle import Screen, Turtle
from typing import List

# #######    CONSTANTS  ##################
WIDTH = 600
HEIGHT = 600
BLACK = "black"
SQUARE = "square"
WHITE = "white"

# ########################################


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


def screen_setup():
    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.bgcolor(BLACK)
    screen.title("Snake Game")
    screen.tracer(0)
    return screen


def create_snake():
    segments = []
    for position in STARTING_POSITIONS:
        segment = Turtle(shape=SQUARE)
        segment.color(WHITE)
        segment.penup()
        segment.goto(x=position[0], y=position[1])
        segments.append(segment)
    return segments


def move_snake(segments: List[Turtle], screen: Screen):
    is_game_on = True
    while is_game_on:
        screen.update()
        for seg in segments:
            seg.forward(20)
            time.sleep(0.1)


def main():
    screen = screen_setup()
    segments = create_snake()
    move_snake(segments, screen)
    screen.exitonclick()


if __name__ == "__main__":
    main()
