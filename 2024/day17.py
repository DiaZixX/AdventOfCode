#!/usr/bin/env python3

import sys
import pyperclip as pc
import aocparser as ap


def part1(filename):
    result = 0
    with open(filename, "r") as file:
        chunks = ap.file2chunks(file)
        register = chunks[0].strip().split("\n")
        regA = int(register[0].strip().split(": ")[1])
        regB = int(register[1].strip().split(": ")[1])
        regC = int(register[2].strip().split(": ")[1])
        sequence = [int(x) for x in chunks[1].strip().split(":")[1].strip().split(",")]

        i = 0
        out = []
        while i < len(sequence):
            match sequence[i]:
                case 0:
                    if 0 <= sequence[i + 1] <= 3:
                        regA = regA // (2 ** sequence[i + 1])
                    elif sequence[i + 1] == 4:
                        regA = regA // (2**regA)
                    elif sequence[i + 1] == 5:
                        regA = regA // (2**regB)
                    elif sequence[i + 1] == 5:
                        regA = regA // (2**regC)
                    else:
                        return
                    i += 2
                case 1:
                    regB = regB ^ sequence[i + 1]
                    i += 2
                case 2:
                    if 0 <= sequence[i + 1] <= 3:
                        regB = sequence[i + 1]
                    elif sequence[i + 1] == 4:
                        regB = regA % 8
                    elif sequence[i + 1] == 5:
                        regB = regB % 8
                    elif sequence[i + 1] == 5:
                        regB = regC % 8
                    else:
                        return
                    i += 2
                case 3:
                    if regA == 0:
                        i += 2
                    else:
                        i = sequence[i + 1]
                case 4:
                    regB = regB ^ regC
                    i += 2
                case 5:
                    if 0 <= sequence[i + 1] <= 3:
                        out.append(sequence[i + 1])
                    elif sequence[i + 1] == 4:
                        out.append(regA % 8)
                    elif sequence[i + 1] == 5:
                        out.append(regB % 8)
                    elif sequence[i + 1] == 5:
                        out.append(regC % 8)
                    else:
                        return
                    i += 2
                case 6:
                    if 0 <= sequence[i + 1] <= 3:
                        regB = regA // (2 ** sequence[i + 1])
                    elif sequence[i + 1] == 4:
                        regB = regA // (2**regA)
                    elif sequence[i + 1] == 5:
                        regB = regA // (2**regB)
                    elif sequence[i + 1] == 5:
                        regB = regA // (2**regC)
                    else:
                        return
                    i += 2
                case 7:
                    if 0 <= sequence[i + 1] <= 3:
                        regC = regA // (2 ** sequence[i + 1])
                    elif sequence[i + 1] == 4:
                        regC = regA // (2**regA)
                    elif sequence[i + 1] == 5:
                        regC = regA // (2**regB)
                    elif sequence[i + 1] == 5:
                        regC = regA // (2**regC)
                    else:
                        return
                    i += 2
                case _:
                    print("ERREUR")

        for i, e in enumerate(out):
            if i == 0:
                print(e, end="")
            else:
                print(f",{e}", end="")
        result = ""
    return result


def part2(filename):
    result = 0
    with open(filename, "r") as file:
        chunks = ap.file2chunks(file)
        register = chunks[0].strip().split("\n")
        regA = int(register[0].strip().split(": ")[1])
        regB = int(register[1].strip().split(": ")[1])
        regC = int(register[2].strip().split(": ")[1])
        sequence = [int(x) for x in chunks[1].strip().split(":")[1].strip().split(",")]

        start_A = 0o670536021
        incr_A = 8**9
        targ_sim = 8
        while True:
            start_A += incr_A
            regA = start_A
            i = 0
            out = []
            while i < len(sequence):
                match sequence[i]:
                    case 0:
                        if 0 <= sequence[i + 1] <= 3:
                            regA = regA // (2 ** sequence[i + 1])
                        elif sequence[i + 1] == 4:
                            regA = regA // (2**regA)
                        elif sequence[i + 1] == 5:
                            regA = regA // (2**regB)
                        elif sequence[i + 1] == 5:
                            regA = regA // (2**regC)
                        else:
                            return
                        i += 2
                    case 1:
                        regB = regB ^ sequence[i + 1]
                        i += 2
                    case 2:
                        if 0 <= sequence[i + 1] <= 3:
                            regB = sequence[i + 1]
                        elif sequence[i + 1] == 4:
                            regB = regA % 8
                        elif sequence[i + 1] == 5:
                            regB = regB % 8
                        elif sequence[i + 1] == 5:
                            regB = regC % 8
                        else:
                            return
                        i += 2
                    case 3:
                        if regA == 0:
                            i += 2
                        else:
                            i = sequence[i + 1]
                    case 4:
                        regB = regB ^ regC
                        i += 2
                    case 5:
                        if 0 <= sequence[i + 1] <= 3:
                            out.append(sequence[i + 1])
                        elif sequence[i + 1] == 4:
                            out.append(regA % 8)
                        elif sequence[i + 1] == 5:
                            out.append(regB % 8)
                        elif sequence[i + 1] == 5:
                            out.append(regC % 8)
                        else:
                            return
                        i += 2
                    case 6:
                        if 0 <= sequence[i + 1] <= 3:
                            regB = regA // (2 ** sequence[i + 1])
                        elif sequence[i + 1] == 4:
                            regB = regA // (2**regA)
                        elif sequence[i + 1] == 5:
                            regB = regA // (2**regB)
                        elif sequence[i + 1] == 5:
                            regB = regA // (2**regC)
                        else:
                            return
                        i += 2
                    case 7:
                        if 0 <= sequence[i + 1] <= 3:
                            regC = regA // (2 ** sequence[i + 1])
                        elif sequence[i + 1] == 4:
                            regC = regA // (2**regA)
                        elif sequence[i + 1] == 5:
                            regC = regA // (2**regB)
                        elif sequence[i + 1] == 5:
                            regC = regA // (2**regC)
                        else:
                            return
                        i += 2
                    case _:
                        print("ERREUR")
            if out == sequence:
                print(
                    "FOUND :",
                    start_A,
                    oct(start_A),
                    sequence,
                    out,
                    len(sequence),
                    len(out),
                )
                break
            else:
                similarity = 0
                for i in range(len(sequence)):
                    if i < len(out) and sequence[i] == out[i]:
                        similarity += 1
                    else:
                        break
                if similarity >= targ_sim:
                    targ_sim = similarity
                    print(
                        start_A,
                        oct(start_A),
                        similarity,
                        sequence,
                        out,
                        len(sequence),
                        len(out),
                    )

        result = start_A
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
