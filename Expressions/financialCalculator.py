# Blaine Buckler, Financial Calculator Python

print("Welcome to my program, this program will calculate your finances. \n")

income = float(input("Please tell me your monthly income: \n$"))
rent = float(input("Please tell me your monthly rent: \n$"))
utilities = float(input("Please tell me your monthly utilities: \n$"))
food = float(input("Please tell me your monthly groceries bill: \n$"))
transport = float(input("Please tell me your monthly transport bill: \n$"))

total = income - rent - utilities - food - transport

prent = rent / income * 100
putilities = utilities / income * 100
pfood = food / income * 100
ptransport = transport / income * 100

ptotal = prent + putilities + pfood + ptransport

savings = income * 0.1

print("\nYour total spendings is", "{:.2f}".format(ptotal) + "% of your income\n")
print("Your rent is", "{:.2f}".format(prent) + "% of your income\n")
print("Your utilities are", "{:.2f}".format(putilities) + "% of your income\n")
print("Your groceries is", "{:.2f}".format(pfood) + "% of your income\n")
print("Your pay for transportation is", "{:.2f}".format(ptransport) + "% of your income\n")
print("You should put", "{:.2f}".format(savings) + "$ into your savings\n")

spending = (total / income * 100) -10 #This is percent form so I can subtract 10 to equal 10% less for the savings
pspending = total - savings #total is income - exspenses

print("You you will have", "{:.2f}".format(spending) + "% left to spend\n")
print("In actual cash you will have $" + "{:.2f}".format(pspending) + ". \n")
