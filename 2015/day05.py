#!/usr/bin/env python

import time

voyels = ["a", "e", "i", "o", "u"]
duo = ["ab", "cd", "pq", "xy"]

total = 0


def part1():
    global total
    with open("input05.txt", "r") as file:
        while line := file.readline():
            nb_voy = 0
            double = False
            pure = True
            old_carac = ""
            for carac in line:
                if carac in voyels:
                    nb_voy += 1
                if not double and old_carac == carac:
                    double = True
                if old_carac + carac in duo:
                    pure = False
                    break
                old_carac = carac
            if pure and double and nb_voy >= 3:
                total += 1
        file.close()


def part2():
    global total
    with open("input05.txt", "r") as file:
        while line := file.readline().strip("\n"):
            pair = []
            repeat = False
            binom = False
            last_binom = ""
            first = ""
            second = ""
            for carac in line:
                test = second + carac
                if test in pair and last_binom != test:
                    binom = True
                else:
                    pair.append(test)
                if carac == first and carac != second:
                    repeat = True
                first = second
                second = carac
                last_binom = test
            if binom and repeat:
                total += 1
            time.sleep(2)
        file.close()


part2()
print(total)
