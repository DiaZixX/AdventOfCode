#!/usr/bin/env python3

import sys
import pyperclip as pc
import aocparser as ap

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def dfs(mat, sr, sc, er, ec, path):
    r, c = sr, sc
    poids = 0
    path[(sr, sc)] = poids
    while (r, c) != (er, ec):
        poids += 1
        for dr, dc in dirs:
            if mat[r + dr][c + dc] != "#" and (r + dr, c + dc) not in path:
                path[(r + dr, c + dc)] = poids
                r += dr
                c += dc
                break


def part1(filename):
    result = 0
    with open(filename, "r") as file:
        mat = ap.file2mat(file)
        R = len(mat)
        C = len(mat[0])

        sr, sc, er, ec = 0, 0, 0, 0
        for r in range(R):
            for c in range(C):
                if mat[r][c] == "S":
                    sr, sc = r, c
                if mat[r][c] == "E":
                    er, ec = r, c

        path = {}
        dfs(mat, sr, sc, er, ec, path)

        for i in range(1, R - 1):
            for j in range(1, C - 1):
                if mat[i][j] == ".":
                    continue
                else:
                    for di, dj in dirs[:2]:
                        if (
                            1 <= i + di < R - 1
                            and 1 <= j + dj < C - 1
                            and mat[i + di][j + dj] != "#"
                            and mat[i - di][j - dj] != "#"
                        ):
                            if (
                                abs(path[(i + di, j + dj)] - path[(i - di, j - dj)]) - 2
                                >= 100
                            ):
                                result += 1

    return result


def dist(i1, j1, i2, j2):
    return abs(i1 - i2) + abs(j1 - j2)


def part2(filename):
    result = 0
    with open(filename, "r") as file:
        mat = ap.file2mat(file)
        R = len(mat)
        C = len(mat[0])

        sr, sc, er, ec = 0, 0, 0, 0
        for r in range(R):
            for c in range(C):
                if mat[r][c] == "S":
                    sr, sc = r, c
                if mat[r][c] == "E":
                    er, ec = r, c

        path = {}
        dfs(mat, sr, sc, er, ec, path)

        cheats = set()
        for i in range(1, R - 1):
            for j in range(1, C - 1):
                if mat[i][j] == "#":
                    continue
                mini = max(1, i - 21)
                maxi = min(R - 1, i + 21)
                minj = max(1, j - 21)
                maxj = min(C - 1, j + 21)
                for di in range(mini, maxi):
                    for dj in range(minj, maxj):
                        if mat[di][dj] == "#":
                            continue
                        if dist(i, j, di, dj) <= 20:
                            if abs(path[(i, j)] - path[(di, dj)]) - dist(
                                i, j, di, dj
                            ) >= 100 and (
                                (i, j, di, dj) not in cheats
                                or (di, dj, i, j) not in cheats
                            ):
                                cheats.add((i, j, di, dj))
                                cheats.add((di, dj, i, j))
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
    p2 = part2(filename)
    pr(p2)


if __name__ == "__main__":
    main()
