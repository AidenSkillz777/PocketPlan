from expense import Expense
#expenses : list[Expense] = []
#total_expenses = 0

#Empty List, No Params
class ExpenseTracker:
    def __init__(self):
        self.expenses : list[Expense] = []

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)

    def remove_expense(self, expense: Expense):
        self.expenses.remove(expense)

    def calculate_total(self):
        return sum(expense.amount for expense in self.expenses)