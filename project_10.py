from tkinter import *
import functions
from classes_10 import Budget

root = Tk()
root.title("Budget Buddy")
root.geometry("500x400")

# ---------- STEP 1: Ask Name ----------
def on_submit():
    user_name = entryname.get()
    for widget in root.winfo_children():
        widget.destroy()

    Label(root, text=f"Hey {user_name}, this is BudgetBuddy! Your personal Budgeting Assistant.").pack()
    ask_income()


# ---------- STEP 2: Ask Income ----------
def ask_income():
    Label(root, text="Enter monthly income (numbers only):").pack()

    income_etr = Entry(root)
    income_etr.pack()

    def process_income():
        try:
            income_val = float(income_etr.get())
            for widget in root.winfo_children():
                widget.destroy()
            ask_expenses(income_val)
        except ValueError:
            Label(root, text="Please enter a valid number").pack()

    Button(root, text="Submit Income", command=process_income).pack()


# ---------- STEP 3: Ask Expenses ----------
def ask_expenses(income):
    Label(root, text="Enter Grocery expenses (e.g., milk 30, bread 10):").pack()
    grocery_entry = Entry(root, width=50)
    grocery_entry.pack()

    Label(root, text="Enter Car expenses (e.g., fuel 50, oil 20):").pack()
    car_entry = Entry(root, width=50)
    car_entry.pack()

    error_label = Label(root, text="", fg="red")
    error_label.pack()

    def process_expenses():
        try:
            grocery = Budget("Grocery")
            car = Budget("Car")

            # Clear previous error message
            error_label.config(text="")

            # Parse grocery input
            for item in grocery_entry.get().split(','):
                name_cost = item.strip().split()
                if len(name_cost) == 2:
                    name, cost = name_cost
                    grocery.add_expense(name, cost)
                else:
                    raise ValueError

            # Parse car input
            for item in car_entry.get().split(','):
                name_cost = item.strip().split()
                if len(name_cost) == 2:
                    name, cost = name_cost
                    car.add_expense(name, cost)
                else:
                    raise ValueError

            total = grocery.get_expenses() + car.get_expenses()
            balance = functions.calc_balance(income, total)

            for widget in root.winfo_children():
                widget.destroy()

            Label(root, text=f"Balance: ${balance:.2f}").pack()
            functions.financial_status(balance)

            Label(root, text="Expenses Breakdown:").pack()
            Label(root, text="Grocery:").pack()
            for name, amount in grocery.get_expenses_list().items():
                Label(root, text=f"{name}: ${amount:.2f}").pack()

            Label(root, text="Car:").pack()
            for name, amount in car.get_expenses_list().items():
                Label(root, text=f"{name}: ${amount:.2f}").pack()

            grocery.write_to_file()
            car.write_to_file()

        except ValueError:
            error_label.config(text="Please follow format: name cost, name cost")

    Button(root, text="Submit Expenses", command=process_expenses).pack()


# ---------- INITIAL SCREEN ----------
Label(root, text="Enter your name").pack()
entryname = Entry(root)
entryname.pack()

Button(root, text="Submit", command=on_submit).pack()

root.mainloop()