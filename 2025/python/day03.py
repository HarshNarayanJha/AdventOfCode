def part1() -> int:
    with open("./data/input3.txt", "r") as fp:
        lines = fp.read().strip().splitlines()

    tot = 0

    for k in lines:
        mx = -1
        for i in range(len(k)):
            for j in range(i + 1, len(k)):
                num = int(k[i] + k[j])
                mx = max(mx, num)

        tot += mx

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
