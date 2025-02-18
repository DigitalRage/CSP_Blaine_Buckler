# Blaine Buckler, Functions in Python

# Funtion is an action stored in a key word. 
#number = int(input("Can I get a number:\n"))
#def add(numOne, numTwo):#perameters go in the parentheses sperated by commas

#    print(numOne+numTwo)

#add(int(input("Tell me a number\n")),number)#arguments are given when the function is cald AND must match the number with parenthesis
#add(2, 4)
#add(7, 21)

def user(word): 
    answer = input(f"Tell me a {word}:\n")
    return answer
    
name = user("name")
verb = user("verb")
place = user("place")
print(f"{name} was {verb} and somhow got to {place}.")