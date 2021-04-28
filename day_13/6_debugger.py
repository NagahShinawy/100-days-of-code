"""
created by Nagaj at 28/04/2021
"""


def mutate(items: list) -> list:
    new_items = []
    for item in items:
        new_value = item * 2

    new_items.append(new_value)
    return new_items


# using the fastest way


def mutate2(items: list) -> list:
    return [value * 2 for value in items]


# print(mutate([]))
print(mutate2([5, 6, 4, 9]))
