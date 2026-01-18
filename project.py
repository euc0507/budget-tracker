import sys
import csv 
import datetime
from colorama import init, Fore, Style
init(autoreset=True)
from tabulate import tabulate
from classes import Category
from storage import export_transactions


#list to store all categories    
categories = []
#category related functions
def add_new_category(categories):
    print(Fore.CYAN + "\nEnter 'b' to go back")
    name = input("Category name: ")
    if name.lower() == "b":
        return
    category_exists = False
    for category in categories:
        if name.lower() == category.name.lower():
            category_exists = True
            break
    
    if category_exists:
        print(Fore.RED + f"Error: Category {name} already exists.")
        input(Fore.YELLOW + "Press Enter to continue: ")
    else:
        while True:
            try:
                limit = float(input("Category limit: $"))
                if limit <= 0:
                    raise ValueError
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a positive number")
                continue
            new_category = Category(name, limit)
            categories.append(new_category)
            print(Fore.GREEN + f"Category {name} with limit ${limit:.2f} created.")
            input(Fore.YELLOW + "Press Enter to continue: ")
            break

def edit_category(categories):
    enumerated_categories = {i+1: cat for i, cat in enumerate(categories)}
    print("\nSelect a category to edit:")
    for idx, cat in enumerated_categories.items():
        print(f"{idx}) {cat.name} (Limit: ${cat.limit:.2f})")
    try:
        print(Fore.CYAN + "\nEnter 'b' to go back")
        choice = (input("Enter the number of the category: "))
        if choice == 'b':
            return
        else:
            choice = int(choice)
        if choice not in enumerated_categories:
            raise ValueError
        selected_category = enumerated_categories[choice]
        print("1) Change name")
        print("2) Change limit")
        edit_choice = input("Choose an option (1-2): ")
        if edit_choice == "1":
            new_name = input("Enter new category name: ")
            selected_category.change_name(new_name)
            print(Fore.GREEN + f"\nCategory name changed to {new_name}.")
            input(Fore.YELLOW + "\nPress Enter to continue: ")
        elif edit_choice == "2":
            while True:
                try:
                    new_limit = float(input("Enter new category limit: $"))
                    if new_limit <= 0:
                        raise ValueError
                    selected_category.change_limit(new_limit)
                    print(Fore.GREEN + f"\nCategory limit changed to ${new_limit:.2f}.")
                    input(Fore.YELLOW + "\nPress Enter to continue: ")
                    break
                except ValueError:
                    print(Fore.RED + "Invalid input. Please enter a positive number")
                    input(Fore.YELLOW + "Press Enter to continue: ")
    except ValueError:
        print(Fore.RED + "Invalid selection.")
        


