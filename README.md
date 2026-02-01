# Python Budget Tracker

**A command-line budgeting application built in Python that allows users to track spending by category, persist financial data across sessions, and analyze monthly spending patterns.**

---

## Overview

Python Budget Tracker is a CLI-based personal finance tool that helps users organize their spending into customizable categories, record transactions, and monitor balances over time. The application is designed with persistent storage and monthly tracking logic, allowing users to close and reopen the program without losing data.


---

## Features

- Create, edit, and delete spending categories  
- Assign optional spending limits to categories  
- Record transactions with timestamps and descriptions  
- Automatically track monthly spending periods  
- View balances and transaction history per category  
- Export financial data to CSV  
- Persistent storage across program runs  
- Unit-tested core financial calculations  

---

## Technical Highlights

- **Object-Oriented Design**  
  Categories are modeled using a dedicated `Category` class, encapsulating category data and behavior.

- **Persistent Data Storage**  
  Categories and transactions are stored in CSV files and reconstructed on program startup.

- **Stable Data Relationships**  
  Each category is assigned a unique ID, allowing category names to be changed without breaking transaction history.

- **Time-Based Logic**  
  Transactions are grouped into monthly periods using timestamps, ensuring accurate monthly budget tracking.

- **Test Coverage**  
  Core financial logic is verified using `pytest` to ensure balance calculations and category filtering remain correct during refactoring.

---

## Architecture Overview

- **`project.py`** – Main entry point and CLI menu logic  
- **`classes.py`** – Defines the `Category` class and category-related behavior  
- **`storage.py`** – Handles reading and writing persistent data to CSV files  
- **`test_project.py`** – Unit tests for balance calculations and filtering logic  

Transactions are stored as structured dictionaries containing category IDs, amounts, timestamps, and optional descriptions.

---

## Technologies Used

- Python 3  
- `colorama` for CLI readability  
- `tabulate` for formatted tables  
- `pytest` for unit testing  
- CSV-based persistence  

---

## Future Improvements

- Add data visualization
- Add command-line arguments support
- Migrate storage from CSV to a database  

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/euc0507/budget-tracker
   cd budget-tracker

2. Install dependencies:
    pip install -r requirements.txt

3. Run the program:
    python project.py

