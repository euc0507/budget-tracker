from classes import Tag
from storage import load_transactions, save_transactions
import csv
import datetime
import sys

#Load existing transactions
all_transactions = load_transactions()

#Build tags from transactions
tags = {}
for t in all_transactions:
    if t.tag not in tags:
        tags[t.tag] = Tag(t.tag)
    tags[t.tag].transactions.append(t)

def main():
    while True:
        print("\nBudget Tracker Menu")
        print("1. Create Tag")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Balance")
        print("5. Exit")
        choice = input("Select an option: ").strip()



if __name__ == "__main__":
    main()