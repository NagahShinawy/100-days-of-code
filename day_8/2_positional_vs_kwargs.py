def to_json(**kwargs):
    return kwargs


def add_table_style(color="red", bgcolor="gray"):
    print("Table colors is <{}> and <{}> for background".format(color, bgcolor))


def complete_profile(name, email, image=None):
    print(f"Welcome <{name}> you have completed your profile")
    print(f"confirmation message sent to your email <{email}>. please check")
    if image:
        print("Your image updated")


def great_with(name, location):
    print(f"Hi, {name}")
    print(f"What it is looks like in {location}")


print(to_json(name="John", title="Python Developer"))

add_table_style()

complete_profile(name="John", email="John@google.com")
print("#" * 30)
complete_profile(name="John", email="John@google.com", image="/john.png")
print("#" * 30)


great_with("Sara", "USA")  # positional argument ( order is must to match parameters)
great_with(
    location="Italy", name="John"
)  # keyword argument (no matter order is because you are using keyword argument)
