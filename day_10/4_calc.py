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
        answer = operations[operator](first, second)
        if answer is False:
            print("Can not div by Zero Try again")
            continue
        option = input(
            f" {first} {operator} {second}  = '{answer}', 'y' to continue or 'no' to restart, ex: to exists"
        )
        if option == "n":
            print("result '{}'".format(answer))
            repeat = False
            calculator()  # restart calc
        elif option == "ex":
            print("Existing the calculator with final result '{}'".format(answer))
            repeat = False
        else:
            # update first number to be latest answer
            first = answer


calculator()
