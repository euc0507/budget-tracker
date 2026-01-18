"""
Domain models for the budget tracker.

Contains the Category class and related logic.
"""

class Category:
    next_id = 1
    def __init__(self, name, limit=0, _id=None):
        self.name = name
        self.limit = limit
        self._id = _id if _id is not None else Category.next_id
        Category.next_id += 1

    def change_limit(self, new_limit):
        self.limit = new_limit

    def change_name(self, new_name):
        self.name = new_name

    @property
    def id(self):
        return self._id