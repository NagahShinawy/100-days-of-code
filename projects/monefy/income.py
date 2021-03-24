from projects.monefy.category import IncomeCategory


class Income(IncomeCategory):
    SIGN = "+"

    def __init__(self, value, income_category, description=None):
        super().__init__(value=value, category=income_category, description=description)
