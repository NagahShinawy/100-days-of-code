"""
created by Nagaj at 22/04/2021
"""
import random
import os


def deal_cards():
    """

    :return: random card
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards: list):
    """
    calc scores

    :param cards: list of random cards to sum
    :return: sum of random cards
    """
    # blackjack_condition = [11 in cards, 10 in cards, len(cards) == 2]  # total is 21
    # check_blackjack = all(blackjack_condition)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)  # ace
        cards.append(1)  # ace

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, Opponent has blackjack"
    elif user_score == 0:
        return "Win with blackjack"

    elif user_score > 21:
        return "You Went Over. You lose"
    elif computer_score > 21:
        return "Opponent Went Over. You Win"
    elif user_score > computer_score:
        return "You Win"
    else:
        return "You Lose"


def play_game():
    is_game_over = False
    user_cards = [deal_cards() for _ in range(2)]
    computer_cards = [deal_cards() for _ in range(2)]
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your Cards {user_cards}, Your Score {user_score}")
        print(f"Computer first's card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, 'n' to pass")
            if user_should_deal == "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)
    print("#" * 100)
    print(f"Your Final Hands {user_cards}, final Score {user_score}")
    print(f"Computer Final Hands {computer_cards}, final Score {computer_score}")
    print(compare(user_score, computer_score))


def main():
    play_game()
    print("#" * 100)
    repeat = input("Do You Want to play a game of Blackjack? Type 'y' or 'n': ")
    while repeat == "y":
        play_game()


if __name__ == "__main__":
    main()
