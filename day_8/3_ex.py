"""
having a list of names , get names startswith "J"
"""

names = ["Leon", "Sara", "John", "Julia"]

names_starswith_j = [name for name in names if name and name[0] in ("j", "J")]

print(names_starswith_j)


def is_name_exists(name, names):
    if name in names:
        return True
    return False


print(is_name_exists(name="John", names=names))
