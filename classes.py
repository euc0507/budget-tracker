

class Category:
    transactions = []
    def __init__(self, name, limit=0):
        self.name = name
        self.limit = limit
        self.balance = limit
        self.total_spent = 0


    def change_balance(self, amount):
        self.balance = self.balance - amount
        self.total_spent += amount

    def balance_percentage(self):
        return self.total_spent/self.limit * 100


