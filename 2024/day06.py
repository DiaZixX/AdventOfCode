#!/usr/bin/env python3

import sys
import pyperclip as pc
import aocparser as ap


def part1(filename):
    result = 0
    with open(filename, "r") as file:
        mat = ap.file2mat(file)

        posx, posy = 0, 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] in ["^", ">", "v", "<"]:
                    posy = i
                    posx = j

        while True:
            if mat[posy][posx] == "^":
                mat[posy][posx] = "X"
                if posy - 1 >= 0 and mat[posy - 1][posx] == "#":
                    mat[posy][posx] = ">"
                else:
                    posy -= 1
                    if posy >= 0:
                        mat[posy][posx] = "^"
                    else:
                        break
            if mat[posy][posx] == ">":
                mat[posy][posx] = "X"
                if posx + 1 < len(mat[0]) and mat[posy][posx + 1] == "#":
                    mat[posy][posx] = "v"
                else:
                    posx += 1
                    if posx < len(mat[0]):
                        mat[posy][posx] = ">"
                    else:
                        break
            if mat[posy][posx] == "v":
                mat[posy][posx] = "X"
                if posy + 1 < len(mat) and mat[posy + 1][posx] == "#":
                    mat[posy][posx] = "<"
                else:
                    posy += 1
                    if posy < len(mat):
                        mat[posy][posx] = "v"
                    else:
                        break
            if mat[posy][posx] == "<":
                mat[posy][posx] = "X"
                if posx - 1 >= 0 and mat[posy][posx - 1] == "#":
                    mat[posy][posx] = "^"
                else:
                    posx -= 1
                    if posx >= 0:
                        mat[posy][posx] = "<"
                    else:
                        break

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == "X":
                    result += 1

    return result


def part2(filename):
    result = 0
    with open(filename, "r") as file:
        mat = ap.file2mat(file)

        startx, starty = 0, 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] in ["^", ">", "v", "<"]:
                    starty = i
                    startx = j

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] in ["#", "^"]:
                    continue
                else:
                    mat[i][j] = "#"
                seen = set()

                posy = starty
                posx = startx
                dir = "^"

                while True:
                    if (posy, posx, dir) in seen:
                        result += 1
                        break
                    else:
                        seen.add((posy, posx, dir))

                    if dir == "^":
                        if posy - 1 >= 0 and mat[posy - 1][posx] == "#":
                            dir = ">"
                        else:
                            posy -= 1
                            if not posy >= 0:
                                break
                    if dir == ">":
                        if posx + 1 < len(mat[0]) and mat[posy][posx + 1] == "#":
                            dir = "v"
                        else:
                            posx += 1
                            if not posx < len(mat[0]):
                                break
                    if dir == "v":
                        if posy + 1 < len(mat) and mat[posy + 1][posx] == "#":
                            dir = "<"
                        else:
                            posy += 1
                            if not posy < len(mat):
                                break
                    if dir == "<":
                        if posx - 1 >= 0 and mat[posy][posx - 1] == "#":
                            dir = "^"
                        else:
                            posx -= 1
                            if not posx >= 0:
                                break

                mat[i][j] = "."

    return result


def pr(s):
    print(s)
    pc.copy(s)


def main():
    if len(sys.argv) != 2:
        print("Input missing !")
        sys.exit(1)

    filename = sys.argv[1]

    p1 = part1(filename)
    pr(p1)
    p2 = part2(filename)
    pr(p2)


if __name__ == "__main__":
    main()
