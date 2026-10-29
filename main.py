from expense import Expense
from expense_tracker import ExpenseTracker

expense1 = Expense("Groceries", 30, "IMPORTANT")
expense2 = Expense("Phone Bill", 20, "Monthly")
expense3 = Expense("Shoes", 110, "Next Year")

tracker = ExpenseTracker()

tracker.add_expense(expense1)
tracker.add_expense(expense2)
tracker.add_expense(expense3)

x = tracker.calculate_total()
print(x)
print(expense1)