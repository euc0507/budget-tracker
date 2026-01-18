

class Category:
    def __init__(self, name, limit=0):
        self.name = name
        self.limit = limit
        self.balance = limit
        self.total_spent = 0
        self.transactions = []


    def change_balance(self, amount):
        self.balance = self.balance - amount
        self.total_spent += amount
        if self.balance < 0:
            print(f"Warning: You have exceeded your budget limit for {self.name}!")
        elif self.balance_percentage() >= 80:
            print(f"Warning: You have used {self.balance_percentage():.2f}% of your budget for {self.name}!")

    def balance_percentage(self):
        return self.total_spent/self.limit * 100


