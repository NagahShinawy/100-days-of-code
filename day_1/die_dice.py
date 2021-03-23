class Number:
    def __init__(self, number: int):
        self.number = number

    # def is_valid(self):
    #     if self.number in range(1, 7):
    #         return True
    #     else:
    #         raise ValueError(f"Invalid number '{self.number}',  must be in from 1 to 6")

    def to_int(self):
        return self.number

    def is_even(self):
        return True if self.number % 2 == 0 else False

    def is_odd(self):
        return False if self.number % 2 == 0 else True

    def is_max(self):
        return True if self.number == 6 else False

    def is_min(self):
        return True if self.number == 1 else False

    @property
    def number(self):
        """
        valid_number to avoid:  maximum recursion depth exceeded while calling a Python object
        :return:
        """
        return self.valid_number

    @number.setter
    def number(self, num):
        """
        run method before assign number attribute to validate it.
        :param num:
        :return:
        """
        if type(num) is not int:
            raise ValueError(f"Number is only <int> not <{num.__class__.__name__}>")

        if num not in range(1, 7):
            raise ValueError(f"Invalid Number {num}, should be from 1 to 6")
        self.valid_number = num
