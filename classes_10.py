class Budget:
    
    def __init__(self, expense_type):
        self.expense_type = expense_type
        self.expenses_dict = {}

    def add_expense(self, name, amount):
        """Add one expense entry (e.g., 'Milk', 10.5)"""
        self.expenses_dict[name] = float(amount)

    def get_expenses(self):
        """Return total of all expenses"""
        return sum(self.expenses_dict.values())

    def get_expenses_list(self):
        """Return dictionary of expense items"""
        return self.expenses_dict

    def write_to_file(self):
        with open("data.txt", "a") as data:
            data.write(f"\n{self.expense_type} Expenses:\n")
            for name, amount in self.expenses_dict.items():
                data.write(f"{name} : ${amount:.2f}\n")
