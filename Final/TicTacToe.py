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
    print(f" {spaces[1]} | {spaces[2]} | {spaces[3]} ")
    print("-----------")
    print(f" {spaces[4]} | {spaces[5]} | {spaces[6]} ")
    print("-----------")
    print(f" {spaces[7]} | {spaces[8]} | {spaces[9]} ")
    print(" ")



# Lisa
def user_turn(spaces):
    taken_x = int(input("Pick a number between 1 and 9:\n"))
    if taken_x == 1 and spaces[1] == 1:
        spaces[1] = "X"
        board()
        winner()
    elif taken_x == 2 and spaces[2] == 2:
        spaces[2] = "X"
        board()
        winner()
    elif taken_x == 3 and spaces[3] == 3:
        spaces[3] = "X"
        board()
        winner()
    elif taken_x == 4 and spaces[4] == 4:
        spaces[4] = "X"
        board()
        winner()
    elif taken_x == 5 and spaces[5] == 5:
        spaces[5] = "X"
        board()
        winner()
    elif taken_x == 6 and spaces[6] == 6:
        spaces[6] = "X"
        board()
        winner()
    elif taken_x == 7 and spaces[7] == 7:
        spaces[7] = "X"
        board()
        winner()
    elif taken_x == 8 and spaces[8] == 8:
        spaces[8] = "X"
        board()
        winner()
    elif taken_x == 9 and spaces[9] == 9:
        spaces[9] = "X"
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
    board()
    if rand == 1:
        if spaces[1] == 1:
            spaces[1] = "O"
            board()
            winner()    
        elif spaces[1] == "X" or "O":
            blue_turn(rand)
    elif rand == 2: 
        if spaces[2] == 2:
            spaces[2] = "O"
            board()
            winner()
        elif spaces[2] == "X" or "O":
            blue_turn(rand)
    elif rand == 3:
        if spaces[3] == 3:
            spaces[3] = "O"
            board()
            winner()
        elif spaces[3] == "X" or "O":
            blue_turn(rand)
    elif rand == 4:
        if spaces[4] == 4:
            spaces[4] = "O"
            board()
            winner()
        elif spaces[4] == "X" or "O":
            blue_turn(rand)
    elif rand == 5:
        if spaces[5] == 5:
            spaces[5] = "O"
            board()
            winner()
        elif spaces[5] == "X" or "O":
            blue_turn(rand)
    elif rand == 6:
        if spaces[6] == 6:
            spaces[1] = "O"
            board()
            winner()
        elif spaces[6] == "X" or "O":
            blue_turn(rand)
    elif rand == 7:
        if spaces[7] == 7:
            spaces[7] = "O"
            board()
            winner()
        elif spaces[7] == "X" or "O":
            blue_turn(rand)
    elif rand == 8:
        if spaces[8] == 8:
            spaces[8] = "O"
            board()
            winner()
        elif spaces[8] == "X" or "O":
            blue_turn(rand)
    elif rand == 9:
        if spaces[9] == 9:
            spaces[9] = "O"
            board()
            winner()
        elif spaces[9] == "X" or "O":
            blue_turn(rand)
    else:
        print("Blue is dumb")
    return


# Blaine

    


def main():
    while winVar == 0: 
        if winVar == 0:
            user_turn(spaces)
            blue_turn(rand)
        else:
            winVar == 1
            break


main()