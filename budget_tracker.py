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

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5)")
        if choice == "1":
            add_income()
        elif choice == "5":
            print("See Ya!")
            break
        else:
            print("Feature coming soon!")

if __name__ == "__main__":
    main()


