import sys
import csv
import datetime
from classes import Category


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
        input("Press Enter to continue: ")
    else:
        while True:
            try:
                limit = float(input("Category limit: "))
            except ValueError:
                print("Invalid input. Please enter a positive number")
                input("Press Enter to continue: ")
                continue
            new_category = Category(name, limit)
            categories.append(new_category)
            print(f"Category {name} with limit {limit:.2f} created.")
            input("Press Enter to continue: ")
            break


#list to store transactions
transactions = []
#Transactions related functions
def record_expense(transactions):
    while True:
        category_name=input("Category: ")
        target_category = next((category for category in categories if category.name.lower() == category_name.lower()), None)
        if target_category:
            amount = int(input("Amount: $"))
            description = input("Description (Optional): ")
            target_category.change_balance(amount)
            time_of_transaction = datetime.datetime.now()
            new_transaction = log_transaction(category_name, amount, time_of_transaction, description)
            transactions.append(new_transaction)
            return
            
        else:
            print("Category not found")
            input("Press Enter to continue: ")
            continue
    
def log_transaction(category, amount, date_time,description=""):
    return {"category":category, "amount":amount, "description":description, "time":date_time}


#main
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
                    print(f"-{category.name}: Remaining balance is ${category.balance:.2f}")
                    print(f"You have used {category.balance_percentage()}% of your {category.name} budget for this month")
                input("Press Enter to continue: ")
            else:
                print("No categories have been created")
                input("Press Enter to continue: ")

        elif response == "3":
            record_expense(transactions)

        elif response == "4":
            if transactions:
                for transaction in transactions:
                    print(f"You spent ${transaction["amount"]:.2f} from your {transaction["category"]} budget")
                    if transaction["description"]:
                        print(f"on {transaction["description"]}")
                    print(f"Date: {transaction["time"]}")
                input("Press Enter to continue: ")
            else:
                print("You have not logged any transactions")
                input("Press Enter to continue: ")

        elif response == "5":
            sys.exit("Goodbye!")

        else:
            print("Invalid. Please enter 1-5")
            input("Press Enter to continue")

if __name__ == "__main__":
    main()