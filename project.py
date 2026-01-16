import sys
import csv
from classes import Tag




#list to store all tags    
tags = []

def main():
    while True:
        print("\nWelcome, choose an option: ")
        print("1) Create a tag")
        print("2. View tag balances")
        print("3. Record an expense")
        print("4. Exit")
        response = input("Choose an option (1-4): ")
        if response == "1":
            name = input("Tag name: ")
            limit = int(input("Tag limit: "))
            new_tag = Tag(name, limit)
            tags.append(new_tag)
            print(f"Tag {name} with limit {limit} created.")

        elif response == "2":
            if tags:
                for tag in tags:
                    print(f"-{tag.name}: Remaining balance is {tag.balance}")

        elif response == "3":
            tag_name=input("Tag: ")
            target_tag = next((tag for tag in tags if tag.name == tag_name), None)
            if target_tag:
                amount = int(input("Amount: "))
                description = input("Description (Optional):")
                target_tag.change_balance(amount)
            else:
                print("Tag not found")
                continue

        elif response == "4":
            sys.exit("Goodbye!")

if __name__ == "__main__":
    main()