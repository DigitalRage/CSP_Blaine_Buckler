# Lisa Rehm, Eve Richardson, and Blaine Buckler; The Final Final
winVar = 0 #Made for my loop to work, Blaine
import random

#Eve
(zero, one, two, three, four, five, six, seven, eight, nine) = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) #Zero is not used to reduce confusion, Blaine
#Lisa
spaces = [zero, one, two, three, four, five, six, seven, eight, nine]

#Eve
def board():
    print(f" {spaces[1]} | {spaces[2]} | {spaces[3]} ")
    print("-----------")
    print(f" {spaces[4]} | {spaces[5]} | {spaces[6]} ")
    print("-----------")
    print(f" {spaces[7]} | {spaces[8]} | {spaces[9]} ")
    print(" ")

board()

#Lisa and Blaine
def user_turn():
    taken_x = int(input("Pick a number between 1 and 9:\n")) #Debugged code to detect number and put in "taken_x" rather than elif for each number. I also stoped the infanite "blue_turn" glitch, Blaine
    if 1 <= taken_x <= 9 and spaces[taken_x] == taken_x:
        spaces[taken_x] = "X"
        board()
        winner()
    else:
        print("Pick a different number.")
        user_turn() 
#Eve and Blaine
def winner():
    global winVar
    if (spaces[1] == spaces[2] == spaces[3] == "O" or #Made easier to understand by putting each condition on differnt lines, Blaine
        spaces[4] == spaces[5] == spaces[6] == "O" or
        spaces[7] == spaces[8] == spaces[9] == "O" or
        spaces[1] == spaces[4] == spaces[7] == "O" or
        spaces[2] == spaces[5] == spaces[8] == "O" or
        spaces[3] == spaces[6] == spaces[9] == "O" or
        spaces[1] == spaces[5] == spaces[9] == "O" or
        spaces[3] == spaces[5] == spaces[7] == "O"):
        print("Blue wins!")
        winVar = 1

    elif (spaces[1] == spaces[2] == spaces[3] == "X" or
          spaces[4] == spaces[5] == spaces[6] == "X" or
          spaces[7] == spaces[8] == spaces[9] == "X" or
          spaces[1] == spaces[4] == spaces[7] == "X" or
          spaces[2] == spaces[5] == spaces[8] == "X" or
          spaces[3] == spaces[6] == spaces[9] == "X" or
          spaces[1] == spaces[5] == spaces[9] == "X" or
          spaces[3] == spaces[5] == spaces[7] == "X"):
        name = input("What is your name?\n")
        print(f"Congratulations {name}, you won!")
        winVar = 1

    elif (spaces[1] in ["X", "O"] and
    spaces[2] in ["X", "O"] and
    spaces[3] in ["X", "O"] and
    spaces[4] in ["X", "O"] and 
    spaces[5] in ["X", "O"] and 
    spaces[6] in ["X", "O"] and 
    spaces[7] in ["X", "O"] and
    spaces[8] in ["X", "O"] and 
    spaces[9] in ["X", "O"]): 
        print("Tie Game")
        winVar = 1
        
    else:
        print("No winner yet, keep playing.")

#Lisa
def blue_turn():
    board()
    valid_move = False #Clears the variable to make it reusable, Blaine
    while not valid_move:
        move = random.randint(1, 9)  
        if spaces[move] == move:
            spaces[move] = "O"
            valid_move = True #Gives a new integer to put in, Blaine
    board()
    winner()

#Blaine
def main(): #Code is used to check if game is over, Blaine
    while winVar == 0:
        user_turn()
        if winVar:
            break
        blue_turn()

main()

