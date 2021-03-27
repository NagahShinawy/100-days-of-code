from random import randint

computer_number = randint(1, 10)
print(computer_number)
user_number = int(input("Enter Number from 1 to 10"))


tries = 1
while user_number != computer_number:
    user_number = int(input(f"Wrong Guess, Try Again. You Tried <{tries}>"))
    tries += 1

if tries == 1:
    text = "try"
else:
    text = "tries"
print("You Win After {} {}".format(tries, text))

option = input("Enter Option l(list) / d(delete) / u(update)")
#
# options = ["l", "d", "u"]
# while option not in options:
#     option = input(
#         f"Invalid option <{option}>, Type 'l' for (list) / 'd' for (delete) / 'u' for (update)"
#     )
#
# if option == "l":
#     print("Listing ....")
#
# elif option == "d":
#     print("Deleting .....")
#
# elif option == "u":
#     print("Updating .....")

while 1:
    option = input(
        f"Invalid option <{option}>, Type 'l' for (list) / 'd' for (delete) / 'u' for (update)"
    )
    if option == "l":
        print("Listing ....")

    elif option == "d":
        print("Deleting .....")

    elif option == "u":
        print("Updating .....")
    else:
        continue
    break
