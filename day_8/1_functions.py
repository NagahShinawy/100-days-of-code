def great(name):
    print("Hello {}".format(name))
    print("How are you, {}?".format(name))
    print("Weather nice today, {}?".format(name))


def welcome(name, title):
    pass


def get_bigger_number(num1: float, num2: float):
    return num1 > num2


def func(something):
    # <something> is a parameter and value passed is <an argument>
    pass


if __name__ == "__main__":
    great(name="John")
    print(get_bigger_number(10, 6.5))
    # welcome(
    #     "John", nam="test"
    # )  # TypeError: welcome() got multiple values for argument 'name'
