"""
created by Nagaj at 19/05/2021
"""
from game import screen
from actions import move_forwards, move_backwards, turn_left, turn_right, close, clear


if __name__ == "__main__":
    screen.listen()
    screen.onkey(fun=move_forwards, key="w")
    screen.onkey(fun=move_backwards, key="s")
    screen.onkey(fun=turn_left, key="l")
    screen.onkey(fun=turn_right, key="r")
    screen.onkey(fun=close, key="x")
    screen.onkey(fun=clear, key="c")
    screen.exitonclick()
