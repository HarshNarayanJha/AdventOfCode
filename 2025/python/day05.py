def part1() -> int:
    with open("../data/input05.txt", "r") as fp:
        lines = fp.read().strip().split("\n\n")

    ranges = []
    igns = lines[1].splitlines()

    for r in lines[0].splitlines():
        a, b = map(int, r.split("-"))
        ranges.append((a, b))

    igns = list(map(int, igns))

    ct = 0
    for i in igns:
        for s, e in ranges:
            if s <= i <= e:
                ct += 1
                break

    return ct


def part2() -> int:
    with open("../data/input05.txt", "r") as fp:
        lines = fp.read().strip().split("\n\n")

    ranges = []
    for r in lines[0].splitlines():
        a, b = map(int, r.split("-"))
        ranges.append((a, b))

    ranges.sort()
    i = 0
    # merge the ranges
    while i < len(ranges) - 1:
        r1 = ranges[i]
        r2 = ranges[i + 1]
        if r1[1] >= r2[0]:
            new_r = (r1[0], max(r1[1], r2[1]))
            ranges[i] = new_r
            del ranges[i + 1]
        else:
            i += 1

    return sum(e - s + 1 for s, e in ranges)


print(part1())
print(part2())
