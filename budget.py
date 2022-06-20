#this code is a module that can be used in other python programs with "import budget"

class BudgetManager:
    def __init__(self, amount):
        self.available = amount
        self.budgets = {}
        self.expenditure = {}

    def add_budget(self, name, amount): #funct that adds to the budget
        global available
        if name in self.budgets:
            raise ValueError("Budget exists") #leaves funct immediately with an exception
        if amount > self.available:
            raise ValueError("Insufficient funds")
        self.budgets[name] = amount #stores the budgeted amount in the budgets dict
        self.available -= amount
        self.expenditure[name] = []
        return self.available

    def change_budget(self, name, new_amount):
        if name not in self.budgets:
            raise ValueError("Budget does not exiat")
        old_amount = self.budgets[name]
        if new_amount > old_amount + self.available:
            raise ValueError("Insufficient funds")
        self.budgets[name] = new_amount
        self.available -= new_amount - old_amount
        return self.available

    def spend(self, name, amount):
        if name not in self.expenditure:
            raise ValueError("No such budget")
        self.expenditure[name].append(amount)
        budgeted = self.budgets[name]
        spent = sum(self.expenditure[name])
        return budgeted - spent

    def print_summary(self):
        print("Budget            Budgeted      Spent  Remaining")
        print("--------------- ---------- ---------- ----------")
        total_budgeted = 0
        total_spent = 0
        total_remaining = 0
        for name in self.budgets:
            budgeted = self.budgets[name]
            spent = self.expenditure[name]
            remaining = budgeted - spent
            print(f'{name:15s} {budgeted:10.2f} {spent:10.2f} ', f'{remaining:10.2f}')
            total_budgeted += budgeted
            total_spent += sum(self.expenditure[name])
            total_remaining += remaining
        print("--------------- ---------- ---------- ----------")
        print(f'{name:15s} {total_budgeted:10.2f} {total_spent:10.2f} ', f'{total_remaining:10.2f}')
