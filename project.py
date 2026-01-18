import sys
import csv
import datetime
from classes import Category
from storage import export_transactions


#list to store all categories    
categories = []
#category related functions
def add_new_category(categories):
    name = input("Category name: ")
    category_exists = False
    for category in categories:
        if name.lower() == category.name.lower():
            category_exists = True
            break
    
    if category_exists:
        print(f"Error: Category {name} already exists.")
        input("Press Enter to continue: ")
    else:
        while True:
            try:
                limit = float(input("Category limit: $"))
                if limit <= 0:
                    raise ValueError
            except ValueError:
                print("Invalid input. Please enter a positive number")
                continue
            new_category = Category(name, limit)
            categories.append(new_category)
            print(f"Category {name} with limit ${limit:.2f} created.")
            input("Press Enter to continue: ")
            break


def total_limit(categories):
    return sum(category.limit for category in categories)

def total_spent_in_category(category, transactions):
    return sum(t["amount"] for t in transactions if t["category"].lower() == category.name.lower())

def compute_balance(category, transactions):
    return category.limit - total_spent_in_category(category, transactions)

def balance_percentage(category, transactions):
    spent = total_spent_in_category(category, transactions)
    return (spent / category.limit * 100) if category.limit else 0


def read_categories_from_file(filename="categories.csv"):
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"]
                limit = float(row["limit"])
                category = Category(name, limit)
                categories.append(category)
    except FileNotFoundError:
        pass


def write_categories_to_file(filename="categories.csv"):
    with open(filename, "w", newline="") as file:
        fieldnames = ["name", "limit"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for category in categories:
            writer.writerow({
                "name": category.name,
                "limit": category.limit,
            })


#list to store transactions
transactions = []
#Transactions related functions
def record_expense(transactions):
    while True:
        category_name=input("Category: ").strip().lower()
        target_category = next((category for category in categories if category.name.lower() == category_name), None)
        if target_category:
            while True:
                try:
                    amount = float(input("Amount: $"))
                    if amount <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid amount")
                    continue
            description = input("Description (Optional): ")
            time_of_transaction = datetime.datetime.now()
            new_transaction = log_transaction(category_name, amount, time_of_transaction, description)
            transactions.append(new_transaction)
            print(f"Recorded expense of ${amount:.2f} from category {category_name}.")
            balance = compute_balance(target_category, transactions)
            print(f"You have ${balance:.2f} remaining in your {category_name} budget.")
            percent = balance_percentage(target_category, transactions)
            if percent >= 100:
                print(f"⚠️  Alert: You have exceeded your budget for {category_name}!")
            elif percent >= 80:
                print(f"⚠️  Warning: You have used {percent:.0f}% of your budget for {category_name}!")
            input("Press Enter to continue: ")
            return
            
        else:
            print("Category not found")
            input("Press Enter to continue: ")
            break
    
def log_transaction(category, amount, date_time,description=""):
    return {
        "category":category, 
        "amount":amount, 
        "description":description, 
        "time":date_time
        }

#main
def main():
    read_categories_from_file()
    while True:
        print("\nWelcome, choose an option: ")
        print("1) Create a category")
        print("2) View category balances")
        print("3) Record an expense")
        print("4) View transactions")
        print("5) View total spent")
        print("6) Export transactions")
        print("7) Exit")
        response = input("Choose an option (1-7): ")
        if response == "1":
            add_new_category(categories)
        elif response == "2":
            if categories:
                for category in categories:
                    balance = compute_balance(category, transactions)
                    percent = balance_percentage(category, transactions)
                    print(f"-{category.name}: ${balance:.2f} remaining out of ${category.limit:.2f}")
                    print(f"You have used {percent:.0f}% of your budget for {category.name}")
                input("Press Enter to continue: ")
            else:
                print("No categories have been created")
                input("Press Enter to continue: ")

        elif response == "3":
            record_expense(transactions)

        elif response == "4":
            if transactions:
                for transaction in transactions:
                    print(f"You spent ${transaction['amount']:.2f} from your {transaction['category']} budget")
                    if transaction['description']:
                        print(f"on {transaction['description']}")
                    print(f"Date: {transaction['time'].strftime('%Y-%m-%d %H:%M:%S')}")
                input("Press Enter to continue: ")
            else:
                print("You have not logged any transactions")
                input("Press Enter to continue: ")

        elif response == "5":
            total = sum(t["amount"] for t in transactions)
            print(f"You have spent a total of ${total:.2f} out of ${total_limit(categories):.2f}")
            print(f"You have ${total_limit(categories) - total:.2f} remaining")
            input("Press Enter to continue: ")

        elif response == "6":
            if transactions:
                export_transactions(transactions)
                input("Press Enter to continue: ")
            else:
                print("You have no transactions to export")
                input("Press Enter to continue: ")

        elif response == "7":
            write_categories_to_file()
            sys.exit("Goodbye!")

        else:
            print("Invalid. Please enter 1-5")
            input("Press Enter to continue")

if __name__ == "__main__":
    main()