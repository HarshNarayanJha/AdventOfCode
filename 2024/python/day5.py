def part1() -> int:
    rules = {}
    orders = []
    with open("../data/input5.txt") as inp:
        lines = inp.readlines()

        rules_done = False
        for line in lines:
            if not line.strip():
                rules_done = True
                continue
            if not rules_done:
                bef, after = tuple(map(int, line.strip().split("|")))
                if bef in rules:
                    rules[bef].append(after)
                else:
                    rules[bef] = list()
                    rules[bef].append(after)
            else:
                orders.append(tuple(map(int, line.strip().split(","))))

    valids = []

    for order in orders:
        correct = True

        for i, page in enumerate(order):
            if page not in rules:
                continue
            # if not all(x in rules[page] for x in order[i + 1 :]):
            #     correct = False
            #     break
            if any(x in rules[page] for x in order[:i]):
                correct = False
                break

        if correct:
            valids.append(order)

    middle_sum = 0
    for v in valids:
        middle_sum += v[len(v) // 2]

    return middle_sum


def part2() -> int:
    rules = {}
    orders = []
    with open("../data/input5.txt") as inp:
        lines = inp.readlines()

        rules_done = False
        for line in lines:
            if not line.strip():
                rules_done = True
                continue
            if not rules_done:
                bef, after = tuple(map(int, line.strip().split("|")))
                if bef in rules:
                    rules[bef].append(after)
                else:
                    rules[bef] = list()
                    rules[bef].append(after)
            else:
                orders.append(list(map(int, line.strip().split(","))))

    invalids = []
    invalid_indices = []

    for order in orders:
        correct = True

        for i, page in enumerate(order):
            if page not in rules:
                continue
            if any(x in rules[page] for x in order[:i]):
                invalid_indices.append(i)
                correct = False
                break

        if not correct:
            invalids.append(order)

    # now fix invalids (sort)

    for inv in invalids:
        for i in range(len(inv)):
            for j in range(1, len(inv)):
                if inv[j] not in rules:
                    continue
                if inv[j - 1] in rules[inv[j]]:
                    inv[j], inv[j - 1] = inv[j - 1], inv[j]

    middle_sum = 0
    for v in invalids:
        middle_sum += v[len(v) // 2]

    return middle_sum


print(part1())
print(part2())
