#!/usr/bin/env python3

import sys
import pyperclip as pc
import aocparser as ap

dirs = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def part1(filename):
    result = 0
    with open(filename, "r") as file:
        chunks = ap.file2chunks(file)
        desc_mat = chunks[0].strip().split()
        mat = []
        for ll in desc_mat:
            tmp = []
            for e in ll:
                tmp.append(e)
            mat.append(tmp)
        moves = chunks[1].strip().split()
        sequence = []
        for ll in moves:
            sequence += [x for x in ll]

        R = len(mat)
        C = len(mat[0])

        r, c = 0, 0
        for i in range(R):
            for j in range(C):
                if mat[i][j] == "@":
                    r, c = i, j
                    mat[r][c] = "."

        for e in sequence:
            dr, dc = dirs[e]
            rr, cc = r + dr, c + dc
            if mat[rr][cc] == "#":
                continue
            elif mat[rr][cc] == ".":
                r, c = rr, cc
            elif mat[rr][cc] == "O":
                stack = [(r, c)]
                seen = set()
                good = True
                while stack != []:
                    rr, cc = stack.pop(0)
                    if (rr, cc) in seen:
                        continue
                    seen.add((rr, cc))
                    rrr, ccc = rr + dr, cc + dc
                    if mat[rrr][ccc] == "#":
                        good = False
                        break
                    if mat[rrr][ccc] == "O":
                        stack.append((rrr, ccc))
                if not good:
                    continue
                while len(seen) > 0:
                    for rr, cc in sorted(seen):
                        rrr, ccc = rr + dr, cc + dc
                        if (rrr, ccc) not in seen:
                            mat[rrr][ccc] = mat[rr][cc]
                            mat[rr][cc] = "."
                            seen.remove((rr, cc))
                r = r + dr
                c = c + dc

        for r in range(R):
            for c in range(C):
                if mat[r][c] == "O":
                    result += r * 100 + c

    return result


def part2(filename):
    result = 0
    with open(filename, "r") as file:
        chunks = ap.file2chunks(file)
        desc_mat = chunks[0].strip().split()
        mat = []
        for ll in desc_mat:
            tmp = []
            for e in ll:
                if e == "#":
                    tmp.append("#")
                    tmp.append("#")
                if e == "O":
                    tmp.append("[")
                    tmp.append("]")
                if e == ".":
                    tmp.append(".")
                    tmp.append(".")
                if e == "@":
                    tmp.append("@")
                    tmp.append(".")
            mat.append(tmp)
        moves = chunks[1].strip().split()
        sequence = []
        for ll in moves:
            sequence += [x for x in ll]

        R = len(mat)
        C = len(mat[0])

        r, c = 0, 0
        for i in range(R):
            for j in range(C):
                if mat[i][j] == "@":
                    r, c = i, j
                    mat[r][c] = "."

        for e in sequence:
            dr, dc = dirs[e]
            rr, cc = r + dr, c + dc

            if mat[rr][cc] == "#":
                continue
            elif mat[rr][cc] == ".":
                r, c = rr, cc
            elif mat[rr][cc] in ["[", "]"]:
                stack = [(r, c)]
                seen = set()
                good = True
                while stack != []:
                    rr, cc = stack.pop(0)
                    if (rr, cc) in seen:
                        continue
                    seen.add((rr, cc))
                    rrr, ccc = rr + dr, cc + dc
                    if mat[rrr][ccc] == "#":
                        good = False
                        break
                    if mat[rrr][ccc] == "[":
                        stack.append((rrr, ccc))
                        stack.append((rrr, ccc + 1))
                    if mat[rrr][ccc] == "]":
                        stack.append((rrr, ccc))
                        stack.append((rrr, ccc - 1))
                if not good:
                    continue
                while len(seen) > 0:
                    for rr, cc in sorted(seen):
                        rrr, ccc = rr + dr, cc + dc
                        if (rrr, ccc) not in seen:
                            mat[rrr][ccc] = mat[rr][cc]
                            mat[rr][cc] = "."
                            seen.remove((rr, cc))
                r = r + dr
                c = c + dc

        for r in range(R):
            for c in range(C):
                if mat[r][c] == "[":
                    result += r * 100 + c

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
