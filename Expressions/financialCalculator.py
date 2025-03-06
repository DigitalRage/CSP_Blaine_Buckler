# Blaine Buckler, Financial Calculator Python

print("Welcome to my program, this program will calculate your finances. \n")

income = float(input("Please tell me your monthly income: \n$"))
rent = float(input("Please tell me your monthly rent: \n$"))
utilities = float(input("Please tell me your monthly utilities: \n$"))
spending = float(input("Please tell me how much you spend on extra stuff a month: \n$"))
food = float(input("Please tell me your monthly groceries bill: \n$"))
transport = float(input("Please tell me your monthly transport bill: \n$"))

total = income - rent - utilities - spending - food - transport

prent = rent / income * 100
putilities = utilities / income * 100
pspending = spending / income * 100
pfood = food / income * 100
ptransport = transport / income * 100

ptotal = prent + putilities + pspending + pfood + ptransport

psavings = (100 - (prent + putilities + pspending + pfood + ptransport)) * 0.2

print("\nYour total spendings is", "{:.2f}".format(ptotal) + "% of your income\n")
print("Your rent is", "{:.2f}".format(prent) + "% of your income\n")
print("Your utilities are", "{:.2f}".format(putilities) + "% of your income\n")
print("Your spendings are", "{:.2f}".format(pspending) + "% of your income\n")
print("Your groceries is", "{:.2f}".format(pfood) + "% of your income\n")
print("Your pay for transportation is", "{:.2f}".format(ptransport) + "% of your income\n")
print("You should put", "{:.2f}".format(psavings) + "% into your savings")

leftOver = 100 - (prent + putilities + pfood + ptransport + psavings)

print("Your leftover income would be", "{:.2f}".format(leftOver) + "%\n")
print("In actual cash you will have $" + "{:.2f}".format(total) + ". \n")