def total_limit(categories):
    """
    Calculate the combined spending limit across all categories that the user has created.
    """
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
def write_transactions_to_file(filename="transactions.csv"):
    """
    Writes all transactions to a CSV file.
    This function runs at the end of the program to save all recorded transactions.
    """
    with open(filename, "w", newline="") as file:
        fieldnames = ["category", "amount", "description", "time"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for transaction in transactions:
            writer.writerow({
                "category": transaction["category"],
                "amount": transaction["amount"],
                "description": transaction["description"],
                "time": transaction["time"].strftime("%Y-%m-%d %H:%M:%S"),
            })

def read_transactions_from_file(filename="transactions.csv"):
    """
    Reads transactions from a CSV file and populates the transactions list.
    This function runs at the start of the program to load previously recorded transactions.
    """
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                category = row["category"]
                amount = float(row["amount"])
                description = row["description"]
                time_of_transaction = datetime.datetime.strptime(row["time"], "%Y-%m-%d %H:%M:%S")
                transaction = log_transaction(category, amount, time_of_transaction, description)
                transactions.append(transaction)
    except FileNotFoundError:
        pass


def record_expense(transactions):
    """
    Prompts the user to record a new transaction
    - Asks the user to select category, either by name or number
    - Prompts the user for amount spent and optional description
    - Validates input
    - Stores transaction in transaction list, with timestamp
    - Displays updated balance and warnings if limits are approached or exceeded
    """
    while True:
        enumerated_categories = {i+1: cat for i, cat in enumerate(categories)}
        print("\nAvailable categories:")
        for idx, cat in enumerated_categories.items():
            print(f"{idx}) {cat.name} (Limit: ${cat.limit:.2f})")
        print(Fore.CYAN + "\nEnter 'b' to go back")
        category_name = input("Enter the category name or number: ").strip().lower()
        if category_name == 'b':
            return
        if category_name.isdigit():
            category_index = int(category_name)
            if category_index in enumerated_categories:
                category_name = enumerated_categories[category_index].name.lower()
            else:
                print(Fore.RED + "Category not found")
                input(Fore.YELLOW + "Press Enter to continue: ")
                break
        target_category = next((category for category in categories if category.name.lower() == category_name), None)
        if target_category:
            while True:
                try:
                    amount = float(input("Amount: $"))
                    if amount <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print(Fore.RED + "Invalid amount")
                    continue
            description = input("Description (Optional): ")
            time_of_transaction = datetime.datetime.now()
            new_transaction = log_transaction(category_name, amount, time_of_transaction, description)
            transactions.append(new_transaction)
            print(Fore.GREEN + f"\nRecorded transaction of ${amount:.2f} from category {category_name}.")
            balance = compute_balance(target_category, transactions)
            print(Fore.GREEN + f"You have ${balance:.2f} remaining in your {category_name} budget.")
            percent = balance_percentage(target_category, transactions)
            if percent >= 100:
                print(Fore.RED + f"⚠️  Alert: You have exceeded your budget for {category_name}!")
            elif percent >= 80:
                print(Fore.YELLOW + f"⚠️  Warning: You have used {percent:.0f}% of your budget for {category_name}!")
            input(Fore.YELLOW + "\nPress Enter to continue: ")
            return
            
        else:
            print(Fore.RED + "Category not found")
            input(Fore.YELLOW + "\nPress Enter to continue: ")
            break
    
def log_transaction(category, amount, date_time,description=""):
    """
    Returns transaction as a dictionary
    """
    return {
        "category":category, 
        "amount":amount, 
        "description":description, 
        "time":date_time
        }

def transactions_by_category(transactions, category_name):
    """
    Returns transactions filtered by category name
    """
    return [t for t in transactions if t["category"].lower() == category_name.lower()]

def tabulate_transactions(transactions):
    """
    Displays transactions formatted into a table, using tabulate library
    """
    table = []
    for t in transactions:
        table.append([
            t["category"],
            f"${t['amount']:.2f}",
            t["description"] if t["description"] else "N/A",
            t["time"].strftime("%Y-%m-%d %H:%M:%S")
        ])
    headers = ["Category", "Amount", "Description", "Time"]
    print(tabulate(table, headers, tablefmt="grid"))

#main
def main():
    """
    Main program loop
    - Loads categories and transactions from files
    - Displays menu and prompts user for actions
    - On exit, saves categories and transactions to files
    """
    read_categories_from_file()
    read_transactions_from_file()
    while True:
        print("\nWelcome! What would you like to do?")
        print("1) Create a category")
        print("2) Edit category")
        print("3) View category balances")
        print("4) Record a transaction")
        print("5) View transactions")
        print("6) View total spent")
        print("7) Export transactions")
        print("8) Exit")
        response = input("Choose an option (1-8): ")
        if response == "1":
            add_new_category(categories)
        elif response == "2":
            if categories:
                edit_category(categories)
            else:
                print(Fore.RED + "No categories have been created")
                input(Fore.YELLOW + "Press Enter to continue: ")
        elif response == "3":
            if categories:
                for category in categories:
                    balance = compute_balance(category, transactions)
                    percent = balance_percentage(category, transactions)
                    print(f"\n-{category.name}: ${balance:.2f} remaining out of ${category.limit:.2f}")
                    print(f"You have used {percent:.0f}% of your budget for {category.name}")
                input(Fore.YELLOW + "\nPress Enter to continue: ")
            else:
                print(Fore.RED + "\nNo categories have been created")
                input(Fore.YELLOW + "Press Enter to continue: ")

        elif response == "4":
            record_expense(transactions)

        elif response == "5":
            if transactions:
                print("\nWould you like to see:")
                print("1) All transactions")
                print("2) Transactions by category")
                sub_response = input("Choose an option (1-2): ")
                if sub_response == "1":
                    print()
                    tabulate_transactions(transactions)
                    input(Fore.YELLOW + "\nPress Enter to continue: ")
                    
                elif sub_response == "2":
                    print("\nAvailable categories:")
                    for category in categories:
                        print(f"- {category.name}")
                    category_name = input("Enter the category name: ").strip().lower()
                    filtered_transactions = transactions_by_category(transactions, category_name)
                    if filtered_transactions:
                        print()
                        tabulate_transactions(filtered_transactions)
                        input(Fore.YELLOW + "\nPress Enter to continue: ")
                    else:
                        print(Fore.RED + f"\nNo transactions found for category '{category_name}'")
                        input(Fore.YELLOW + "Press Enter to continue: ")
                
            else:
                print(Fore.RED + "\nYou have not recorded any transactions")
                input(Fore.YELLOW + "Press Enter to continue: ")

        elif response == "6":
            total = sum(t["amount"] for t in transactions)
            print(f"\nYou have spent a total of ${total:.2f} out of ${total_limit(categories):.2f}")
            print(f"You have ${total_limit(categories) - total:.2f} remaining")
            input(Fore.YELLOW + "\nPress Enter to continue: ")

        elif response == "7":
            if transactions:
                export_transactions(transactions)
                input(Fore.YELLOW + "Press Enter to continue: ")
            else:
                print(Fore.RED + "You have no transactions to export")
                input(Fore.YELLOW + "Press Enter to continue: ")

        elif response == "8":
            write_categories_to_file()
            write_transactions_to_file()
            sys.exit(Fore.GREEN + "Goodbye!")

        else:
            print(Fore.RED + "Invalid. Please enter 1-5")
            input(Fore.YELLOW + "Press Enter to continue")

if __name__ == "__main__":
    main()