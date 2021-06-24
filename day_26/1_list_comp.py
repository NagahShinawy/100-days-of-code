"""
created by Nagaj at 24/06/2021
"""
import random
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


countries = {
    "egypt": ["Alex", "Cairo", "Giza"],
    "sa": ["Riyad", "Makka", "Dammam", "Madina", "Dadda"],
    "usa": ["Dubai", "Abu dhabi"],
}

counts = {country: len(cities) for country, cities in countries.items()}

print(counts)

names = ["John", "James", "Leon", "Smith", "Sara", "Angela", ""]

names_length = {name: len(name) for name in names if name}
print(names_length)

authors = {"bob": [40, 60], "james": [10, 80, 30, 50], "john": [15, 35, 70, 30]}
# result = {
#     "bob": 120,
#     "james": 120,
#     "john": 120
# }

revenue = {author: sum(prices) for author, prices in authors.items()}

print(sorted(revenue.items(), key=lambda author: author[-1]))
print(
    {
        author: sum(prices)
        for author, prices in sorted(authors.items(), key=lambda author: sum(author[1]))
    }
)

print("#" * 100)

authors = {
    "bob": [{"title": "clean code", "price": 30}, {"title": "clean ach", "price": 50}],
    "james": [{"title": "flask", "price": 10}, {"title": "django", "price": 90}],
}


def calc_total_revenue(books: list) -> float:
    total = 0
    for book in books:
        total += book["price"]
    return total


total_revenue = {author: calc_total_revenue(books) for author, books in authors.items()}

print(total_revenue)

students = ["john", "james", "sara"]

scores = {student: random.randint(1, 100) for student in students}

print(scores)

passed_students = {student: score for student, score in scores.items() if score >= 60}

print(passed_students)

print("#" * 100)


def exclude_punctuation(original_text: str):
    new_text = ""
    for char in original_text:
        if char not in punctuation:
            new_text += char
    return new_text


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

sentence = exclude_punctuation(sentence)

words = sentence.split()

count_letters = {word: len(word) for word in words if word and word not in punctuation}

print(count_letters)
