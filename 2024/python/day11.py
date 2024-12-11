from functools import cache


@cache
def process_number(num: int) -> tuple[int, ...]:
    if num == 0:
        return (1,)
    s = str(num)
    if len(s) % 2 == 1:
        return (2024 * num,)
    mid = len(s) // 2
    left, right = int(s[:mid]), int(s[mid:])
    return (left, right)


@cache
def simulate(line: tuple[int], blinks: int) -> int:
    counts = dict.fromkeys(line, 0)
    for v in line:
        counts[v] += 1

    for _ in range(blinks):
        new_counts = {}
        for num, count in counts.items():
            for new_num in process_number(num):
                new_counts[new_num] = new_counts.get(new_num, 0) + count
        counts = new_counts

    return sum(counts.values())


def part1() -> int:
    with open("../data/input11.txt", "r") as inp:
        line = tuple(map(int, inp.read().strip().split()))

    return simulate(line, 25)


def part2() -> int:
    with open("../data/input11.txt", "r") as inp:
        line = tuple(map(int, inp.read().strip().split()))

    return simulate(line, 75)


print(part1())
print(part2())
