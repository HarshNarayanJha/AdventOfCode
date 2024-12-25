def part1() -> int:
    locks = []
    keys = []
    with open("../data/input25.txt", "r") as inp:
        for g in inp.read().split("\n\n"):
            g = g.strip()
            # print(g)
            # print()
            if g.startswith("#" * 5) and g.endswith("." * 5):
                locks.append([list(line) for line in g.splitlines()])
            elif g.startswith("." * 5) and g.endswith("#" * 5):
                keys.append([list(line) for line in g.splitlines()])

    num_locks = []
    for lock in locks:
        heights = []
        for k in range(len(lock[0])):
            height = 0
            for r in lock:
                if r[k] == "#":
                    height += 1
            heights.append(height - 1)
        num_locks.append(heights)

    num_keys = []
    for key in keys:
        heights = []
        for k in range(len(key[0])):
            height = 0
            for r in key:
                if r[k] == "#":
                    height += 1
            heights.append(height - 1)
        num_keys.append(heights)

    print(num_locks)
    print(num_keys)

    keys_worked = 0

    for lock in num_locks:
        for key in num_keys:
            if all([a + b <= 5 for a, b in zip(lock, key)]):
                keys_worked += 1
    # print(locks)
    # print(keys)

    return keys_worked


def part2() -> int: ...


print(part1())
print(part2())
