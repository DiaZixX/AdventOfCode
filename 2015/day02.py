#! /usr/bin/env python3

total = 0


def area(l, w, h):
    c1 = l * w
    c2 = w * h
    c3 = l * h
    return 2 * c1 + 2 * c2 + 2 * c3 + min(c1, c2, c3)


def ribbon(l, w, h):
    peri = 0
    if l <= h and w <= h:
        peri = 2 * l + 2 * w
    elif l <= w and h <= w:
        peri = 2 * l + 2 * h
    else:
        peri = 2 * w + 2 * h
    return peri + l * w * h


with open("input02.txt", "r") as file:
    while line := file.readline():
        values = line.split("x")
        total += ribbon(int(values[0]), int(values[1]), int(values[2]))
    file.close()

print(total)
