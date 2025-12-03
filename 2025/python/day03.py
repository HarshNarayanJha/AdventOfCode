def part1() -> int:
    with open("./data/input3.txt", "r") as fp:
        lines = fp.read().strip().splitlines()

    tot = 0

    for k in lines:
        val = ""

        M = 2
        s, e = 0, len(k) - M
        while s < len(k) and e < len(k):
            mx = max(k[s : e + 1])
            val += mx

            s = k.index(mx, s, e + 1) + 1
            M -= 1
            e = len(k) - M

        tot += int(val)

    return tot


def part2() -> int:
    with open("./data/input3.txt", "r") as fp:
        lines = fp.read().strip().splitlines()

    tot = 0

    for k in lines:
        val = ""

        M = 12
        s, e = 0, len(k) - M
        while s < len(k) and e < len(k):
            mx = max(k[s : e + 1])
            val += mx

            s = k.index(mx, s, e + 1) + 1
            M -= 1
            e = len(k) - M

        tot += int(val)

    return tot


print(part1())
print(part2())
