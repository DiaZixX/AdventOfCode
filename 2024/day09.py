#!/usr/bin/env python3

import sys
import pyperclip as pc
import aocparser as ap


def part1(filename):
    result = 0
    with open(filename, "r") as file:
        line = ap.file2lines(file)[0]
        id = 0
        disk = []
        for i, e in enumerate(line):
            if i % 2 != 0:
                disk.append([int(e), "."])
            else:
                disk.append([int(e), str(id)])
                id += 1

        for i in range(len(disk) - 1, -1, -1):
            if disk[i][1] == ".":
                continue
            else:
                nb = disk[i][0]
                for j in range(0, i):
                    if nb == 0:
                        break
                    if disk[j][1] == ".":
                        if disk[j][0] == disk[i][0]:
                            disk[j][1], disk[i][1] = disk[i][1], disk[j][1]
                            break
                        elif disk[j][0] < disk[i][0]:
                            disk[j][1] = disk[i][1]
                            disk[i][0] -= disk[j][0]
                            nb -= disk[j][0]
                        else:
                            disk.insert(j + 1, [disk[j][0] - disk[i][0], "."])
                            i += 1
                            disk[j], disk[i] = disk[i], disk[j]
                            break

        flatten_disk = []
        while disk != []:
            e = disk.pop()
            for _ in range(e[0]):
                flatten_disk.append(e[1])

        flatten_disk.reverse()

        for i, val in enumerate(flatten_disk):
            if val != ".":
                result += i * int(val)
            else:
                break

    return result


def part2(filename):
    result = 0
    with open(filename, "r") as file:
        line = ap.file2lines(file)[0]
        id = 0
        disk = []
        for i, e in enumerate(line):
            if i % 2 != 0:
                disk.append([int(e), "."])
            else:
                disk.append([int(e), str(id)])
                id += 1

        for i in range(len(disk) - 1, -1, -1):
            if disk[i][1] == ".":
                continue
            else:
                for j in range(0, i):
                    if disk[j][1] == "." and disk[i][0] == disk[j][0]:
                        disk[j], disk[i] = disk[i], disk[j]
                        break
                    elif disk[j][1] == "." and disk[i][0] < disk[j][0]:
                        length_exceed = disk[j][0] - disk[i][0]
                        disk.insert(j + 1, [length_exceed, "."])
                        i += 1
                        disk[j][0] = disk[i][0]
                        disk[j], disk[i] = disk[i], disk[j]
                        break

        flatten_disk = []
        while disk != []:
            e = disk.pop()
            for _ in range(e[0]):
                flatten_disk.append(e[1])

        flatten_disk.reverse()

        for i, val in enumerate(flatten_disk):
            if val != ".":
                result += i * int(val)

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
