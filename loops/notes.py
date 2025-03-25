# Blaine Buckler, Loops Notes in Python

#Section of code that will repeat

#While loop
x = 0
while x < 10:
    print("Hello", x)
    x +=1

#For loop
nums = [3,5,7,2,8]
for num in nums:
    print(num)

#Iteration: the repitition of an action

#Lists A bunch of values in the same variable
siblings = ["Alex", "Katie", "Andrew", "Vienna", "Tori", "Treyson", "Jeff", "Hailey"]
#print from list
print(siblings[3])

#Change an item in the list
siblings[7] = "Jake"
#remove an item form a list
#siblings.pop(5)
#proper list printing with a for loop
print(siblings)

#you do [] around the list, and commas betweemn each item in the list. 
num = 1 
for sibling in siblings:
    print(f"{num}. {sibling}, LaRose")
    num +=1
# Using range instead of list
for num in range(1,11, 2):
    print(num)

    #How to make while loop
import random

num = 1
rand = random.randint(1,20)
while num < 21:
    if num == rand:
        print(f"Goose!")
        #continue # tells the loop to be done
        break
    else:
        print("Duck")
    num += 1

#continue tells loop to stop the specific round of the loop