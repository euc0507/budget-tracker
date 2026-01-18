

class Category:
    def __init__(self, name, limit=0):
        self.name = name
        self.limit = limit

    def change_limit(self, new_limit):
        self.limit = new_limit

    def change_name(self, new_name):
        self.name = new_name