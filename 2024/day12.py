#!/usr/bin/env python3

import sys
import pyperclip as pc
import aocparser as ap

peri = 0
area = 0
sides = set()


def parcours(mat, i, j, letter, seen, facing):
    global peri
    global area
    global sides
    if not (i >= 0 and j >= 0 and i < len(mat) and j < len(mat[0])):
        peri += 1
        sides.add((i, j, facing))
    elif mat[i][j] == letter:
        if (i, j) in seen:
            return
        area += 1
        seen.add((i, j))
        parcours(mat, i + 1, j, letter, seen, "S")
        parcours(mat, i - 1, j, letter, seen, "N")
        parcours(mat, i, j + 1, letter, seen, "E")
        parcours(mat, i, j - 1, letter, seen, "W")
    else:
        peri += 1
        sides.add((i, j, facing))


def part1(filename):
    global peri
    global area
    result = 0
    with open(filename, "r") as file:
        mat = ap.file2mat(file)
        R = len(mat)
        C = len(mat[0])
        done = set()
        for rr in range(R):
            for cc in range(C):
                if (rr, cc) in done:
                    continue
                else:
                    area = 0
                    peri = 0
                    seen = set()
                    parcours(mat, rr, cc, mat[rr][cc], seen, "")
                    result += area * peri
                    done.update(seen)
    return result


def part2(filename):
    global area
    global sides
    result = 0
    with open(filename, "r") as file:
        mat = ap.file2mat(file)
        R = len(mat)
        C = len(mat[0])
        done = set()
        for rr in range(R):
            for cc in range(C):
                if (rr, cc) in done:
                    continue
                else:
                    area = 0
                    sides = set()
                    seen = set()
                    parcours(mat, rr, cc, mat[rr][cc], seen, "")
                    count_sides = 0
                    for d in ["N", "S"]:
                        filtered = [x for x in sides if x[2] == d]
                        if filtered == []:
                            continue
                        filtered.sort(key=lambda x: (x[0], x[1]))
                        i = filtered[0][0]
                        j = filtered[0][1]
                        while filtered != []:
                            ni, nj, _ = filtered.pop(0)
                            if ni != i or nj != j + 1:
                                count_sides += 1
                            i = ni
                            j = nj
                    for d in ["W", "E"]:
                        filtered = [x for x in sides if x[2] == d]
                        if filtered == []:
                            continue
                        filtered.sort(key=lambda x: (x[1], x[0]))
                        i = filtered[0][0]
                        j = filtered[0][1]
                        while filtered != []:
                            ni, nj, _ = filtered.pop(0)
                            if ni != i + 1 or nj != j:
                                count_sides += 1
                            i = ni
                            j = nj
                    result += area * count_sides
                    done.update(seen)
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
