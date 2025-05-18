titles = []
amounts = []
is_income = []

def input_data():
    title = input("Enter the title of transaction: ")
    amount = float(input("Enter the amount (positive for income and negative for expense): "))
    return title, amount

def add():
    title, amount = input_data()
    if title in titles:
        print("Tis title already exist!")
        return
    
    if amount == 0:
        print("Amount cannot be zero!")
        return
    
    if amount < 0 and sum(amounts) < -amount:
        print("Expense exceeds current balance!")
        return

    titles.append(title) 
    amounts.append(amount)
    is_income.append(amount > 0)
    kind = "Income" if amount > 0 else "Expense"
    print(f"{kind} added: {title} , {amount}")
 

def search(search_title):
    if search_title in titles:
        idx = titles.index(search_title)
        kind = "Income" if is_income[idx] else "Expense"
        print(f"{titles[idx]} | Type:{kind} | Amont: {amounts[idx]}") 
    else:
        print("Not Found!")


def filtered_index(show_type):
    filtered = []
    if show_type == "all":
        filtered = range(len(titles))
    elif show_type == "income":
        for i in range(len(titles)):
            if is_income[i]:
                filtered.append(i)
    elif show_type == "expense":
        filtered = [i for i in range(len(titles)) if not is_income[i]]
    else:
        print("Not Found!")
    return filtered


def show(show_type):
    filtered = filtered_index(show_type)
    for i in filtered: # 0
        kind = "Income" if is_income[i] else "Expense"
        print(f"{titles[i]} | Type:{kind} | Amont: {amounts[i]}") 
    print()


def total():
    total_income = sum(i for i in amounts if i > 0)
    total_expense = sum(i for i in amounts if i < 0)
    balance = total_income + total_expense
    print(f"\nTotal income: {total_income}")
    print(f"Total expense: {total_expense}")
    print(f"Balance: {balance}\n")
    

def help():
    print("\nBudget Manager Help:")
    print("-" * 50)
    print("add       : Add a new transaction (income or expense).")
    print("search    : Search for a transaction by exact title.")
    print("show      : Display transactions. Options: all / income / expense.")
    print("total     : Show the total income, total expense, and balance.")
    print("exit      : Exit the program.")
    print("-" * 50)


#for i in range(200):
while True:
    action = input("Choose an option or type 'help': ")
    if action == "add":
        add()

    elif action == "search":
        search_title = input("Enter the title for search: ")
        search(search_title)

    elif action == "show":
        kind = input("all / income / expense: ")
        show(kind)
       
    elif action == "total":
        total()

    elif action == "help":
        help()
        
    elif action == "exit":
        break
    elif action == "":
        continue
    else:
        print(f"{action}: Not Found!")