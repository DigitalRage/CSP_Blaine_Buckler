
print("Welcome to my program, this program will calculate your finances. \n")


income = int(input("Please tell me your monthly income: \n"))
rent = int(input("Please tell me your monthly rent: \n"))
utilities = int(input("Please tell me your monthly utilities: \n"))
spending = int(input("Please tell me how much you spend on extra stuff a month: \n"))
food = int(input("Please tell me your monthly groceries bill: \n"))
transport = int(input("Please tell me your monthly transport bill: \n"))


leftOver = income - rent - utilities - food - transport


print("Your leftover income is", leftOver)