import json
import os

# Define the file name for persistent storage
FILE_NAME = 'expenses.json'

def initialize_data():
    """Check if the JSON file exists; if not, create it with an empty list."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w') as file:
            json.dump([], file)
        return []
    
    # If it exists, read and return the data
    with open(FILE_NAME, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            # Handle the case where the file is completely empty or corrupted
            return []

def save_data(expenses):
    """Save the expenses list to the JSON file."""
    with open(FILE_NAME, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    """Prompt user for an item and amount, then save it."""
    item = input("Enter expense description (e.g., Coffee): ")
    
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid input! Please enter a valid number for the amount.")
        return

    # Data structure requirement: Dictionary containing item and amount
    expense_entry = {"item": item, "amount": amount}
    expenses.append(expense_entry)
    
    # Save immediately after adding
    save_data(expenses)
    print(f"Success! c '{item}' for {amount:.2f} naira.") #I couldn't find the naira sign on my laptop

def view_all_expenses(expenses):
    """Format and print all expenses from the list."""
    if not expenses:
        print("\nNo expenses found. Your tracker is empty!")
        return

    print("\n--- Your Expenses ---")
    total = 0.0
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['item']} - ${expense['amount']:.2f}")
        total += expense['amount']
    
    print("-" * 21)
    print(f"Total Spent: ${total:.2f}")
    print("-" * 21)

def main():
    # 1. Initialize JSON requirement
    expenses = initialize_data()

    # 2. User Menu requirement
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All")
        print("3. Exit")
        
        choice = input("Select an option (1/2/3): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_all_expenses(expenses)
        elif choice == '3':
            print("Exiting Expense Tracker. Have a great day!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()