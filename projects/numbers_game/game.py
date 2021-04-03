from random import randint

user_number = int(input("Enter Your Number"))

computer_number = randint(5, 101)
tries = 1
while user_number != computer_number:
    if user_number > computer_number:
        print(f"Your Number <{user_number}> is bigger than computer number")
        if (user_number - computer_number) in range(1, 4):
            print("Almost Done. reduce Your number little bit")
    else:
        print(f"Your Number <{user_number}> is less than computer number")
        if (computer_number - user_number) in range(1, 4):
            print("Almost Done. Increase Your number little bit")
    user_number = int(input("New Number"))
    tries += 1


print("You Win after <{}>".format(tries))
