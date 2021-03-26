left_or_right = input(
    'You\'re across road, where do you want to go? type "left" / "right" . '
).lower()

if left_or_right == "left":

    swim_or_wait = input(
        'You have come to lake , there is an island on the middle of the lake Type "swim" / "wait"'
    ).lower()
    if swim_or_wait == "wait":
        door = input("You have 3 doors with one do you want ? red / blue/ yellow")
        if door == "red":
            print("Room full of fire .Game Over")
        elif door == "blue":
            print("You entered a room of beasts .Game Over")
        elif door == "yellow":
            print("You found the treasure. You Win")
        else:
            print(f'Door "{door}" not found')
    elif swim_or_wait == "swim":
        print("You have go attacked .Game Over")

elif left_or_right == "right":
    print("You fell into a hole Game Over")
