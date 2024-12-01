#!/usr/bin/env python3

import sys
import aocparser as ap


def diff(a, b):
    if a > b:
        return a - b
    else:
        return b - a


def part1(filename):
    result = 0
    with open(filename, "r") as file:
        lines = ap.file2lines(file)
        splitted = ap.lines2split(lines, ["   "])

        left = []
        right = []

        for e in splitted:
            left.append(int(e[0]))
            right.append(int(e[1]))

        left.sort()
        right.sort()

        for e in list(zip(left, right)):
            result += diff(e[0], e[1])

        file.close()
    return result


def part2(filename):
    result = 0
    with open(filename, "r") as file:
        lines = ap.file2lines(file)
        splitted = ap.lines2split(lines, ["   "])

        left = []
        right = []

        for e in splitted:
            left.append(int(e[0]))
            right.append(int(e[1]))

        left.sort()
        right.sort()

        for e in left:
            count = 0
            for check in right:
                if check == e:
                    count += 1
            result += count * e

        file.close()
    return result


def main():
    if len(sys.argv) != 2:
        print("Input missing !")
        sys.exit(1)

    filename = sys.argv[1]

    p1 = part1(filename)
    print(p1)
    p2 = part2(filename)
    print(p2)


if __name__ == "__main__":
    main()
