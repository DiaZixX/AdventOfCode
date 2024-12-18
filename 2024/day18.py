#!/usr/bin/env python3

import sys
import pyperclip as pc
import aocparser as ap
import heapq
import math

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def h(i, j, ti, tj):
    return int(math.sqrt((ti - i) ** 2 + (tj - j) ** 2))


def part1(filename):
    result = 0
    with open(filename, "r") as file:
        lines = ap.file2lines(file)
        R = 71
        C = 71
        mat = [["." for _ in range(C)] for _ in range(R)]
        for i in range(0, 1024):
            c, r = lines[i].strip().split(",")
            c, r = int(c), int(r)
            mat[r][c] = "#"

        sr, sc = 0, 0
        er, ec = R - 1, C - 1
        pq = []
        d = {}

        d[(sr, sc)] = 0
        heapq.heappush(pq, (0, sr, sc))
        while pq:
            p, r, c = heapq.heappop(pq)
            if r == er and c == ec:
                result = p
                break
            for dr, dc in dirs:
                if 0 <= r + dr < R and 0 <= c + dc < C and mat[r + dr][c + dc] != "#":
                    if d[(r, c)] + 1 < d.get((r + dr, c + dc), 999999999999):
                        d[(r + dr, c + dc)] = d[(r, c)] + 1
                        for i, e in enumerate(pq):
                            if e[1] == r + dr and e[2] == c + dc:
                                pq[i][0] = d[(r + dr, c + dc)] + h(
                                    r + dr, c + dc, er, ec
                                )
                                pq.sort(key=lambda x: x[0])
                                break
                        else:
                            heapq.heappush(
                                pq,
                                (
                                    d[(r + dr, c + dc)] + h(r + dr, c + dc, er, ec),
                                    r + dr,
                                    c + dc,
                                ),
                            )

    return result


def part2(filename):
    result = 0
    with open(filename, "r") as file:
        lines = ap.file2lines(file)
        R = 71
        C = 71
        falling_bytes = 1024
        mat = [["." for _ in range(C)] for _ in range(R)]
        for i in range(0, 1024):
            c, r = lines[i].strip().split(",")
            c, r = int(c), int(r)
            mat[r][c] = "#"

        sr, sc = 0, 0
        er, ec = R - 1, C - 1

        for j in range(falling_bytes, len(lines)):
            fc, fr = lines[j].strip().split(",")
            fc, fr = int(fc), int(fr)
            mat[fr][fc] = "#"

            pq = []
            d = {}
            trouve = False

            d[(sr, sc)] = 0
            heapq.heappush(pq, (0, sr, sc))
            while pq:
                p, r, c = heapq.heappop(pq)
                if r == er and c == ec:
                    result = p
                    trouve = True
                    break
                for dr, dc in dirs:
                    if (
                        0 <= r + dr < R
                        and 0 <= c + dc < C
                        and mat[r + dr][c + dc] != "#"
                    ):
                        if d[(r, c)] + 1 < d.get((r + dr, c + dc), 999999999999):
                            d[(r + dr, c + dc)] = d[(r, c)] + 1
                            for i, e in enumerate(pq):
                                if e[1] == r + dr and e[2] == c + dc:
                                    pq[i][0] = d[(r + dr, c + dc)] + h(
                                        r + dr, c + dc, er, ec
                                    )
                                    pq.sort(key=lambda x: x[0])
                                    break
                            else:
                                heapq.heappush(
                                    pq,
                                    (
                                        d[(r + dr, c + dc)] + h(r + dr, c + dc, er, ec),
                                        r + dr,
                                        c + dc,
                                    ),
                                )
            if not trouve:
                result = f"{fc},{fr}"
                break
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
