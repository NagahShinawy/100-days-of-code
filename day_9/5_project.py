# http://pythontutor.com/visualize.html#mode=display
# visualize your code

import os


def is_valid_option(opt: str):
    while opt not in ["yes", "no"]:
        opt = input(f"Invalid Option '{opt}'. Type 'yes' or 'no' ")
    return opt


def validate_name(name: str):
    while len(name) < 3:
        name = input("name must be at least 3 letters")
    return name


def validate_bid(bid: str):
    while not bid.isdigit():
        bid = input(f"Invalid int '{bid}' Please Type a valid int number")
    return int(bid)


def main():
    repeat = True
    max_bid = 0
    winner = ""
    process = dict()
    while repeat:
        name = validate_name(input("Enter name"))
        bid = validate_bid(input("Enter Bid"))
        if bid > max_bid:
            max_bid = bid
            winner = name
            process.update({"name": name, "bid": bid})

        option = input("Repeat the process? Type 'yes' or 'no'")
        opt = is_valid_option(option)
        if opt == "no":
            repeat = False
        os.system("cls")  # clear
    print(f"Winner is '{winner}' with Bid '{max_bid}$'")
    print(f"Winner is '{process['name']}' with Bid '{process['bid']}$'")


if __name__ == "__main__":
    main()
