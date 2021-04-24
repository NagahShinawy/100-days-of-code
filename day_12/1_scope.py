"""
created by Nagaj at 23/04/2021
"""

"""Variable Scopes"""

username = "John"


def welcome_username():
    username = "James"
    print("Welcome " + username)


print(username)  # John
welcome_username()  # James
print(username)  # John

print("#" * 100)

username = "Leon"


def greeting():
    global username
    username = "Sara"
    print(username)


print(username)  # Leon
greeting()  # Sara
print(username)  # Sara

print("#" * 100)

enemies = 1


def increase_enemies():
    enemies = 2  # local scope
    print(f"enemies inside function: {enemies}")


print(f"enemies OUTSIDE function: {enemies}")
increase_enemies()
print(f"enemies OUTSIDE function: {enemies}")

print("#" * 100)
# ##########################################################################################

username = "Smith"  # global Scope


def say_welcome():
    print(username)  # Smith


say_welcome()


# ############################################################################################


class User:
    username = "USER"


print(User().username)
print(username)

print("#" * 100)


# ############################################################################################


def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()


# print(potion_strength)  # NameError: name 'potion_strength' is not defined


def about():
    global version
    version = "2.0.1"
    print(version)


about()
print("Version", version)


print("#" * 100)


# ############################################################################################


def game():
    def shouter():  # local scope
        print("Shouter")

    return shouter


shouter()  # NameError: name 'shouter' is not defined
