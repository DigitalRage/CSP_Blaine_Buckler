
print("Welcome to my program, this program will calculate your finances. \n")


income = int(input("Please tell me your monthly income: \n"))
rent = int(input("Please tell me your monthly rent: \n"))
utilities = int(input("Please tell me your monthly utilities: \n"))
spending = int(input("Please tell me how much you spend on extra stuff a month: \n"))
food = int(input("Please tell me your monthly groceries bill: \n"))
transport = int(input("Please tell me your monthly transport bill: \n"))

total = income-rent-utilities-spending-food-transport

prent = rent/income*100
putilities = utilities/income*100
pspending = spending/income*100
pfood = food/income*100
ptransort = transport/income*100

ptotal = prent+putilities+pspending+pfood+ptransort

psavings = (100-(prent+putilities+pspending+pfood+ptransort))*0.2

print("your total spendings is", ptotal, "% of your oncome")
print("Your rent is", "{:.2f}".format(prent), "% of your income\n")
print("Your utilities are", "{:.2f}".format(putilities), "% of your income\n")
print("Your spendings are", "{:.2f}".format(pspending), "%  of your income\n")
print("Your groceries is", "{:.2f}".format(pfood), "% of your income\n")
print("Your pay for transportation is", "{:.2f}".format(ptransort), "% of your income\n")
print("You should put", "{:.2f}".format(psavings), "% into your savings")

leftOver = income - (rent + utilities + food + transport + psavings)


print("Your leftover income would be", leftOver*0.1, "%\n")
print("In actual cash you will have", total, "dollars left. \n")