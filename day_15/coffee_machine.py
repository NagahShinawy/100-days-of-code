"""
created by Nagaj at 07/05/2021
"""

# TODO: check resource sufficient to make drink order

# TODO: 1. print report of all coffee machine resources
from menu import MENU, resources, profit

OFF = "off"
REPORT = "report"
DRINKS = ["espresso", "latte", "cappuccino"]
is_on = True


def is_resource_sufficient(order_ingredients: dict) -> bool:
    """

    :param order_ingredients: ingredients for order (water, milk, coffee
    :return: True if order can be made else False when ingredients are not sufficient
    """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins() -> float:
    """
    calc total from coins inserted
    :return: total of coins inserted
    """
    print("Please Insert Coins")
    quarters = int(input("how many quarters? ")) * 0.25
    dimes = int(input("how many dimes? ")) * 0.1
    nickles = int(input("how many nickles? ")) * 0.05
    pennies = int(input("how many pennies? ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total


def is_transaction_successful(money_received: float, drink_cost: float) -> bool:
    """
        check the payment inserted by the client accepted or not
    :param money_received: money inserted by client
    :param drink_cost: the cost of the drink
    :return: True if accepted payment else False
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True
    print(f"Sorry, '{money_received}' is not enough money.Money Refunded.")
    return False


def make_coffee(drink_name, order_ingredients):
    """
    deduct the requirements ingredients from resources.
    :param drink_name:
    :param order_ingredients:
    :return:
    """
    for item in resources:
        resources[item] -= order_ingredients[item]
    print(f"Here is Your Drink {drink_name} ☕. Enjoy ")


while is_on:
    choice = input("What would you like (espresso/latte/cappuccino)").lower()
    if choice == OFF:
        is_on = False
    elif choice == REPORT:
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Money: ${round(profit, 2)}")
    elif choice in DRINKS:
        drink = MENU[choice]
        is_sufficient = is_resource_sufficient(drink["ingredients"])
        if not is_sufficient:
            continue
        payment = process_coins()
        if not is_transaction_successful(payment, drink["cost"]):
            continue

        profit += drink["cost"]
        make_coffee(choice, drink["ingredients"])
        print(resources)

    else:
        print(f"Invalid Drink Choice '{choice}'")
