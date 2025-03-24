# Blaine Buckler, Financial Calculator Update Python

print("Welcome to my program, this program will calculate your finances. \n")


def get_input(prompt):  
    print("Please tell me your ", end="")
    return float(input(prompt))  
  
income = get_input("income: ")  
rent = get_input("rent: ")  
utilities = get_input("utilities: ")  
food = get_input("expenses: ")  
transport = get_input("costs: ")  


savings = income * 0.2
exspenses = rent + utilities + food + transport
spending = income - exspenses - savings

def percent(type, amount): 
    per = amount/income *100

    print(f"Your {type} is {per:.2f}% income. \n")

def cash(type, amount): 

    print(f"Your monthly {type} is ${amount:.2f}\n")

cash("rent", rent)
cash("exspenses", exspenses)
cash("savings", savings)
cash("spending", spending)

percent("rent", rent)
percent("utilities", utilities)
percent("groceries", food)
percent("transportation", transport)
percent("savings", savings)
percent("exspenses", exspenses)
