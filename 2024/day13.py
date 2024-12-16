#!/usr/bin/env python3

import sys
import pyperclip as pc
import aocparser as ap


def part1(filename):
    result = 0
    with open(filename, "r") as file:
        chunks = ap.file2chunks(file)
        for c in chunks:
            btn_a, btn_b, prize = c.strip().split("\n")

            btn_a = btn_a.split(": ")[1].strip().split(", ")
            btn_a = (int(btn_a[0][2:]), int(btn_a[1][2:]))
            btn_b = btn_b.split(": ")[1].strip().split(", ")
            btn_b = (int(btn_b[0][2:]), int(btn_b[1][2:]))
            prize = prize.split(": ")[1].strip().split(", ")
            prize = (int(prize[0][2:]), int(prize[1][2:]))

            times_b = (prize[1] * btn_a[0] - prize[0] * btn_a[1]) / (
                btn_b[1] * btn_a[0] - btn_b[0] * btn_a[1]
            )
            times_a = (prize[0] - btn_b[0] * times_b) / btn_a[0]

            if (
                0 <= times_a <= 100
                and 0 <= times_b <= 100
                and times_a.is_integer()
                and times_b.is_integer()
            ):
                result += int(times_a) * 3 + int(times_b)

    return result


def part2(filename):
    result = 0
    with open(filename, "r") as file:
        chunks = ap.file2chunks(file)
        for c in chunks:
            btn_a, btn_b, prize = c.strip().split("\n")

            btn_a = btn_a.split(": ")[1].strip().split(", ")
            btn_a = (int(btn_a[0][2:]), int(btn_a[1][2:]))
            btn_b = btn_b.split(": ")[1].strip().split(", ")
            btn_b = (int(btn_b[0][2:]), int(btn_b[1][2:]))
            prize = prize.split(": ")[1].strip().split(", ")
            prize = (
                int(prize[0][2:]) + 10000000000000,
                int(prize[1][2:]) + 10000000000000,
            )

            times_b = (prize[1] * btn_a[0] - prize[0] * btn_a[1]) / (
                btn_b[1] * btn_a[0] - btn_b[0] * btn_a[1]
            )
            times_a = (prize[0] - btn_b[0] * times_b) / btn_a[0]

            if times_a.is_integer() and times_b.is_integer():
                result += int(times_a) * 3 + int(times_b)
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
