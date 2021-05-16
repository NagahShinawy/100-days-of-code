"""
created by Nagaj at 16/05/2021
"""


class Question:
    total = 0

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def __repr__(self):
        return self.text
