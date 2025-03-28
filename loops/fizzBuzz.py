#Blaine Buckler, Fizz Buzz Python

num = 1
multiplier = 3  # Set any number for the multiplier
multiplierT = 5
while num < 51:
    if num % multiplier == 0 and num % multiplierT == 0: 
        print("FizzBuzz")
    elif num % multiplier == 0:  # Check if 'num' is a multiple of 'multiplier'
        print("Fizz")
    elif num % multiplierT == 0: 
        print("Buzz")
    else:
        print(num)
    num += 1
