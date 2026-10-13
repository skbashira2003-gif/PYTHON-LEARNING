
import csv
import os
import matplotlib.pyplot as plt

FILE_NAME = "expenses.csv"


def add_expense():
    category = input("Enter category (Food/Travel/Shopping/Bills): ").title()

    try:
        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        file_exists = os.path.exists(FILE_NAME)

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists or os.path.getsize(FILE_NAME) == 0:
                writer.writerow(["Category", "Amount"])

            writer.writerow([category, amount])

        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount.")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        expenses = list(reader)

    if not expenses:
        print("No expenses found.")
        return

    print("\nYour Expenses")

    for expense in expenses:
        print(f"{expense['Category']}: Rs. {float(expense['Amount']):.2f}")


def get_category_totals():
    totals = {}

    if not os.path.exists(FILE_NAME):
        print("No expenses found. Add expenses first.")
        return None

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for expense in reader:
            category = expense["Category"]
            amount = float(expense["Amount"])

            totals[category] = totals.get(category, 0) + amount

    if not totals:
        print("No expenses found. Add expenses first.")
        return None

    return totals


def show_total():
    totals = get_category_totals()

    if totals is None:
        return

    total = sum(totals.values())

    print(f"\nTotal Expenses: Rs. {total:.2f}")

    for category, amount in totals.items():
        print(f"{category}: Rs. {amount:.2f}")


def show_charts():
    totals = get_category_totals()

    if totals is None:
        return

    categories = list(totals.keys())
    amounts = list(totals.values())

    # Bar chart
    plt.figure(figsize=(8, 5))
    plt.bar(categories, amounts)
    plt.title("Category-wise Expenses")
    plt.xlabel("Category")
    plt.ylabel("Amount (Rs.)")
    plt.tight_layout()
    plt.savefig("expense_bar_chart.png")
    plt.show()

    # Pie chart
    plt.figure(figsize=(7, 7))
    plt.pie(amounts, labels=categories, autopct="%1.1f%%")
    plt.title("Expense Distribution")
    plt.tight_layout()
    plt.savefig("expense_pie_chart.png")
    plt.show()

    print("Charts saved successfully!")


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expenses")
    print("4. Display Charts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        show_charts()
    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice. Try again.")
