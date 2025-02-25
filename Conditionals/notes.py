# Blaine Buckler, Conditionals notes Python

#print("Hello welcome to my program that will sort you into a catagory")

#name = input("What is your name:\n")

#if name == "Vienna":
#    print("Oh your the teacher. . . never mind.")
#else:
#    print("You are a student. Welcome to class.")


# == will check if content is same
# === will check if content and data type is the same


#num = int(input("how many would you like:(give ma a number above 0)"))

#if num == 1:
#    print("You have asked for a item")
#elif num <= 3: 
#    print("You have asked for a couple of the item") 
#elif num <= 5:
#    print("You have asked for a few of the item. . .or in the south and you asked for a couple")
#else:
#    print("You have asked for some of the item")

# Conditionals start at the top and work their way down, they will stop at the first correct one. 
# 1st condition will be the least likely first
# Don't trigger false positive

# name = "Katie"

# if "a" in name or "e" in name or "i" in name or "o" in name or "u" in name:
#     print("your name name has the vowel!")
# else:
#     print("your name doesn't have a vowel.") 

num = 6

if num > 5 and num < 10: 
    if num == 7: 
        print(f"{num}That is an unluck number!")
    else: 
        print(f"{num} is a large single digit number. ")
else: 
    if num == 4:
        print(f"{num} is the best number")
    else:
        if num >= 10: 
         print(f"{num} is not a single number")
    else: 
        print(f"{num} is a single number")