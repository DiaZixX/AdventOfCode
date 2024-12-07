#!/usr/bin/env python3

import sys
import pyperclip as pc
import aocparser as ap


def recursive_solve(score, digits, current, part):
    if digits == [] and current == score:
        return True
    elif digits != [] and current <= score:
        candidat = digits.pop(0)
        return (
            recursive_solve(score, digits.copy(), current + candidat, part)
            or recursive_solve(score, digits.copy(), current * candidat, part)
            or (
                part
                and recursive_solve(
                    score, digits.copy(), int(str(current) + str(candidat)), part
                )
            )
        )
    else:
        return False


def part1(filename):
    result = 0
    with open(filename, "r") as file:
        lines = ap.file2lines(file)
        splitted = ap.lines2split(lines, [":"])
        for ll in splitted:
            score = int(ll[0])
            digits = [int(x) for x in ll[1].split()]
            first = digits.pop(0)
            if recursive_solve(score, digits, first, False):
                result += score
    return result


def part2(filename):
    result = 0
    with open(filename, "r") as file:
        lines = ap.file2lines(file)
        splitted = ap.lines2split(lines, [":"])
        for ll in splitted:
            score = int(ll[0])
            digits = [int(x) for x in ll[1].split()]
            first = digits.pop(0)
            if recursive_solve(score, digits, first, True):
                result += score
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
