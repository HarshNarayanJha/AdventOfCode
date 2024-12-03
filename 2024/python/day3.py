import re

def part1() -> int:
    instruction = None
    with open("../data/input3.txt") as inp:
        instruction = ''.join(inp.readlines())

    pat = re.compile(r"mul\((\d+),(\d+)\)")
    matches = [(int(i), int(j)) for i, j in pat.findall(instruction)]

    result = sum([i * j for i, j in matches])

    return result


def part2() -> int: ...


print(part1())
print(part2())
