from random import randint

user_number = int(input("Enter Number from 1 to 10"))

computer_number = randint(1, 10)

tries = 1
while user_number != computer_number:
    user_number = int(input(f"Wrong Guess, Try Again. You Tried <{tries}>"))
    tries += 1

if tries == 1:
    text = "try"
else:
    text = "tries"
print("You Win After {} {}".format(tries, text))
