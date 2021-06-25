"""
created by Nagaj at 25/06/2021
"""
import pandas as pd

states = pd.read_csv("./states.csv")
# print(states)
# for i in range(len(states)):
#     print(states["state"][i])

print("#" * 100)
students_ = [
    {"name": "John", "Arabic": 30, "English": 50, "Math": 60},
    {"name": "James", "Arabic": 67, "English": 55, "Math": 75},
    {"name": "Leon", "Arabic": 20, "English": 80, "Math": 90},
    {"name": "Angela", "Arabic": 45, "English": 85, "Math": 95},
]
# orderDictionary
students_df = pd.DataFrame(students_)
print(students_df)
print("#" * 100)
students = {"name": ["Leon", "James", "Angela"], "score": [60, 50, 20]}
for item in students.items():  # every item is tuple , item is tuple of key and value
    print(item)

print("#" * 50)
# looping through dictionaries
for (
    name,
    score,
) in students.items():  # using tuple unpacking to get name(key) and score(value)
    print(name, score)

print("#" * 50)

for (
    name,
    score,
) in students.items():  # using tuple unpacking to get name(key) and score(value)
    print(name, score)

dimension1 = (
    4,
    7,
)  # you can use () or remove it to init a tuple jut like we did in student.items()
dimension2 = 4, 7

print(dimension1 == dimension2)

print("*" * 30)
# key is name , series list of names
# key is arabic , series list of arabic
# .......

# not the best way to loop through dataframe
# not return entire row, it returns entire col
# iteration#1 ==> all names (first col)
# iteration#2 ==> all arabic (second col)
# and so on
for col, series in students_df.items():
    print(col, series)

print("#" * 100)
for index, row in students_df.iterrows():
    print(index + 1, end=" ")
    # each row contains series of entire row values ==>  (name, John),(arabic, 30),(english, 50), (math, 60)
    for (
        value
    ) in row:  # one iteration is (name, John),(arabic, 30),(english, 50), (math, 60)
        # but NOT like tuple unpacking. it returns value of each col ==> John 30 50 60
        print(value, end=" ")
    print()
print("#" * 60)
# Series obj contains index (number or string) and value, you can use index to access the value. NOT tuple unpacking
# index just use to access the value like list, tuple, string but Series itself not return something
# like [ (index, value), ....] . it just one value you can through over
names = states["state"]
for name in names:
    print(name)

print("*" * 50)

# every row is a series contains entire row values
# LIKE ==> (name, John),(arabic, 30),(english, 50), (math, 60). NOT list of tuple. it is series (index, value)
# (index, value) but don't use unpacking. index is NOT actual value. it used to access the value
for index, row in students_df.iterrows():
    print(index + 1, *row, end=".\n")

# you can access series value using series index (int or string)

print("#" * 50)
for index, row in students_df.iterrows():
    if row["name"] == "James":
        print(row["name"], row["Math"], row["Arabic"], row["English"])

print("*" * 50)
