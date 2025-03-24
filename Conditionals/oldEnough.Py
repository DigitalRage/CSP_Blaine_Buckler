# Blaine Buckler, Old Enough Python
age = int(input("Please tell me your age: "))
if age < 128: 
    if age >= 18:
        print("You are old enough to vote.\n")
    else:
        print("You are not old enough to vote.\n")

    if age >= 16:
        print("You are old enough to drive.\n")
    elif age >= 15:
        print("You are old enough to have a driver's permit.\n")
    else:
        print("You are not old enough to drive.\n")

    if age >= 5:
        print("You are old enough to go to school.\n")
    else:
        print("You are not old enough to go to school.\n")
else: 
    print("How are you alive?")