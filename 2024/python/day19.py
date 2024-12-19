def part1() -> int:
    available = []
    to_make = []
    with open("../data/input19.txt") as inp:
        lines = iter(inp.readlines())

        available = next(lines).strip().split(", ")
        next(lines)

        for line in lines:
            to_make.append(line.strip())

    count = 0

    DP = {}

    def ways(words, target):
        if target in DP:
            return DP[target]

        ans = 0 if target else 1

        for word in words:
            if target.startswith(word):
                ans += ways(words, target[len(word) :])

        DP[target] = ans
        return ans

    for make in to_make:
        count += 1 if ways(available, make) > 0 else 0

    return count


def part2() -> int:
    available = []
    to_make = []
    with open("../data/input19.txt") as inp:
        lines = iter(inp.readlines())

        available = next(lines).strip().split(", ")
        next(lines)

        for line in lines:
            to_make.append(line.strip())

    count = 0

    DP = {}

    def ways(words, target):
        if target in DP:
            return DP[target]

        ans = 0 if target else 1

        for word in words:
            if target.startswith(word):
                ans += ways(words, target[len(word) :])
        DP[target] = ans
        return ans

    for make in to_make:
        count += ways(available, make)

    return count


print(part1())
print(part2())
