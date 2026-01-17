

class Category:
    transactions = []
    def __init__(self, name, limit=0):
        self.name = name
        self.limit = limit
        self.balance = limit


    def change_balance(self, amount):
        self.balance = self.limit - amount

def log_transaction(category, amount, date_time,description=""):
    return {"category":category, "amount":amount, "description":description, "time":date_time}
