from datetime import datetime

class Transaction:
    def __init__(self, tag, amount, t_type, description="", date=None):
        self.tag = tag
        self.amount = amount
        self.type = t_type  # "deposit" or "withdraw"
        self.description = description
        self.date = date or datetime.now()


class Tag:
    def __init__(self, name):
        self.name = name
        self.transactions=[]

    def deposit(self, amount, description=""):
        t = Transaction(self.name, amount, "deposit", description)
        self.transactions.append(t)

    def withdraw(self, amount, description=""):
        pass

    def balance(self):
        pass