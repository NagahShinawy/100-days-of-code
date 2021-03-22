# get length of string


def is_odd(number):
    return False if number % 2 == 0 else True


def is_even(number):
    return True if number % 2 == 0 else False


def count(string: str):
    assert type(string) == str, "Not string , it is {}".format(
        string.__class__.__name__
    )
    i = 0
    for _ in string:
        i += 1
    return i


# Returns length of string
def findlen(string):
    counter = 0
    while string[counter:]:
        counter += 1
    return counter


# Returns length of string
def getlen(string: str):
    if not str:
        return 0
    else:
        some_random_str = 'py'  # 'tpyepyspyt' ==> if string=test
        return some_random_str.join(string).count(some_random_str) + 1


geeks = "test"
print(getlen(geeks))

name = input("Enter Your Name: ")

print(name)
print(len(name))
print(is_odd(len(name)))
print(count("test"))
print(findlen("test"))

print("#" * 20)

print("Color:", len(input("Enter Your color: ")))