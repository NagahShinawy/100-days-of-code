from random import choice, randint
from projects.monefy.account import Account
from projects.monefy.expense import Expense
from projects.monefy.income import Income
from projects.monefy.category import ExpenseCategory, IncomeCategory

if __name__ == "__main__":
    john = Account()

    income = Income(
        value=randint(1, 10), income_category=choice(IncomeCategory.INCOMES)
    )
    expense = Expense(
        value=randint(1, 10), expense_category=choice(ExpenseCategory.EXPENSES)
    )
    john.calc_income(income)
    john.calc_expense(expense)
