def parse_input(lines: list[str]) -> tuple[dict[int, tuple[int]], list[list[int]]]:
    rules = {}
    orders = []

    rules_done = False
    for line in lines:
        if not line.strip():
            rules_done = True
            continue
        if not rules_done:
            bef, after = tuple(map(int, line.strip().split("|")))
            rules.setdefault(bef, [])
            rules[bef].append(after)
        else:
            orders.append(list(map(int, line.strip().split(","))))

    return rules, orders


def part1() -> int:
    rules = {}
    orders = []
    with open("../data/input5.txt") as inp:
        rules, orders = parse_input(inp.readlines())

    valids = []
    for order in orders:
        correct = True

        for i, page in enumerate(order):
            if page not in rules:
                continue
            if any(x in rules[page] for x in order[:i]):
                correct = False
                break

        if correct:
            valids.append(order)

    return sum([v[len(v) // 2] for v in valids])


def part2() -> int:
    rules = {}
    orders = []
    with open("../data/input5.txt") as inp:
        rules, orders = parse_input(inp.readlines())

    invalids = []
    for order in orders:
        correct = True

        for i, page in enumerate(order):
            if page not in rules:
                continue
            if any(x in rules[page] for x in order[:i]):
                correct = False
                break

        if not correct:
            invalids.append(order)

    for inv in invalids:
        for i in range(len(inv)):
            for j in range(1, len(inv)):
                if inv[j] not in rules:
                    continue
                if inv[j - 1] in rules[inv[j]]:
                    inv[j], inv[j - 1] = inv[j - 1], inv[j]

    return sum([v[len(v) // 2] for v in invalids])


print(part1())
print(part2())
