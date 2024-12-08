#!/usr/bin/env python3

import sys
import pyperclip as pc
import aocparser as ap


def part1(filename):
    result = 0
    with open(filename, "r") as file:
        mat = ap.file2mat(file)
        R = len(mat)
        C = len(mat[0])
        antinode = set()

        for rr in range(R):
            for cc in range(C):
                if mat[rr][cc] == ".":
                    continue
                candidat = mat[rr][cc]
                for dr in range(R):
                    for dc in range(C):
                        if rr == dr and cc == dc:
                            continue
                        other = mat[dr][dc]
                        if other != candidat:
                            continue
                        diffr = dr - rr
                        diffc = dc - cc
                        if 0 <= (2 * diffr + rr) < R and 0 <= (2 * diffc + cc) < C:
                            antinode.add((2 * diffr + rr, 2 * diffc + cc))

        result = len(antinode)

    return result


def part2(filename):
    result = 0
    with open(filename, "r") as file:
        mat = ap.file2mat(file)
        R = len(mat)
        C = len(mat[0])
        antinode = set()

        for rr in range(R):
            for cc in range(C):
                if mat[rr][cc] == ".":
                    continue
                candidat = mat[rr][cc]
                for dr in range(R):
                    for dc in range(C):
                        if rr == dr and cc == dc:
                            continue
                        other = mat[dr][dc]
                        if other != candidat:
                            continue
                        diffr = dr - rr
                        diffc = dc - cc

                        i = 1
                        while True:
                            if 0 <= (i * diffr + rr) < R and 0 <= (i * diffc + cc) < C:
                                antinode.add((i * diffr + rr, i * diffc + cc))
                                i += 1
                            else:
                                break

        result = len(antinode)
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
