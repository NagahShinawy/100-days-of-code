"""
created by Nagaj at 15/05/2021
"""
from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
coffee_maker.report()
money_machine.report()

print(menu.get_items())

print("#" * 100)

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What Would you like? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink is None:
            continue
        print(f"You Have Chose Drink '{drink.name}' With Cost '{drink.cost}'")
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            coffee_maker.make_coffee(drink)
