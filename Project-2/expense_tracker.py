expenses = []

def add_expense():
    desc = input("Expense description: ").strip()
    try:
        amount = float(input("Amount: ").strip())
    except ValueError:
        print("Invalid amount.")
        return
    expenses.append((desc, amount))
    print("Expense added.")

def view_expenses():
    print("Expenses:")
    for i, (d, a) in enumerate(expenses, start=1):
        print(f"{i}. {d} - ${a:.2f}")

def total_expenses():
    total = sum(a for _, a in expenses)
    print(f"Total: ${total:.2f}")

def main():
    while True:
        print("\n1. Add expense\n2. View expenses\n3. Total\n4. Exit")
        ch = input("Choice: ").strip()
        if ch == "1":
            add_expense()
        elif ch == "2":
            view_expenses()
        elif ch == "3":
            total_expenses()
        elif ch == "4":
            break
        else:
            print("Invalid.")

if __name__ == "__main__":
    main()