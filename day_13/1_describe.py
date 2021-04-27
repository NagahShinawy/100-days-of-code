"""
created by Nagaj at 27/04/2021
"""


def find_number_in_range(number: int, start: int, end: int) -> int:
    for i in range(start, end):
        if i == number:
            return number


def find_number_in_range2(number: int, start: int, end: int) -> int:
    for i in range(start, end + 1):
        if i == number:
            return number


def find_number_in_range3(number: int, start: int, end: int) -> int:
    return number if number in range(start, end + 1) else False


print(find_number_in_range(number=10, start=5, end=10))
print(find_number_in_range2(number=10, start=5, end=10))
print(find_number_in_range3(number=40, start=5, end=10))
number = 60
start = 12
end = 30
if find_number_in_range3(number=number, start=start, end=end):
    print(f"{number} Found.")

else:
    print(f"{number} not found between {start} and {end}.")
