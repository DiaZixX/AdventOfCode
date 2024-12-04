#!/usr/bin/env python3

import sys
import pyperclip as pc
import aocparser as ap

letters = ["X", "M", "A", "S"]
letters_rev = ["S", "A", "M", "X"]

xlet = ["M", "A", "S"]
xlet_rev = ["S", "A", "M"]


def hori(mat, i, j, let):
    if (
        j + 3 < len(mat[0])
        and mat[i][j] == let[0]
        and mat[i][j + 1] == let[1]
        and mat[i][j + 2] == let[2]
        and mat[i][j + 3] == let[3]
    ):
        return True


def verti(mat, i, j, let):
    if (
        i + 3 < len(mat)
        and mat[i][j] == let[0]
        and mat[i + 1][j] == let[1]
        and mat[i + 2][j] == let[2]
        and mat[i + 3][j] == let[3]
    ):
        return True


def diagdown(mat, i, j, let):
    if (
        i + 3 < len(mat)
        and j + 3 < len(mat[0])
        and mat[i][j] == let[0]
        and mat[i + 1][j + 1] == let[1]
        and mat[i + 2][j + 2] == let[2]
        and mat[i + 3][j + 3] == let[3]
    ):
        return True


def diagup(mat, i, j, let):
    if (
        i - 3 >= 0
        and j + 3 < len(mat[0])
        and mat[i][j] == let[0]
        and mat[i - 1][j + 1] == let[1]
        and mat[i - 2][j + 2] == let[2]
        and mat[i - 3][j + 3] == let[3]
    ):
        return True


def cross(mat, i, j):
    return (
        i + 2 < len(mat)
        and j + 2 < len(mat[0])
        and (
            (
                mat[i][j] == "M"
                and mat[i + 1][j + 1] == "A"
                and mat[i + 2][j + 2] == "S"
                and mat[i + 2][j] == "M"
                and mat[i][j + 2] == "S"
            )
            or (
                mat[i][j] == "M"
                and mat[i + 1][j + 1] == "A"
                and mat[i + 2][j + 2] == "S"
                and mat[i + 2][j] == "S"
                and mat[i][j + 2] == "M"
            )
            or (
                mat[i][j] == "S"
                and mat[i + 1][j + 1] == "A"
                and mat[i + 2][j + 2] == "M"
                and mat[i + 2][j] == "M"
                and mat[i][j + 2] == "S"
            )
            or (
                mat[i][j] == "S"
                and mat[i + 1][j + 1] == "A"
                and mat[i + 2][j + 2] == "M"
                and mat[i + 2][j] == "S"
                and mat[i][j + 2] == "M"
            )
        )
    )


def check(mat, i, j):
    ret = 0
    if hori(mat, i, j, letters):
        ret += 1
    if hori(mat, i, j, letters_rev):
        ret += 1
    if verti(mat, i, j, letters):
        ret += 1
    if verti(mat, i, j, letters_rev):
        ret += 1
    if diagup(mat, i, j, letters):
        ret += 1
    if diagup(mat, i, j, letters_rev):
        ret += 1
    if diagdown(mat, i, j, letters):
        ret += 1
    if diagdown(mat, i, j, letters_rev):
        ret += 1
    return ret


def part1(filename):
    result = 0
    with open(filename, "r") as file:
        mat = ap.file2mat(file)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                result += check(mat, i, j)
    return result


def part2(filename):
    result = 0
    with open(filename, "r") as file:
        mat = ap.file2mat(file)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if cross(mat, i, j):
                    result += 1
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
