#!/usr/bin/env python3

import sys
import pyperclip as pc
import aocparser as ap

mod_val = 16777216


def new_secret(n):
    # Step 1
    m = n * 64
    n = n ^ m
    n = n % mod_val
    # Step 2
    m = n // 32
    n = n ^ m
    n = n % mod_val
    # Step 3
    m = n * 2048
    n = n ^ m
    n = n % mod_val
    return n


def part1(filename):
    result = 0
    with open(filename, "r") as file:
        lines = ap.file2lines(file)
        for ll in lines:
            n = int(ll)
            for _ in range(2000):
                n = new_secret(n)
            result += n
    return result


def part2(filename):
    result = 0
    with open(filename, "r") as file:
        lines = ap.file2lines(file)
        dic = {}
        for ll in lines:
            n = int(ll)
            change = []
            values = [int(str(n)[-1])]
            seen = set()
            for _ in range(2000):
                m = new_secret(n)
                ones = int(str(m)[-1])
                change.append(ones - values[len(values) - 1])
                values.append(ones)
                n = m

            for i in range(4, len(change)):
                seq = tuple(change[(i - 4) : i])
                val = values[i]

                if seq not in dic:
                    dic[seq] = val
                else:
                    if seq not in seen:
                        dic[seq] += val
                seen.add(seq)

        best_score = 0
        best_key = []
        for key in dic:
            s = dic[key]
            if s > best_score:
                best_score = s
                best_key = key
        print(best_key, end=" ")
        result = best_score
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
