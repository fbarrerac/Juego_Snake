import os

import random

import readchar as readchar

map_height = 15
map_width = 20

snake_Pos = [0, 0]
tail_Lenght = 0
tail_Pos = []

apples_Cant = int(input("Ingrese la cantidad de manzanas: "))
apples_Pos = []

def print_map(tail_Length):
    print("╔" + "═" * map_width * 3 + "╗")

    for i in range(map_height):
        print("║", end="")

        for j in range(map_width):

            elementToPrint = " "

            for k in range(len(apples_Pos)):
                if apples_Pos[k][0] == j and apples_Pos[k][1] == i:
                    elementToPrint = "*"

            if snake_Pos[0] == j and snake_Pos[1] == i:
                elementToPrint = "@"

                if [j, i] in apples_Pos:
                    apples_Pos.remove([j, i])
                    tail_Length += 1

            print(" {} ".format(elementToPrint), end="")

        print("║")

    print("╚" + "═" * map_width * 3 + "╝")

def create_apples():

    while len(apples_Pos) < apples_Cant:
        x = random.randint(0, map_width - 1)
        y = random.randint(0, map_height - 1)

        if [x, y] in apples_Pos or [x, y] == [0, 0]:
            pass
        else:
            apples_Pos.append([x, y])


create_apples()

while True:

    print_map(tail_Lenght)

    direction = readchar.readchar()

    if direction == "w":
        snake_Pos[1] -= 1
        snake_Pos[1] %= map_height
    elif direction == "s":
        snake_Pos[1] += 1
        snake_Pos[1] %= map_height
    if direction == "a":
        snake_Pos[0] -= 1
        snake_Pos[0] %= map_width
    elif direction == "d":
        snake_Pos[0] += 1
        snake_Pos[0] %= map_width
    elif direction == "q":
        break

    os.system("cls")
