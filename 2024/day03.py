#!/usr/bin/env python3

import sys
import re
import pyperclip as pc
import aocparser as ap


def part1(filename):
    result = 0
    with open(filename, "r") as file:
        bigline = ap.file2oneline(file)
        for i in range(len(bigline)):
            matching = re.match(r"mul\((\d{1,3}),(\d{1,3})\)", bigline[i:])
            if matching is not None:
                x, y = int(matching.group(1)), int(matching.group(2))
                result += x * y
        file.close()
    return result


def part2(filename):
    result = 0
    good = True
    with open(filename, "r") as file:
        bigline = ap.file2oneline(file)
        for i in range(len(bigline)):
            if bigline[i:].startswith("do()"):
                good = True
            if bigline[i:].startswith("don't()"):
                good = False
            matching = re.match(r"mul\((\d{1,3}),(\d{1,3})\)", bigline[i:])
            if matching is not None:
                x, y = int(matching.group(1)), int(matching.group(2))
                if good:
                    result += x * y
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
