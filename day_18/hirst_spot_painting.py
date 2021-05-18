"""
created by Nagaj at 18/05/2021
"""
import random
import turtle
from turtle import Turtle, Screen
import colorgram
from colors import rgb_colors_list


tim = Turtle()
tim.penup()
tim.speed("fastest")
turtle.colormode(255)
tim.setheading(255)
tim.forward(300)
tim.setheading(0)
tim.hideturtle()

#
# colors = colorgram.extract("hirst spot painting.jpg", 10)


def generate_colors_from_image(image, num_of_colors):
    colors = colorgram.extract(image, num_of_colors)
    rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

    return rgb_colors


def draw_dot():
    tim.dot(20, random.choice(rgb_colors_list))
    tim.fd(50)


def next_step(step_number):
    tim.home()
    shifting = step_number * 10
    tim.setheading(tim.heading() + shifting)


def draw_flower():
    steps = 360 // 10
    for step_number in range(1, steps + 1):
        for _ in range(10):
            draw_dot()
        next_step(step_number)


def next_step_for_dots(step_number):
    tim.home()
    shifting = step_number * 30
    moves = tim.heading() + shifting
    print(moves)
    tim.left(90)
    tim.fd(moves)
    tim.right(90)


def draw_dots():
    for step_number in range(1, 10):
        for _ in range(10):
            draw_dot()
        next_step_for_dots(step_number)


def go_home():
    tim.setheading(90)  # look to up
    tim.forward(50)  # move to up
    tim.setheading(180)  # look to left
    tim.forward(500)  # move to reach the home point
    tim.setheading(0)  # look right


def draw_dots_challenge():
    number_of_dots = 100
    for dot_count in range(1, number_of_dots + 1):
        tim.dot(20, random.choice(rgb_colors_list))
        tim.forward(50)
        if dot_count % 10 == 0:
            # if dot_count == 100:
            #     break
            go_home()


def main():
    print(rgb_colors_list)
    # draw_flower()
    # draw_dots()
    draw_dots_challenge()
    Screen().exitonclick()


if __name__ == "__main__":
    main()
    # tim.setheading(45)
    # time.sleep(2)
    # tim.setheading(225)  # 45 but the vs direction
    # Screen().exitonclick()
