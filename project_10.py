import customtkinter as ctk
from classes_10 import Budget
import functions

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Budget Buddy")
app.geometry("600x500")

frame = ctk.CTkFrame(master=app)
frame.pack(pady=40, padx=60, fill="both", expand=True)

# ---------- THEME SWITCH ----------
theme_label = ctk.CTkLabel(master=frame, text="Theme:")
theme_label.pack(pady=(10, 0))

def change_theme(choice):
    ctk.set_appearance_mode(choice)

theme_menu = ctk.CTkOptionMenu(master=frame, values=["Light", "Dark"], command=change_theme)
theme_menu.pack()

# ---------- NAME ENTRY ----------
name_label = ctk.CTkLabel(master=frame, text="Enter your name:")
name_label.pack(pady=(20, 0))
name_entry = ctk.CTkEntry(master=frame)
name_entry.pack()

# ---------- ERROR DISPLAY ----------
error_label = ctk.CTkLabel(master=frame, text="", text_color="red")
error_label.pack()

# ---------- RESULT LABEL ----------
result_label = ctk.CTkLabel(master=frame, text="")
result_label.pack(pady=(10, 0))

def submit_all():
    try:
        income = float(income_entry.get())
        grocery = Budget("Grocery")
        car = Budget("Car")

        for item in grocery_entry.get().split(','):
            name_cost = item.strip().split()
            if len(name_cost) == 2:
                name_item, cost = name_cost
                grocery.add_expense(name_item, cost)
            else:
                raise ValueError

        for item in car_entry.get().split(','):
            name_cost = item.strip().split()
            if len(name_cost) == 2:
                name_item, cost = name_cost
                car.add_expense(name_item, cost)
            else:
                raise ValueError

        total = grocery.get_expenses() + car.get_expenses()
        balance = functions.calc_balance(income, total)
        status_message = functions.financial_status(balance)

        for widget in frame.winfo_children():
            widget.pack_forget()

        theme_label.pack(pady=(10, 0))
        theme_menu.pack()

        result_text = f"Total Expenses: ${total:.2f}\nBalance: ${balance:.2f}\n{status_message}"
        result_label.configure(text=result_text, text_color="red" if balance < 0 else "green")
        result_label.pack(pady=20)

        # ---- Prepare current session's expense details ----
        expense_text = "\nGrocery Expenses:\n"
        for name, cost in grocery.get_expenses_list().items():
            expense_text += f"{name} : ${float(cost):.2f}\n"

        expense_text += "\nCar Expenses:\n"
        for name, cost in car.get_expenses_list().items():
            expense_text += f"{name} : ${float(cost):.2f}\n"

        #expense_text += "\n----------------------\n"

        # --- Append to file ---
        with open("data.txt", "a") as f:
            f.write(expense_text)

        # --- Show only current session expenses ---
        expense_title = ctk.CTkLabel(master=frame, text="Individual Expenses:")
        expense_title.pack()

        data_label = ctk.CTkLabel(master=frame, text=expense_text, justify="left", anchor="w")
        data_label.pack(pady=(10, 0))


        view_all_button = ctk.CTkButton(master=frame, text="View All Past Expenses", command=show_all_expenses)
        view_all_button.pack(pady=(10, 0))

    except ValueError:
        error_label.configure(text="Please follow 'name cost' format")

def submit_income():
    try:
        float(income_entry.get())
        for widget in frame.winfo_children():
            widget.pack_forget()

        theme_label.pack(pady=(10, 0))
        theme_menu.pack()

        grocery_label = ctk.CTkLabel(master=frame, text="Grocery expenses (e.g., milk 30, bread 10):")
        grocery_label.pack(pady=(10, 0))
        global grocery_entry
        grocery_entry = ctk.CTkEntry(master=frame)
        grocery_entry.pack()

        car_label = ctk.CTkLabel(master=frame, text="Car expenses (e.g., fuel 50, oil 20):")
        car_label.pack(pady=(10, 0))
        global car_entry
        car_entry = ctk.CTkEntry(master=frame)
        car_entry.pack()

        error_label.pack()
        submit_button = ctk.CTkButton(master=frame, text="Submit Expenses", command=submit_all)
        submit_button.pack(pady=20)

    except ValueError:
        error_label.configure(text="Please enter a valid number for income.")

def proceed():
    user_name = name_entry.get()
    for widget in frame.winfo_children():
        widget.pack_forget()

    theme_label.pack(pady=(10, 0))
    theme_menu.pack()

    global income_entry
    income_label = ctk.CTkLabel(master=frame, text=f"Hi {user_name}, please enter monthly income:")
    income_label.pack(pady=(10, 0))
    income_entry = ctk.CTkEntry(master=frame)
    income_entry.pack()

    income_submit = ctk.CTkButton(master=frame, text="Submit Income", command=submit_income)
    income_submit.pack(pady=10)

    error_label.pack()

def show_all_expenses():
    try:
        with open("data.txt", "r") as f:
            all_data = f.read()

        # Remove previous widgets in frame
        for widget in frame.winfo_children():
            widget.pack_forget()

        theme_label.pack(pady=(10, 0))
        theme_menu.pack()

        title = ctk.CTkLabel(master=frame, text="All Past Expenses:")
        title.pack(pady=(10, 5))

        all_data_label = ctk.CTkLabel(master=frame, text=all_data, justify="left", wraplength=500)
        all_data_label.pack(pady=(0, 10))

        back_button = ctk.CTkButton(master=frame, text="Back", command=proceed)
        back_button.pack(pady=(10, 0))

    except FileNotFoundError:
        error_label.configure(text="No past expense data found.")







submit_button = ctk.CTkButton(master=frame, text="Continue", command=proceed)
submit_button.pack()


app.mainloop()
