import math
from itertools import product


def part1() -> int:
    equations = {}
    with open("../data/input7.txt", "r") as inp:
        lines = inp.readlines()
        for line in lines:
            res, values = line.split(":")
            equations[int(res)] = tuple(map(int, values.split()))
    operators = ["+", "*"]
    true_sum = 0

    for res in equations:
        vals = equations[res]
        found = False
        for ops_combo in product(operators, repeat=len(vals) - 1):
            curr = vals[0]
            for i, op in enumerate(ops_combo):
                if op == "+":
                    curr = curr + vals[i + 1]
                elif op == "*":
                    curr = curr * vals[i + 1]
            if curr == res:
                found = True
                break
        if found:
            true_sum += res

    return true_sum


def part2() -> int:
    equations = {}
    with open("../data/input7.txt", "r") as inp:
        lines = inp.readlines()
        for line in lines:
            res, values = line.split(":")
            equations[int(res)] = tuple(map(int, values.split()))

    operators = ["+", "*", "||"]
    true_sum = 0

    for res in equations:
        vals = equations[res]
        found = False
        for ops_combo in product(operators, repeat=len(vals) - 1):
            curr = vals[0]
            for i, op in enumerate(ops_combo):
                if op == "+":
                    curr = curr + vals[i + 1]
                elif op == "*":
                    curr = curr * vals[i + 1]
                elif op == "||":
                    curr = curr * (10 ** math.ceil(math.log10(vals[i + 1]) + 1)) + vals[i + 1]
            if curr == res:
                found = True
                break
        if found:
            true_sum += res

    return true_sum


print(part1())
print(part2())
