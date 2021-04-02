def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return False
    return a / b


def calculator():
    operations = {"+": add, "-": sub, "*": multiply, "/": division}
    repeat = True
    first = int(input("Enter first number : "))
    while repeat:
        second = int(input("Enter next number number : "))
        operator = input("Enter Operator (+, -, *, / )")
        total = operations[operator](first, second)
        if total is False:
            print("Can not div by Zero Try again")
            continue
        options = input(f" {first} {operator} {second}  = '{total}', 'yes' or 'no'")
        if options == "no":
            print("Final result is '{}'".format(total))
            repeat = False
        first = total


calculator()
