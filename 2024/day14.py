#!/usr/bin/env python3

import sys
import pyperclip as pc
import aocparser as ap


def part1(filename):
    result = 0
    with open(filename, "r") as file:
        lines = ap.file2lines(file)
        R = 103
        C = 101
        mat = [[0 for _ in range(C)] for _ in range(R)]
        dic_robot = {}
        num_robot = 0
        for l in lines:
            split1 = l.strip().split(" ")
            splitpos = split1[0].strip().split("=")
            splitvit = split1[1].strip().split("=")
            x, y = splitpos[1].strip().split(",")
            vx, vy = splitvit[1].strip().split(",")
            x, y, vx, vy = int(x), int(y), int(vx), int(vy)
            dic_robot[num_robot] = [y, x, vy, vx]
            num_robot += 1

        for _ in range(100):
            for i in range(num_robot):
                tmp = dic_robot[i]
                dic_robot[i] = [
                    (tmp[0] + tmp[2]) % R,
                    (tmp[1] + tmp[3]) % C,
                    tmp[2],
                    tmp[3],
                ]

        upl, upr, dnl, dnr = 0, 0, 0, 0
        for i in range(num_robot):
            y, x = dic_robot[i][0], dic_robot[i][1]
            mat[y][x] += 1
            if y < R // 2 and x < C // 2:
                upl += 1
            if y < R // 2 and x > C // 2:
                upr += 1
            if y > R // 2 and x < C // 2:
                dnl += 1
            if y > R // 2 and x > C // 2:
                dnr += 1

        result = upl * upr * dnl * dnr

    return result


def part2(filename):
    result = 0
    with open(filename, "r") as file:
        lines = ap.file2lines(file)
        R = 103
        C = 101
        dic_robot = {}
        num_robot = 0
        for l in lines:
            split1 = l.strip().split(" ")
            splitpos = split1[0].strip().split("=")
            splitvit = split1[1].strip().split("=")
            x, y = splitpos[1].strip().split(",")
            vx, vy = splitvit[1].strip().split(",")
            x, y, vx, vy = int(x), int(y), int(vx), int(vy)
            dic_robot[num_robot] = [y, x, vy, vx]
            num_robot += 1

        iter = 1
        while True:
            for i in range(num_robot):
                tmp = dic_robot[i]
                dic_robot[i] = [
                    (tmp[0] + tmp[2]) % R,
                    (tmp[1] + tmp[3]) % C,
                    tmp[2],
                    tmp[3],
                ]

            mat = [["." for _ in range(C)] for _ in range(R)]
            for i in range(num_robot):
                y, x = dic_robot[i][0], dic_robot[i][1]
                mat[y][x] = "#"

            components = 0
            seen = set()
            for y in range(R):
                for x in range(C):
                    if mat[y][x] == "#" and (y, x) not in seen:
                        sx, sy = x, y
                        components += 1
                        fifo = [(sy, sx)]
                        while fifo != []:
                            y2, x2 = fifo.pop(0)
                            if (y2, x2) in seen:
                                continue
                            seen.add((y2, x2))
                            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                xx, yy = x2 + dx, y2 + dy
                                if 0 <= yy < R and 0 <= xx < C and mat[yy][xx] == "#":
                                    fifo.append((yy, xx))

            if components <= 150:
                result = iter
                for e in mat:
                    for ee in e:
                        print(ee, end="")
                    print()
                break
            else:
                iter += 1

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
