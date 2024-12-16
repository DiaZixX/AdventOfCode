#!/usr/bin/env python3

import heapq
from collections import deque
import sys
import pyperclip as pc
import aocparser as ap
import math as m

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def h(i, j, C):
    return int(m.sqrt((1 - i) ** 2 + (C - 2 - j) ** 2))


def part1(filename):
    result = 0
    with open(filename, "r") as file:
        mat = ap.file2mat(file)
        R = len(mat)
        C = len(mat[0])

        r, c = R - 2, 1
        dir = 1

        prio_stack = []
        d = {}

        for i in range(R):
            for j in range(C):
                if mat[i][j] != "#":
                    d[(i, j)] = 999999999999

        d[(r, c)] = 0
        heapq.heappush(prio_stack, (0, r, c, dir))

        while prio_stack != []:
            _, r, c, dir = heapq.heappop(prio_stack)

            if (r, c) == (1, C - 2):
                result = d[(r, c)]
                break

            for i, e in enumerate(dirs):
                dr, dc = e
                if mat[r + dr][c + dc] == "#":
                    continue
                if i == (dir + 2) % 4:
                    continue

                if i == (dir + 1) % 4 or i == (dir + 3) % 4:
                    weight = 1001
                else:
                    weight = 1

                if d[(r, c)] + weight < d[(r + dr, c + dc)]:
                    d[(r + dr, c + dc)] = d[(r, c)] + weight
                    for j in range(len(prio_stack)):
                        if (
                            prio_stack[j][1] == r + dr
                            and prio_stack[j][2] == c + dc
                            and prio_stack[j][3] == i
                        ):
                            prio_stack.pop(j)
                            break

                    heapq.heappush(
                        prio_stack,
                        (
                            d[(r + dr, c + dc)] + h(r + dr, c + dc, C),
                            r + dr,
                            c + dc,
                            i,
                        ),
                    )

    return result


def part2(filename):
    result = 0
    with open(filename, "r") as file:
        mat = ap.file2mat(file)
        R = len(mat)
        C = len(mat[0])

        r, c = R - 2, 1
        dir = 1

        prio_stack = []
        heapq.heappush(prio_stack, (0, r, c, dir))
        lowest_cost = {(r, c, dir): 0}
        backtrack = {}
        best_cost = 999999999999
        end_states = set()

        while prio_stack != []:
            cost, r, c, dir = heapq.heappop(prio_stack)
            dr, dc = dirs[dir]
            if cost > lowest_cost.get((r, c, dir), 999999999999):
                continue
            if r == 1 and c == C - 2:
                if cost > best_cost:
                    break
                best_cost = cost
                end_states.add((r, c, dir))
            for new_cost, nr, nc, ndir in [
                (cost + 1, r + dr, c + dc, dir),
                (cost + 1000, r, c, (dir + 1) % 4),
                (cost + 1000, r, c, (dir + 3) % 4),
            ]:
                if mat[nr][nc] == "#":
                    continue
                lowest = lowest_cost.get((nr, nc, ndir), 999999999999)
                if new_cost > lowest:
                    continue
                if new_cost < lowest:
                    backtrack[(nr, nc, ndir)] = set()
                    lowest_cost[(nr, nc, ndir)] = new_cost
                backtrack[(nr, nc, ndir)].add((r, c, dir))
                heapq.heappush(prio_stack, (new_cost, nr, nc, ndir))

        states = deque(end_states)
        seen = set(end_states)

        while states:
            key = states.popleft()
            for last in backtrack.get(key, []):
                if last in seen:
                    continue
                seen.add(last)
                states.append(last)

        result = len({(r, c) for r, c, _ in seen})
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
