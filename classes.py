

class Tag:
    def __init__(self, name, limit=0):
        self.name = name
        self.limit = limit
        self.balance = limit


    def change_balance(self, amount):
        self.balance = self.limit - amount