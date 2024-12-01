#! /usr/bin/env python3

x = 0
y = 0

a = 0
b = 0

santa = True

with open("input03.txt", "r") as file:
    house = []
    house.append((x, y))
    while carac := file.read(1):
        if carac == "^":
            if santa:
                y += 1
            else:
                b += 1
        elif carac == ">":
            if santa:
                x += 1
            else:
                a += 1
        elif carac == "v":
            if santa:
                y -= 1
            else:
                b -= 1
        elif carac == "<":
            if santa:
                x -= 1
            else:
                a -= 1
        else:
            continue
        if (x, y) not in house:
            house.append((x, y))
        if (a, b) not in house:
            house.append((a, b))
        santa = not santa

    file.close()
    print(len(house))
