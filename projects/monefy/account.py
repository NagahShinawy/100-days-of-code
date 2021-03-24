from projects.monefy.expense import Expense
from projects.monefy.income import Income


class Account:
    def __init__(self):
        self.incomes = 0
        self.expense = 0
        self.balance = 0

    def calc_expense(self, expense: Expense):
        if expense.value > self.balance:
            print("Your Balance not enough")

        else:
            self.balance -= expense.value

    def calc_income(self, income: Income):
        self.balance += income.value

    @property
    def show_balance(self):
        return self.balance
