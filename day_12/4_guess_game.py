"""
created by Nagaj at 24/04/2021
"""
# todo : json file for result , user_number, computer_number, attempts, result
import random

from art import logo

print(logo)

LEVELS = ["easy", "hard"]
ATTEMPTS = 5
REMAINING_EASY = 11
REMAINING_HARD = 6
REMAINING = REMAINING_HARD
RESULT = {"lose": "Lose", "win": "Win"}


def get_computer_number() -> int:
    return random.randint(1, 100)


def validate_number() -> int:
    number = int(input("Enter Your Number From '1' to '100'."))
    # CHAIN OPERATORS: (LARGER THAN AND SMALLER THAN)
    is_valid_number = 1 <= number <= 100
    while not is_valid_number:
        number = int(input(f"Invalid Number <{number}>. Type From '1' to '100'."))
        is_valid_number = 1 <= number <= 100
    return number


def validate_level() -> str:
    level = input("Enter Level 'easy' or 'hard'.")
    while level.lower() not in LEVELS:
        level = input(f"Invalid Level <{level}>. Type 'easy' or 'hard'").lower()
    return level


def play_guess_game(computernumber, usernum):
    """
    check if number by user matches computernumber
    :param computernumber: correct answer
    :param usernum: guess number bu yser
    :return:
    """
    _ATTEMPTS = ATTEMPTS
    is_win = True
    while computernumber != usernum:
        _ATTEMPTS -= 1
        if _ATTEMPTS == 0:
            print(f"You {RESULT['lose']}, After {ATTEMPTS} Attempts")
            is_win = False
            break
        if usernum > computernumber:
            print("It Is High")
        else:
            print("It Is Low")
        print(f"Not Match, You Have Only {_ATTEMPTS} Attempts")
        usernum = validate_number()

    if is_win:
        print(f"You {RESULT['win']}, After {REMAINING - _ATTEMPTS} attempts")


computer_number = get_computer_number()
validated_level = validate_level()
user_num = validate_number()

if validated_level == "easy":
    ATTEMPTS = 10
    REMAINING = REMAINING_EASY

play_guess_game(computer_number, user_num)
