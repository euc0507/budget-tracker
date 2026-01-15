class Transaction:
    def __init__(self, amount, date, tagname, monthid, description = ""):
        pass


class Tag:
    def __init__(self, name, limit):
        self.transactions = []

    def total_spent(self):
        pass

    def add_transaction(self):
        pass

    def remaining_budget(self):
        pass

    def percent_used(self):
        pass


class BudgetMonth:
    def __init__(self, monthid, income):
        tags = []
        transactions = []

    def add_tag(self, tag):
        pass

    def add_transaction(self, transaction):
        pass

    def total_spent(self):
        pass

    def remaining_income(self):
        pass

    def get_tag_by_name(self, tagname):
        pass

