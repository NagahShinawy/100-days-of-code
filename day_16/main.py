"""
created by Nagaj at 15/05/2021
"""
import another_module
from turtle import Turtle, Screen
from prettytable import PrettyTable

#
# print(another_module.items)

# timmy = Turtle()  # timmy is the arrow located in the middle of screen by default
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(250)  # 250 moves
# timmy.back(250 * 2)
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
#
# my_screen.exitonclick()  # still running screen until click anywhere to exit


print("| Pokemon Name | Type |")
print("_" * 25)

columns = ["name", "age", "address", "phone"]

john = ["John", 20, "London", "01278309863"]
james = ["James", 25, "Paris", "01070309863"]
leon = ["Leon", 30, "Roma", "0104000000"]
employees = PrettyTable()
employees.field_names = columns
employees.add_row(john)
employees.add_row(james)
employees.add_row(leon)
print(employees)

print("*" * 100)

books = [
    ("clean code", "bob", 400),
    ("flask micro framework", "john", 200),
    ("django web framework", "james", 500),
]


def update_field(new_field, old_field, fields):
    old_field_index = fields.index(old_field)

    if old_field_index == 0:
        new_fields = [new_field] + fields[1:]

    elif old_field_index == len(fields) - 1:
        new_fields = fields[:-1] + [new_field]

    else:
        new_fields = (
            fields[:old_field_index] + [new_field] + fields[old_field_index + 1 :]
        )

    return new_fields


book_table = PrettyTable()
book_table.field_names = ["title", "author", "pages"]
book_table.add_rows(books)

print(book_table)
print("#" * 30)
book_table.add_column("price", [15, 20, 30])
print(book_table)
book_table.field_names = update_field("MYPRICE", "price", book_table.field_names)
book_table.field_names = update_field("MYTITLE", "title", book_table.field_names)

print(book_table)

book_table.align = "r"  # align to right
print(book_table)

book_table.align = "l"

print(book_table)  # align to left
