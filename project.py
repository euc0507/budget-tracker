import sys
import csv
from classes import Category, log_transaction




#list to store all categories    
categories = []
def add_new_category(categories):
    name = input("Category name: ")
    category_exists = False
    for category in categories:
        if name.lower() == category.name.lower():
            category_exists = True
            break
    
    if category_exists:
        print(f"Error: Category {name} already exists.")
    else:
        try:
            limit = float(input("Category limit: "))
        except ValueError:
            print("Invalid input. Please enter a positive number")
            return
        new_category = Category(name, limit)
        categories.append(new_category)
        print(f"Category {name} with limit {limit} created.")


#list to store transactions
transactions = []
def record_expense(transactions):
    category_name=input("Category: ")
    target_category = next((category for category in categories if category.name.lower() == category_name.lower()), None)
    if target_category:
        amount = int(input("Amount: "))
        description = input("Description (Optional):")
        target_category.change_balance(amount)
        new_transaction = log_transaction(category_name, amount, description)
        transactions.append(new_transaction)
    else:
        print("Category not found")
        return


def main():
    while True:
        print("\nWelcome, choose an option: ")
        print("1) Create a category")
        print("2) View category balances")
        print("3) Record an expense")
        print("4) View transactions")
        print("5) Exit")
        response = input("Choose an option (1-5): ")
        if response == "1":
            add_new_category(categories)
        elif response == "2":
            if categories:
                for category in categories:
                    print(f"-{category.name}: Remaining balance is {category.balance}")
            else:
                print("No categories have been created")

        elif response == "3":
            record_expense(transactions)

        elif response == "4":
            pass

        elif response == "5":
            sys.exit("Goodbye!")

if __name__ == "__main__":
    main()