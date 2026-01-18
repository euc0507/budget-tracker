from classes import Category
import csv
def export_transactions(transactions=[], filename="transactions.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["category", "amount", "description", "time"]
        )
        writer.writeheader()
        for t in transactions:
            writer.writerow({
                "category": t["category"],
                "amount": t["amount"],
                "description": t["description"],
                "time": t["time"].isoformat()
            })
    
    print(f"Transactions exported to {filename}")


