import re


def part1() -> int:
    instruction = None
    with open("../data/input3.txt") as inp:
        instruction = "".join(inp.readlines())

    pat = re.compile(r"mul\((\d+),(\d+)\)")
    matches = [(int(i), int(j)) for i, j in pat.findall(instruction)]

    result = sum([i * j for i, j in matches])

    return result


def part2() -> int:
    instruction = None
    with open("../data/input3.txt") as inp:
        instruction = "".join(inp.readlines())

    do_pat = re.compile(r"do\(\)")
    dont_pat = re.compile(r"don\'t\(\)")
    pat = re.compile(r"mul\((\d+),(\d+)\)")

    muls = pat.finditer(instruction)
    dos = do_pat.finditer(instruction)
    donts = dont_pat.finditer(instruction)

    enabled = True

    result = 0

    arr = sorted(list(muls) + list(dos) + list(donts), key=lambda x: x.span()[0])

    for m in arr:
        if m.re == pat and enabled:
            result += int(m.groups()[0]) * int(m.groups()[1])
        elif m.re == do_pat:
            enabled = True
        elif m.re == dont_pat:
            enabled = False

    return result


print(part1())
print(part2())
