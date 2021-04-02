from typing import Union


def format_name(name: str) -> str:
    return name.title()


def format_name2(*args: Union[str]) -> str:
    fullname = ""
    for name in args:
        fullname += name.title() + " "
    return fullname


def format_name3(fname: str, lname: str) -> str:
    return fname.title() + " " + lname.title()


print(format_name("join james leon"))
print(format_name2("john", "james", "leon"))
print(format_name3("john", "james"))


# return value
length = len("test")

if length < 3:
    print("Short name")
