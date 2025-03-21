# Blaine Buckler, Financial Calculator Update Python

print("Welcome to my program, this program will calculate your finances. \n")


def get_inputs():

    income = float(input("Please tell me your monthly income: \n$"))
    rent = float(input("Please tell me your monthly rent: \n$"))
    utilities = float(input("Please tell me your monthly utilities: \n$"))
    food = float(input("Please tell me your monthly groceries bill: \n$"))
    transport = float(input("Please tell me your monthly transport bill: \n$"))
    return income, rent, utilities, food, transport

income, rent, utilities, food, transport = get_inputs()

savings = income * 0.2
exspenses = rent + utilities + food + transport
spending = income - exspenses - savings
#prent = rent / income * 100
#putilities = utilities / income * 100
#pfood = food / income * 100
#ptransport = transport / income * 100
#psavings = savings/income * 100
def percent(type, amount): 
    per = amount/income *100

    print(f"Your {type} is {per:.2f}% income. \n")

def cash(type, amount): 

    print(f"Your monthly {type} is ${amount:.2f}\n")
#print(f"Your monthly income is ${income:.2f}\n")
#print(f"Your monthly exspenses are ${exspenses:.2f}\n")
#print(f"Your monthly savings is ${savings:.2f}\n")
#print(f"Your monthly spending money is ${spending:.2f}\n")
cash("rent", rent)
cash("exspenses", exspenses)
cash("savings", savings)
cash("spending", spending)
#print(f"Your rent is %{int(prent)} of your monthly income\n")
#print(f"Your utilities are {int(putilities)}% of your income\n")
#print(f"Your groceries are {int(pfood)}% of your income\n")
#print(f"Your transportation are {int(ptransport)}% of your income\n")
#print(f"Your savings are {int(psavings)}% of your income\n")
#print(f"Your exspenses are {int(pexspenses)}% of your income\n")
percent("rent", rent)
percent("utilities", utilities)
percent("groceries", food)
percent("transportation", transport)
percent("savings", savings)
percent("exspenses", exspenses)
