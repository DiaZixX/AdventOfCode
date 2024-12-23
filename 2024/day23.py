#!/usr/bin/env python3

import sys
import pyperclip as pc
import aocparser as ap


def part1(filename):
    result = 0
    with open(filename, "r") as file:
        lines = ap.file2lines(file)
        dic = {}
        for ll in lines:
            pc1, pc2 = ll.strip().split("-")
            if pc1 not in dic:
                dic[pc1] = [pc2]
            else:
                dic[pc1].append(pc2)
            if pc2 not in dic:
                dic[pc2] = [pc1]
            else:
                dic[pc2].append(pc1)

        seen = set()
        for key in dic:
            for key2 in dic[key]:
                for key3 in dic[key2]:
                    if key in dic[key3] and (key, key2, key3) not in seen:
                        if key[0] == "t" or key2[0] == "t" or key3[0] == "t":
                            result += 1
                            seen.add((key, key2, key3))
                            seen.add((key, key3, key2))
                            seen.add((key2, key, key3))
                            seen.add((key2, key3, key))
                            seen.add((key3, key, key2))
                            seen.add((key3, key2, key))

    return result


def part2(filename):
    result = 0
    with open(filename, "r") as file:
        lines = ap.file2lines(file)
        dic = {}
        for ll in lines:
            pc1, pc2 = ll.strip().split("-")
            if pc1 not in dic:
                dic[pc1] = [pc2]
            else:
                dic[pc1].append(pc2)
            if pc2 not in dic:
                dic[pc2] = [pc1]
            else:
                dic[pc2].append(pc1)

        best = []

        for key in dic:
            composition = [key]
            for key2 in dic[key]:
                for pc in composition:
                    if pc not in dic[key2]:
                        break
                else:
                    composition.append(key2)
            if len(composition) > len(best):
                best = composition

        best.sort()
        print(len(best), best)
        ret = ""
        for e in best:
            ret += f"{e},"

        result = ret[: len(ret) - 1]

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
