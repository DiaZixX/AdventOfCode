#! /usr/bin/env python3

score = 0
pos = 0

with open("input01.txt", "r") as file:
    content = file.read()
    for carac in content:
        if carac == "(":
            score += 1
            pos += 1
        elif carac == ")":
            score -= 1
            pos += 1
        else:
            continue
        if score == -1:
            break
    file.close()

print(pos)
