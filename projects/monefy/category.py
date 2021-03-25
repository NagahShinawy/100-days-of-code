class Base:
    SIGN = ""

    def __init__(self, value, category, description=None):
        self.value = value
        self.category = category
        self.description = description

    def __repr__(self):
        return f"{self.SIGN}{self.value}-{self.category}"


class IncomeCategory(Base):
    INCOMES = ("Deposits", "Salary", "Savings")


class ExpenseCategory(Base):
    EXPENSES = (
        "Bills",
        "Car",
        "Clothes",
        "Food",
        "Transportation",
        "Health",
        "Gifts",
        "Gym",
        "Pets",
        "Phones",
    )
