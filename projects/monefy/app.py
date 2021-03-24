from random import choice
from projects.monefy.account import Account
from projects.monefy.expense import Expense
from projects.monefy.income import Income
from projects.monefy.category import ExpenseCategory

if __name__ == "__main__":
    john = Account()
    income_transaction = Income(value=8, income_category="Salary")
    expense_transaction = Expense(
        value=12, expense_category=choice(ExpenseCategory.EXPENSE)
    )
    john.calc_income(income_transaction)
    john.calc_expense(expense_transaction)
