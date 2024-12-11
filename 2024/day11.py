#!/usr/bin/env python3

import sys
import pyperclip as pc
import aocparser as ap

dic = {}


def memoi(x, steps):
    if (x, steps) in dic:
        return dic[(x, steps)]
    ret = 0
    if steps == 0:
        ret = 1
    elif x == 0:
        ret = memoi(1, steps - 1)
    elif len(str(x)) % 2 == 0:
        ret = memoi(int(str(x)[: len(str(x)) // 2]), steps - 1) + memoi(
            int(str(x)[len(str(x)) // 2 :]), steps - 1
        )
    else:
        ret = memoi(x * 2024, steps - 1)
    dic[(x, steps)] = ret
    return ret


def part1(filename):
    result = 0
    with open(filename, "r") as file:
        line = ap.file2lines(file)
        line = [int(x) for x in line[0].split()]
        for e in line:
            result += memoi(e, 25)
    return result


def part2(filename):
    result = 0
    with open(filename, "r") as file:
        line = ap.file2lines(file)
        line = [int(x) for x in line[0].split()]
        for e in line:
            result += memoi(e, 75)
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
    # print(len(dic))
    p2 = part2(filename)
    pr(p2)
    # print(len(dic))


if __name__ == "__main__":
    main()
