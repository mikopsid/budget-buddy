
def calc_balance(income, expenses):
    balance = income - expenses
    return balance


def financial_status(balance):
    if balance > 0:
        return "Great! You are saving money!"
    elif balance  == 0:
        return "You are breaking even."
    elif balance < 0:
        return "**WARNING** You are overspending!"
    
