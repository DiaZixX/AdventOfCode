#!/usr/bin/env python3

import sys
import pyperclip as pc
import aocparser as ap


def part1(filename):
    result = 0
    with open(filename, "r") as file:
        chunks = ap.file2chunks(file)
        order = ap.lines2split(chunks[0], ["\n", "|"])
        update = ap.lines2split(chunks[1], ["\n", ","])
        dic_before = {}

        for ll in order:
            if int(ll[1]) not in dic_before:
                dic_before[int(ll[1])] = [int(ll[0])]
            else:
                dic_before[int(ll[1])].append(int(ll[0]))

        for ll in update:
            pages = [int(x) for x in ll]
            good = True
            for i in range(len(pages) - 1):
                for j in range(i + 1, len(pages)):
                    if pages[j] in dic_before[pages[i]]:
                        good = False
            if good:
                result += pages[len(pages) // 2]

    return result


def part2(filename):
    result = 0
    with open(filename, "r") as file:
        chunks = ap.file2chunks(file)
        order = ap.lines2split(chunks[0], ["\n", "|"])
        update = ap.lines2split(chunks[1], ["\n", ","])
        dic_after = {}
        dic_before = {}

        for ll in order:
            if int(ll[0]) not in dic_after:
                dic_after[int(ll[0])] = [int(ll[1])]
            else:
                dic_after[int(ll[0])].append(int(ll[1]))
            if int(ll[1]) not in dic_before:
                dic_before[int(ll[1])] = [int(ll[0])]
            else:
                dic_before[int(ll[1])].append(int(ll[0]))

        for ll in update:
            pages = [int(x) for x in ll]
            good = True
            for i in range(len(pages) - 1):
                for j in range(i + 1, len(pages)):
                    if pages[j] in dic_before[pages[i]]:
                        good = False

            if not good:
                stack = []
                corrected = []
                topology = {}

                for p in pages:
                    temp = []
                    for b in dic_before[p]:
                        if b not in temp and b in pages:
                            temp.append(b)

                    topology[p] = len(temp)
                    if len(temp) == 0:
                        stack.append(p)

                while stack != []:
                    elem = stack.pop(0)
                    corrected.append(elem)
                    for a in dic_after:
                        if a in topology:
                            topology[a] -= 1
                            if topology[a] == 0:
                                stack.append(a)

                result += corrected[len(corrected) // 2]

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
