"""
created by Nagaj at 04/05/2021
"""
import os
import random
from art import logo, vs
from game_data import data


# format the account data to printable format


def format_account(account):
    name = account["name"]
    desc = account["description"]
    country = account["country"]
    return f"{name}, a {desc} from {country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


score = 0
game_should_continue = True
# Display art
print(logo)
account_b = random.choice(data)
# Generate a random account from the game data.

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_account(account_a)}")
    print(vs)
    print(f"Against B: {format_account(account_b)}")

    # Make the game repeatable.
    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct.
    # ##get follower count for each account

    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]
    # ## Use if to check if user is correct

    print("A count: ", a_followers_count)
    print("B count: ", b_followers_count)
    is_correct = check_answer(guess, a_followers_count, b_followers_count)
    os.system("cls")
    # Give user feedback on their guess.
    if is_correct:
        score += 1
        print("You're Right!, Current Score {}".format(score))
    else:
        print("Sorry , That is wrong. Final Score is {}".format(score))
        game_should_continue = False

# score keeping

# Making account at position B become the next account at position A.

# clear the screen
