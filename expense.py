class Expense:
    def __init__(self, description: str, amount: float, category: str):
        self.description = description
        self.amount = amount
        self.category = category

    def __str__(self):
        return "Description: " + str(self.description) + ", Cost: " + str(self.amount) + ", Category: " + str(self.category)