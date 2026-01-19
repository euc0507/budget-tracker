from classes import Category
import datetime
import csv

def read_transactions_from_file(filename="transactions.csv"):
    """
    Reads transactions from a CSV file and populates the transactions list.
    This function runs at the start of the program to load previously recorded transactions.
    """
    try:
        transactions = []
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                category = int(row["category_id"])
                amount = float(row["amount"])
                description = row["description"]
                time_of_transaction = datetime.datetime.strptime(row["time"], "%Y-%m-%d %H:%M:%S")
                period = row["period"]
                transaction = log_transaction(category, amount, time_of_transaction, description, period)
                transactions.append(transaction)
    except FileNotFoundError:
        pass
    return transactions


def write_transactions_to_file(transactions,filename="transactions.csv"):
    """
    Writes all transactions to a CSV file.
    This function runs at the end of the program to save all recorded transactions.
    """
    with open(filename, "w", newline="") as file:
        fieldnames = ["category_id", "amount", "description", "time", "period"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for transaction in transactions:
            writer.writerow({
                "category_id": transaction["category_id"],
                "amount": transaction["amount"],
                "description": transaction["description"],
                "time": transaction["time"].strftime("%Y-%m-%d %H:%M:%S"),
                "period": transaction["period"]
            })

def log_transaction(category_id, amount, date_time, description="", period=None):
    """
    Creates and returns a transaction as a dictionary.
    """
    if period is None:
        period = date_time.strftime("%Y-%m")
    return {
        "category_id": category_id,
        "amount": amount,
        "description": description,
        "time": date_time,
        "period": period
    }

#Categories storage functions
def read_categories_from_file(filename="categories.csv"):
    categories = []
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"]
                limit = float(row["limit"])
                id = int(row["id"])
                category = Category(name, limit, _id=id)
                categories.append(category)
    except FileNotFoundError:
        pass
    return categories


def write_categories_to_file(categories,filename="categories.csv"):
    with open(filename, "w", newline="") as file:
        fieldnames = ["name", "limit", "id"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for category in categories:
            writer.writerow({
                "name": category.name,
                "limit": category.limit,
                "id": category.id
            })
