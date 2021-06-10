"""
created by Nagaj at 10/06/2021
"""
from program import get_names, read_letter


def test_names_list():
    names = get_names()
    expected = ["Aang", "Zuko", "Appa", "Katara", "Sokka", "Momo", "Uncle Iroh", "Toph"]
    assert names == expected


def test_letter_body_template():
    body = read_letter()
    expected = """Dear [name],

You are invited to my birthday this Saturday.

Hope you can make it!

Angela"""
    assert body == expected
