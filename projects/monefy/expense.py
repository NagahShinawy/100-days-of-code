from projects.monefy.category import ExpenseCategory


class Expense(ExpenseCategory):
    SIGN = "-"

    def __init__(self, value, expense_category, description=None):
        super().__init__(
            value=value, category=expense_category, description=description
        )
