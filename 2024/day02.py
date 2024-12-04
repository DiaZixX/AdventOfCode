#!/usr/bin/env python3

import sys
import pyperclip as pc
import aocparser as ap


def safe(tab):
    is_sorted = tab == sorted(tab) or tab == sorted(tab, reverse=True)
    is_safe = True
    for i in range(len(tab) - 1):
        diff = abs(tab[i] - tab[i + 1])
        if not 1 <= diff <= 3:
            is_safe = False
            break
    return is_sorted and is_safe


def part1(filename):
    result = 0
    with open(filename, "r") as file:
        lines = ap.file2lines(file)
        for line in lines:
            stripped = list(map(int, line.split(" ")))
            if safe(stripped):
                result += 1
        file.close()
    return result


def part2(filename):
    result = 0
    with open(filename, "r") as file:
        lines = ap.file2lines(file)
        for line in lines:
            stripped = list(map(int, line.split(" ")))

            is_good = False
            for j in range(len(stripped)):
                tab = stripped[:j] + stripped[j + 1 :]
                if safe(tab):
                    is_good = True

            if is_good:
                result += 1
        file.close()
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
