# budget_tracker.py
transactions = []

def show_menu():
        print("\nBudget Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Summary")
        print("5. Quit")

def add_income():
    try:
        amount = float(input("Enter income amount: "))
        category = input("Enter category (e.g., paycheck): ")
        transactions.append({"type": "income", "amount": amount, "category": category})
        print(f"Added ${amount:.2f} to {category}")
    except ValueError:
        print(f"Please enter a valid number for amount.")

def add_expense():
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter category (e.g., Food): ")
        transactions.append({"type": "expense", "amount": amount, "category": category})
        print(f"Added ${amount:.2f} to {category}")
    except ValueError:
        print(f"Please enter a valid number for amount.")

def get_balance():
    balance = 0
    for t in transactions:
        if t ["type"] == "income":
            balance += t["amount"]
        else:
            balance -= t["amount"]
    print(f"Current balance: ${balance:.2f}")

def get_summary():
    categories = {}
    for t in transactions:
        if t ["type"] == "expense":
            cat = t["category"]
            categories[cat] = categories.get(cat, 0) + t["amount"]
    for cat, total in categories.items():
        print(f"{cat}: ${total:.2f}")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5)")
        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            get_balance()
        elif choice == "4":
            get_summary()
        elif choice == "5":
            print("See Ya!")
            break
        else:
            print("Invalid choice, please select 1-5.")

if __name__ == "__main__":
    main()


