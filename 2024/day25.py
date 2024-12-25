#!/usr/bin/env python3

import sys
import pyperclip as pc
import aocparser as ap


def part1(filename):
    result = 0
    with open(filename, "r") as file:
        chunks = ap.file2chunks(file)
        keys = []
        locks = []
        for c in chunks:
            mat = []
            for ll in c.strip().split("\n"):
                mat.append([x for x in ll])
            tmp = [(-1) for _ in range(5)]
            for r in range(len(mat)):
                for c in range(len(mat[0])):
                    if mat[r][c] == "#":
                        tmp[c] += 1
            if mat[0][0] == ".":
                keys.append(tmp)
            else:
                locks.append(tmp)
        for lock in locks:
            for key in keys:
                for i in range(len(key)):
                    if lock[i] + key[i] >= 6:
                        break
                else:
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


if __name__ == "__main__":
    main()
