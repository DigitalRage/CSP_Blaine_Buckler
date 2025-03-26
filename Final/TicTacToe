# Lisa Rehm and Eve Richardson, The Final Final
winVar = 0
import random

rand = random.randint(1,9)

# Eve
(zero, one, two, three, four, five, six, seven, eight, nine) = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Lisa
spaces = [zero, one, two, three, four, five, six, seven, eight, nine]

# Eve
def board():
    print(f" {spaces[0]} | {spaces[1]} | {spaces[2]} ")
    print("-----------")
    print(f" {spaces[3]} | {spaces[4]} | {spaces[5]} ")
    print("-----------")
    print(f" {spaces[6]} | {spaces[7]} | {spaces[8]} ")
    print(" ")

board()

# Lisa
def user_turn(spaces):
    taken_x = int(input("Pick a number between 1 and 9:\n"))
    if taken_x == 1 and spaces[0] == 1:
        spaces[0] = "X"
        board()
        winner()
    elif taken_x == 2 and spaces[1] == 2:
        spaces[1] = "X"
        board()
        winner()
    elif taken_x == 3 and spaces[2] == 3:
        spaces[2] = "X"
        board()
        winner()
    elif taken_x == 4 and spaces[3] == 4:
        spaces[3] = "X"
        board()
        winner()
    elif taken_x == 5 and spaces[4] == 5:
        spaces[4] = "X"
        board()
        winner()
    elif taken_x == 6 and spaces[5] == 6:
        spaces[5] = "X"
        board()
        winner()
    elif taken_x == 7 and spaces[6] == 7:
        spaces[6] = "X"
        board()
        winner()
    elif taken_x == 8 and spaces[7] == 8:
        spaces[7] = "X"
        board()
        winner()
    elif taken_x == 9 and spaces[8] == 9:
        spaces[8] = "X"
        board()
        winner()
    else:
        print("Pick a different number.")
        user_turn(spaces)
    return

# Eve
def winner():
    if spaces[0]==spaces[1]==spaces[2]=="O" or spaces[3]==spaces[4]==spaces[5]=="O" or spaces[6]==spaces[7]==spaces[8]=="O" or spaces[0]==spaces[3]==spaces[6]=="O" or spaces[1]==spaces[4]==spaces[7]=="O" or spaces[2]==spaces[5]==spaces[8]=="O" or spaces[0]==spaces[4]==spaces[8]=="O" or spaces[2]==spaces[4]==spaces[6]=="O":
        print("Blue wins!")
        #Blaine
        winVar = 1
        #end
    elif spaces[0]==spaces[1]==spaces[2]=="X" or spaces[3]==spaces[4]==spaces[5]=="X" or spaces[6]==spaces[7]==spaces[8]=="X" or spaces[0]==spaces[3]==spaces[6]=="X" or spaces[1]==spaces[4]==spaces[7]=="X" or spaces[2]==spaces[5]==spaces[8]=="X" or spaces[0]==spaces[4]==spaces[8]=="X" or spaces[2]==spaces[4]==spaces[6]=="X":
        name = input("What is your name?\n")
        print(f"Congratulations {name}, you won!")
        #Blaine
        winVar = 1
        #end
    else:
        print("No winner yet, keep playing.")
        #Blaine
        winVar = 0
        #end

# Lisa
def blue_turn(rand):
    if rand == 1 and spaces[0] == 1:
        spaces[0] = "O"
        board()
        winner()
    elif rand == 2 and spaces[1] == 2:
        spaces[1] = "O"
        board()
        winner()
    elif rand == 3 and spaces[2] == 3:
        spaces[2] = "O"
        board()
        winner()
    elif rand == 4 and spaces[3] == 4:
        spaces[3] = "O"
        board()
        winner()
    elif rand == 5 and spaces[4] == 5:
        spaces[4] = "O"
        board()
        winner()
    elif rand == 6 and spaces[5] == 6:
        spaces[5] = "O"
        board()
        winner()
    elif rand == 7 and spaces[6] == 7:
        spaces[6] = "O"
        board()
        winner()
    elif rand == 8 and spaces[7] == 8:
        spaces[7] = "O"
        board()
        winner()
    elif rand == 9 and spaces[8] == 9:
        spaces[8] = "O"
        board()
        winner()
    else:
        print("Blue is dumb")
    return


# Blaine
while winVar == 0: 
    if winVar == 0:
        user_turn(spaces)
        blue_turn(rand)
    else:
        winVar == 1
        break
    
    