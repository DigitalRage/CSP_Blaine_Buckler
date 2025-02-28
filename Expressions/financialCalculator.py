# Blaine Buckler, Financial Calculator C
print("Welcome to my program, this program will calculate your finances. ")

# Prompt the user for financial information and convert inputs to integers
income = int(input("Please tell me your monthly income: "))
rent = int(input("Please tell me your monthly rent: "))
utilities = int(input("Please tell me your monthly utilities: "))
food = int(input("Please tell me your monthly groceries bill: "))
transport = int(input("Please tell me your monthly transport bill: "))

# Calculate the leftover income
leftOver = income - rent - utilities - food - transport

# Display the leftover income
print("Your leftover income is", leftOver)