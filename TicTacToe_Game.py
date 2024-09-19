#!/usr/bin/python3
import random
import time


row2 = [[" "], [" "], [" "]]
row1 = [[" "], [" "], [" "]]
row0 = [[" "], [" "], [" "]]
nim = list()
choose_round = ["Rounds:"]
condition = " "
def grid_board():
    
    print("{} | {} | {} \t row2 | 7 | 8 | 9 |".format(row2[0][0], row2[1][0], row2[2][0])) 
    print("{} | {} | {} \t row1 | 4 | 5 | 6 |".format(row1[0][0], row1[1][0], row1[2][0]))
    print("{} | {} | {} \t row0 | 1 | 2 | 3 |".format(row0[0][0], row0[1][0], row0[2][0]))

def game_Play():
    count = 0
    while count < 9:   
        time.sleep(2)
        choose = round_get()
        if choose == "X":
            count += 1
            print("\tit's Player 'X' turn:")
            number = Human_choice(choose) #randomComputer_choice()
            if number < 4:
                if number == 1:
                    row0[0].insert(0, "X")
                elif number == 2:
                    row0[1].insert(0, "X")
                elif number == 3:
                    row0[2].insert(0, "X")
            elif 3 < number < 7:
                if number == 4:
                    row1[0].insert(0, "X")
                elif number == 5:
                    row1[1].insert(0, "X")
                elif number == 6:
                    row1[2].insert(0, "X")
            else:
                if number == 7:
                    row2[0].insert(0, "X")
                elif number == 8:
                    row2[1].insert(0, "X")
                elif number == 9:
                    row2[2].insert(0, "X")

        else:
            count += 1
            print("\tIt's player 'O' turn:")
            number = randomComputer_choice()
            if number < 4:
                if number == 1:
                    row0[0].insert(0, "O")
                elif number == 2:
                    row0[1].insert(0, "O")
                elif number == 3:
                    row0[2].insert(0, "O")
            elif 3 < number < 7:
                if number == 4:
                    row1[0].insert(0, "O")
                elif number == 5:
                    row1[1].insert(0, "O")
                elif number == 6:
                    row1[2].insert(0, "O")
            else:
                if number == 7:
                    row2[0].insert(0, "O")
                elif number == 8:
                    row2[1].insert(0, "O")
                elif number == 9:
                    row2[2].insert(0, "O")
        grid_board()
        condition = Game_win()
        time.sleep(1)
        if condition == True:
            return print("GAME Over")
        print("\n")
        
    
def randomComputer_choice():
    count = 0
    while count <= 9:
        number = random.randint(1,9)
        count += 1
        if number not in nim:
            nim.append(number)
            return number
        else:
            pass
    return number
    
def Human_choice(choose):
    number = int(input(f"Enter grid number for {choose}: "))
    for i in range(100):
        if number not in nim:
            nim.append(number)
            return number
        else:
            number = int(input("Enter grid number for {choose}: "))
    return number



def round_get():       
    count = 0
    while count <= 9:
        choose = random.choice(["X","O"])
        count += 1
        if choose != choose_round[-1]:
            choose_round.append(choose)
            print("\nGame Round:",len(choose_round)-1)
            print("\n")
            return choose
        else:
            pass


def Game_win():
    # check if the column are equal to "X"
    if row0[0][0] == row1[0][0] and row0[0][0] == row2[0][0] and row0[0][0] == "X":
        print(f"{row0[0][0]} is the winner.")
        return True
    elif row0[1][0] == row1[1][0] and row0[1][0] == row2[1][0] and row0[1][0] == "X": 
        print(f"{row0[1][0]} is the winner.")
        return True
    elif row0[2][0] == row1[2][0] and row0[2][0] == row2[2][0] and row0[2][0] == "X":
        print(f"{row0[2][0]} is the winner.")
        return True
    # check if diagonal is qual to "X"
    elif row0[0][0] == row1[1][0] and row0[0][0] == row2[2][0] and row0[0][0] == "X":
        print(f"{row0[0][0]} is the winner.")
        return True
    elif row0[2][0] == row1[1][0] and row0[2][0] == row2[0][0] and row0[2][0] == "X":
        print(f"{row0[2][0]} is the winner.")
        return True

    elif row0[0][0] == row1[0][0] and row0[0][0] == row2[0][0] and row0[0][0] == "O":
        print(f"{row0[0][0]} is the winner.")
        return True
    elif row0[1][0] == row1[1][0] and row0[1][0] == row2[1][0] and row0[1][0] == "O": 
        print(f"{row0[1][0]} is the winner.")
        return True
    elif row0[2][0] == row1[2][0] and row0[2][0] == row2[2][0] and row0[2][0] == "O":
        print(f"{row0[2][0]} is the winner.")
        return True
    elif row0[0][0] == row1[1][0] and row0[0][0] == row2[2][0] and row0[0][0] == "O":
        print(f"{row0[0][0]} is the winner.")
        return True
    elif row0[2][0] == row1[1][0] and row0[2][0] == row2[0][0] and row0[2][0] == "O":
        print(f"{row0[2][0]} is the winner.")
        return True
    
    elif row0[0][0] == row0[1][0] and row0[0][0] == row0[2][0] and row0[0][0] == "X":
        print(f"{row0[0][0]} is the winner.")
        return True
    elif row1[0][0] == row1[1][0] and row1[0][0] == row1[2][0] and row1[0][0] == "X":
        print(f"{row1[0][0]} is the winner.")
        return True
    elif row2[0][0] == row2[1][0] and row2[0][0] == row2[2][0] and row2[0][0] == "X":
        print(f"{row2[0][0]} is the winner.")
        return True
    
    elif row0[0][0] == row0[1][0] and row0[0][0] == row0[2][0] and row0[0][0] == "O":
        print(f"{row0[0][0]} is the winner.")
        return True
    elif row1[0][0] == row1[1][0] and row1[0][0] == row1[2][0] and row1[0][0] == "O":
        print(f"{row1[0][0]} is the winner.")
        return True
    elif row2[0][0] == row2[1][0] and row2[0][0] == row2[2][0] and row2[0][0] == "O":
        print(f"{row2[0][0]} is the winner.")
        return True

    else:
        return False

grid_board()
game_Play()
if condition == False:
    print("Its a tie.")
