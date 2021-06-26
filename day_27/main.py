"""
created by Nagaj at 26/06/2021
"""
from datetime import datetime


# 1- required inputs
def welcome(name: str):
    print(f"Welcome {name}")


# 2- default inputs (user can update it)
def capture_photo(photoname=datetime.now()):
    if not isinstance(photoname, str):
        print(f"{photoname.strftime('%Y-%m-%d %H:%M:%S')}.png")
    else:
        print(photoname + ".png")


# 3- required and default inputs
def init_screen(title, size=500):
    print(f"Creating Screen '{title}' with size '{size}'")


# 3- required, default inputs and more args
def init_screen2(title, size=500, *args):
    print(f"Creating Screen '{title}' with size '{size}'")
    if args:
        print(f"Available colors are {args}")


# 4- required, default inputs and more args
def init_screen3(title, size=500, *args, **kwargs):
    print(f"Creating Screen '{title}' with size '{size}'")
    if args:
        print(f"Available colors are {args}")
    font = kwargs.get("font")
    style = kwargs.get("style")
    if font:
        print(f"Your Font is {font}")

    if style:
        print(f"Your Style is {style}")


def show_colors(*args):
    for color in args:
        print(color)


# use might parse 0 or many arguments
def names_len(*args: str):
    return {name: len(name) for name in args}


def exclude_keys(items: dict, *args):
    new_items = dict()
    for key in items:
        if key not in args:
            new_items[key] = items[key]
    return new_items


def update_values(items: dict, **kwargs):
    for key, value in kwargs.items():
        if key in items:
            items[key] = value

    return items


def table_style(title="TABLE", **kwargs):
    print(f"Your are styling table with name {title}")
    font = kwargs.get("font")
    bgcolor = kwargs.get("background")
    color = kwargs.get("color")
    if font:
        print(f"Table font is {font}")

    if bgcolor:
        print(f"Table bgcolor is {bgcolor}")

    if color:
        print(f"Table color is {color}")


def my_fuc(a, b, c):
    print(a, b, c)


def add(*args: float):
    # unlimited positional arguments
    # packing(collect) all values to tuple (args)
    return sum(args)


if __name__ == "__main__":
    welcome("")
    capture_photo()
    capture_photo("nagah")
    init_screen("Pong Game")
    init_screen("Pong Game", size=200)
    init_screen2("Memory Game", 300, "green", "black", "blue")
    init_screen3("Snake Game", 400, "green", "black", "blue", font=40, style="bold")

    print("#" * 100)
    show_colors("white", "yellow", "blue")
    show_colors()
    print("#" * 100)
    show_colors("black")

    print("*" * 100)
    table_style()
    print("*" * 100)
    table_style("Scores", font=10)

    my_fuc(c=7, a=4, b=10)

    # todo : check problems
    # SyntaxError: positional argument(required_ follows keyword argument(optional)
    # to avoid parse many values to the same argument
    # in this case you parse values 7 and 4 for the same arg [b]
    # my_fuc(b=7, 4, a=10)  # you can not do that

    # my_fuc(5, a=7, b=8)  # TypeError: my_fuc() got multiple values for argument 'a'

    print("#" * 100)
    print(names_len("john", "thomas", "james"))
    print(names_len("leon"))

    print(exclude_keys({"name": "james", "age": 40, "salary": 5000}, "salary", "age"))
    print(
        update_values(
            {"name": "james", "age": 40, "salary": 5000},
            salary=10000,
            name="James Thomas",
        )
    )

    print(add(5, 6, 10))
    print(add(7, 3))
    # refer to arguments by name not position
