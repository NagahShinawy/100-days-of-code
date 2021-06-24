"""
created by Nagaj at 24/06/2021
"""
from string import punctuation


numbers = [5, 6, 7]

plus_one = [number + 10 for number in numbers]

print(plus_one)

# square numbers from 10 to 20

squares = [num ** 2 for num in range(10, 21)]
print(squares)
names = ["joHn", "JaMes", "LEon", "smItH"]  # James, John

names = [name.title() for name in names]
print(names)

tolist = [char.upper() for char in "test"]

print(tolist)

text = "I am using python 3.5"

letters = [char for char in text if not char.isdigit() and char not in punctuation]
print("".join(letters))

# even numbers from 1 to 10

evens = [num for num in range(1, 11) if num % 2 == 0]

print(evens)

# using filter


def find_even(number: int):
    return number % 2 == 0 and number > 5


def find_odd(number: int):
    return number % 2 != 0 and number >= 5


evens = filter(find_even, range(1, 11))
print(list(evens))


names = ["angela", "james", "John Smith", "leon", "Jolia", "alex"]
to_upper = [name.upper() for name in names if len(name) > 5]

print(to_upper)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squares = [num ** 2 for num in numbers]

print(squares)
odds = [num for num in numbers if num % 2 != 0]

print(odds)

odds2 = filter(find_odd, numbers)
print(list(odds2))

evens = filter(find_even, numbers)
print(list(evens))


def get_lines(file):
    with open(file) as f:
        all_lines = f.readlines()
        if not all_lines[-1].endswith("\n"):
            all_lines[-1] = all_lines[-1] + "\n"
        return all_lines


lines1 = get_lines("file1.txt")
lines2 = get_lines("file2.txt")
if len(lines1) < len(lines2):
    lines = lines1
    other = lines2
else:
    lines = lines2
    other = lines1
common = [int(line) for line in lines if line in other]

print(common)


def test_squares():
    for i in range(len(numbers)):
        assert numbers[0] ** 2 == squares[0]
