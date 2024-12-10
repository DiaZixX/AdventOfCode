#!/usr/bin/env python3

import sys
import pyperclip as pc
import aocparser as ap


def explore(mat, i, j, current, seen):
    if current == "9":
        if isinstance(seen, set):
            seen.add((i, j))
        if isinstance(seen, list):
            seen.append((i, j))
    if i - 1 >= 0 and int(mat[i - 1][j]) == int(current) + 1:
        explore(mat, i - 1, j, mat[i - 1][j], seen)
    if j - 1 >= 0 and int(mat[i][j - 1]) == int(current) + 1:
        explore(mat, i, j - 1, mat[i][j - 1], seen)
    if i + 1 < len(mat) and int(mat[i + 1][j]) == int(current) + 1:
        explore(mat, i + 1, j, mat[i + 1][j], seen)
    if j + 1 < len(mat[0]) and int(mat[i][j + 1]) == int(current) + 1:
        explore(mat, i, j + 1, mat[i][j + 1], seen)


def part1(filename):
    result = 0
    with open(filename, "r") as file:
        mat = ap.file2mat(file)
        R = len(mat)
        C = len(mat[0])
        for r in range(R):
            for c in range(C):
                if mat[r][c] == "0":
                    seen = set()
                    explore(mat, r, c, mat[r][c], seen)
                    result += len(seen)

    return result


def part2(filename):
    result = 0
    with open(filename, "r") as file:
        mat = ap.file2mat(file)
        R = len(mat)
        C = len(mat[0])
        for r in range(R):
            for c in range(C):
                if mat[r][c] == "0":
                    seen = []
                    explore(mat, r, c, mat[r][c], seen)
                    result += len(seen)
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
