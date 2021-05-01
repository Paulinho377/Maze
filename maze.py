import os

import readchar

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15

my_position = [3, 1]


print("+" + "-" * MAP_WIDTH * 3 + "+")

while True:

    for cordinate_y in range(MAP_HEIGHT):
        print("|",end="")
        for cordinate_x in range(MAP_WIDTH):
            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                print(" @ ", end="")
            else:
                print("   ",end="")
        print("|")
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    direction = readchar.readchar().decode()

    if direction == "w":
        my_position[POS_Y] -= 1
    elif direction == "s":
        my_position[POS_Y] += 1
    elif direction == "a":
        my_position[POS_X] -= 1
    elif direction == "d":
        my_position[POS_X] += 1
    
    if my_position[POS_X] == 0:
        my_position[POS_X] = 15
    if my_position[POS_Y] == 0:
        my_position[POS_Y] = 20
    elif direction == "q":
   
    elif direction == "q":
        break

    os.system("cls")