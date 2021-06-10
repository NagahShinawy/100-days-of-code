"""
created by Nagaj at 09/06/2021
"""
import os


def get_file_or_create():
    if not os.path.isfile(os.path.join(os.getcwd(), "scores.txt")):
        with open("scores.txt", "w") as f:
            f.write("0")


with open("scores.txt", "r") as f:
    content = f.read()

print(content, type(content))


# write(w) mode ==> override content
# if file does not exist , it will be created
with open("scores_.txt", "w") as f:
    f.write("PHP for web development")


# append(a) mode ==> append content
# if file does not exist , it will be created
with open("_scores.txt", "w") as f:
    f.write("PHP for web development")
