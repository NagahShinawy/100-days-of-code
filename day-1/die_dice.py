
class Number:

    def __init__(self, number):
        self.number = number

    def is_valid(self):
        if self.number in range(1, 7):
            return True
        else:
            raise ValueError(f"Invalid number '{self.number}',  must be in from 1 to 6")

    def to_int(self):
        return self.number

    def is_even(self):
        return True if self.number % 2 == 0 else False

    def is_odd(self):
        return False if self.number % 2 == 0 else True