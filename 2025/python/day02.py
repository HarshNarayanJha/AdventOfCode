def part1() -> int:
    with open("../data/input02.txt", "r") as fp:
        line = fp.read().strip()

    ranges = line.split(",")
    values = []
    for r in ranges:
        a, b = r.split("-")
        values.append(range(int(a), int(b) + 1))

    res = 0
    for k in values:
        for v in k:
            s = str(v)
            if len(s) % 2 != 0:
                continue

            i, j = 0, len(s) // 2
            while i < len(s) // 2 and j < len(s):
                if s[i] != s[j]:
                    break
                i += 1
                j += 1
            else:
                res += v

    return res


def part2() -> int:
    with open("../data/input02.txt", "r") as fp:
        line = fp.read().strip()

    ranges = line.split(",")
    values = []
    for r in ranges:
        a, b = r.split("-")
        values.append(range(int(a), int(b) + 1))

    res = 0
    for k in values:
        for v in k:
            s = str(v)

            i, j = 0, 1
            while j < len(s):
                ss = s[i:j]
                if ss * (len(s) // j) == s:
                    res += v
                    break
                j += 1

    return res


print(part1())
print(part2())
