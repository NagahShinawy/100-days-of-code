users = ["John", "Leon", "Sara"]


def breakline(symbol="#", times=20):
    print(symbol * times)


def welcome_user(username: str):
    print("Welcome " + username)


def get_info(username: str, age: int):
    print(f"Name <{username}> is and age is <{age}>")


def bye(username: str):
    print("Hope we meet you again soon <{}> !.".format(username))


def get_user_by_name(username: str):
    username = username.lower()
    if username in [user.lower() for user in users]:
        print(f"user is <{username.title()}>")
    else:
        print(f"User <{username}> not found")


def get_milk(store: str, quantity: int):
    print(f"Go to Store <{store}> and get <{quantity}> bottle(s) of milk")


welcome_user("John")
breakline()
get_info("John", 25)
print("Name is John")
breakline()
bye("Leon")
breakline(symbol="*", times=10)
get_user_by_name("SAra")
breakline()
get_user_by_name("test")
breakline()
get_milk("Janna Store", 2)
print("John", 24, sep="||")  # separator

print(len("john"))  # valid input for len function
