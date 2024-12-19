#!/usr/bin/env python3

import sys
import pyperclip as pc
import aocparser as ap


def possible(disp, patt):
    if disp == "":
        return True
    for p in patt:
        if disp[0 : len(p)] == p:
            test = possible(disp[len(p) :], patt)
            if test:
                return True
    return False


def part1(filename):
    result = 0
    with open(filename, "r") as file:
        chunks = ap.file2chunks(file)
        patterns = chunks[0].strip().split(", ")
        lines = chunks[1].strip().split("\n")
        for ll in lines:
            if possible(ll, patterns):
                result += 1
    return result


def all_possible(mem, disp, patt):
    if disp in mem:
        return mem[disp]
    ways = 0
    if disp == "":
        ways = 1
    for p in patt:
        if disp[0 : len(p)] == p:
            ways += all_possible(mem, disp[len(p) :], patt)
    mem[disp] = ways
    return ways


def part2(filename):
    result = 0
    with open(filename, "r") as file:
        chunks = ap.file2chunks(file)
        patterns = chunks[0].strip().split(", ")
        lines = chunks[1].strip().split("\n")
        memoi = {}
        for ll in lines:
            result += all_possible(memoi, ll, patterns)
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
