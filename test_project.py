from project import total_spent_in_category, compute_balance, balance_percentage
from classes import Category

def test_total_spent_in_category():
    transactions = [
        {"category_id": 1, "amount": 50.0, "description": "groceries", "time": "2026-01-10 12:00:00", "period": "2026-01"},
        {"category_id": 1, "amount": 30.0, "description": "dining out", "time": "2026-01-15 18:00:00", "period": "2026-01"},
        {"category_id": 2, "amount": 20.0, "description": "movie", "time": "2026-01-20 20:00:00", "period": "2026-01"},
    ]

    cat1 = Category("Food", 100, _id=1)
    cat2 = Category("Entertainment", 50, _id=2)
    cat3 = Category("Utilities", 200, _id=3)

    assert total_spent_in_category(cat1, transactions) == 80.0
    assert total_spent_in_category(cat2, transactions) == 20.0
    assert total_spent_in_category(cat3, transactions) == 0.0

def test_compute_balance():
    transactions = [
        {"category_id": 1, "amount": 70.0, "description": "groceries", "time": "2026-01-05 14:00:00", "period": "2026-01"},
        {"category_id": 1, "amount": 40.0, "description": "dining out", "time": "2026-01-12 19:00:00", "period": "2026-01"},
    ]

    cat = Category("Food", 150, _id=1)

    balance = compute_balance(cat, transactions)

    assert balance == 40.0


def test_balance_percentage():
    transactions = [
        {"category_id": 1, "amount": 60.0, "description": "groceries", "time": "2026-01-08 13:00:00", "period": "2026-01"},
        {"category_id": 1, "amount": 30.0, "description": "dining out", "time": "2026-01-18 20:00:00", "period": "2026-01"},
    ]

    cat = Category("Food", 120, _id=1)

    percentage = balance_percentage(cat, transactions)

    assert percentage == 75.0