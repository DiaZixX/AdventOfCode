#!/usr/bin/env python3

import sys
import pyperclip as pc
import aocparser as ap


def apply_gate(a, b, gate):
    if gate == "XOR":
        return a ^ b
    elif gate == "AND":
        return a & b
    else:
        return a | b


def check_z(tab):
    for e in tab:
        if e == -1:
            return False
    return True


def value_of_tab(tab):
    tab.reverse()
    ret = ""
    for e in tab:
        ret += str(e)
    return int(ret, 2)


def convert_to_binary_array(number):
    if number == 0:
        return [0]
    binary_array = []
    while number > 0:
        binary_array.append(number % 2)
        number //= 2
    binary_array.reverse()
    return binary_array


def part1(filename):
    result = 0
    with open(filename, "r") as file:
        chunks = ap.file2chunks(file)
        init_values = chunks[0].strip().split("\n")
        wire_d = {}
        for iv in init_values:
            w, val = iv.split(": ")
            wire_d[w] = int(val)

        gate_d = {}

        gate = chunks[1].strip().split("\n")
        for g in gate:
            splitted = g.strip().split(" ")
            if (splitted[0], splitted[2]) not in gate_d:
                gate_d[(splitted[0], splitted[2])] = [(splitted[1], splitted[4])]
            else:
                gate_d[(splitted[0], splitted[2])].append((splitted[1], splitted[4]))

            if splitted[0] not in wire_d:
                wire_d[splitted[0]] = -1
            if splitted[2] not in wire_d:
                wire_d[splitted[2]] = -1
            if (
                splitted[0] in wire_d
                and splitted[2] in wire_d
                and wire_d[splitted[0]] != -1
                and wire_d[splitted[2]] != -1
            ):
                wire_d[splitted[4]] = apply_gate(
                    wire_d[splitted[0]], wire_d[splitted[2]], splitted[1]
                )
            else:
                wire_d[splitted[4]] = -1

        z = []
        for key in wire_d:
            if key[0] == "z":
                z.append(-1)

        while not check_z(z):
            for key in wire_d:
                for c, gg in gate_d.items():
                    for g in gg:
                        if g[1] == key and wire_d[c[0]] != -1 and wire_d[c[1]] != -1:
                            wire_d[key] = apply_gate(wire_d[c[0]], wire_d[c[1]], g[0])
                if key[0] == "z":
                    z[int(key[1:])] = wire_d[key]

        z.reverse()
        print(z)
        result = ""
        for e in z:
            result += str(e)
        result = int(result, 2)

    return result


def graphviz(gates):
    print("strict digraph {")
    for g in gates:
        n1, n2 = g
        for op, n3 in gates[g]:
            print(f"  {n1} -> {n3} [label={op}]")
            print(f"  {n2} -> {n3} [label={op}]")
    print("}")


def part2(filename):
    result = 0
    with open(filename, "r") as file:
        chunks = ap.file2chunks(file)
        init_values = chunks[0].strip().split("\n")
        wire_d = {}
        max_x, max_y = 0, 0
        for iv in init_values:
            w, val = iv.split(": ")
            wire_d[w] = int(val)
            if w[0] == "x":
                if int(w[1:]) > max_x:
                    max_x = int(w[1:])
            if w[0] == "y":
                if int(w[1:]) > max_y:
                    max_y = int(w[1:])

        gate_d = {}

        gate = chunks[1].strip().split("\n")
        for g in gate:
            splitted = g.strip().split(" ")
            if (splitted[0], splitted[2]) not in gate_d:
                gate_d[(splitted[0], splitted[2])] = [(splitted[1], splitted[4])]
            else:
                gate_d[(splitted[0], splitted[2])].append((splitted[1], splitted[4]))

            if splitted[0] not in wire_d:
                wire_d[splitted[0]] = -1
            if splitted[2] not in wire_d:
                wire_d[splitted[2]] = -1
            if (
                splitted[0] in wire_d
                and splitted[2] in wire_d
                and wire_d[splitted[0]] != -1
                and wire_d[splitted[2]] != -1
            ):
                wire_d[splitted[4]] = apply_gate(
                    wire_d[splitted[0]], wire_d[splitted[2]], splitted[1]
                )
            else:
                wire_d[splitted[4]] = -1

        x = [-1 for _ in range(max_x + 1)]
        y = [-1 for _ in range(max_y + 1)]
        z = []
        for key in wire_d:
            if key[0] == "z":
                z.append(-1)
            if key[0] == "x":
                x[int(key[1:])] = wire_d[key]
            if key[0] == "y":
                y[int(key[1:])] = wire_d[key]

        val_x = value_of_tab(x)
        val_y = value_of_tab(y)
        print(x, val_x)
        print(y, val_y)

        while not check_z(z):
            for key in wire_d:
                for c, gg in gate_d.items():
                    for g in gg:
                        if g[1] == key and wire_d[c[0]] != -1 and wire_d[c[1]] != -1:
                            wire_d[key] = apply_gate(wire_d[c[0]], wire_d[c[1]], g[0])
                if key[0] == "z":
                    z[int(key[1:])] = wire_d[key]

        target = convert_to_binary_array(val_x + val_y)
        print("Target : ", len(target))
        print(target, val_x + val_y)
        print(z, value_of_tab(z))

        # Found with graphviz (uncomment next line to print the graph)
        # graphviz(gate_d)
        solution = ["z08", "vvr"] + ["bkr", "rnq"] + ["tfb", "z28"] + ["z39", "mqh"]
        solution.sort()
        ret = ""
        print(solution)
        for e in solution:
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
