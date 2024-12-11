def part1() -> int:
    line = None
    with open("../data/input11.txt", "r") as inp:
        line = list(map(int, inp.read().strip().split()))

    blinks = 25

    counts = dict.fromkeys(line, 0)
    for v in line:
        counts[v] += 1

    for _ in range(blinks):
        new_counts = {}

        new_counts[1] = counts.get(0, 0)

        for num, count in counts.items():
            if num != 0:
                s = str(num)
                if len(s) % 2 == 1:
                    new_counts[2024 * num] = new_counts.get(2024 * num, 0) + count
                else:
                    mid = len(s) // 2
                    left, right = int(s[:mid]), int(s[mid:])
                    new_counts[left] = new_counts.get(left, 0) + count
                    new_counts[right] = new_counts.get(right, 0) + count

            counts = new_counts

    return sum(counts.values())


def part2() -> int:
    line = None
    with open("../data/input11.txt", "r") as inp:
        line = list(map(int, inp.read().strip().split()))

    blinks = 75

    counts = dict.fromkeys(line, 0)
    for v in line:
        counts[v] += 1

    for _ in range(blinks):
        new_counts = {}

        new_counts[1] = counts.get(0, 0)

        for num, count in counts.items():
            if num != 0:
                s = str(num)
                if len(s) % 2 == 1:
                    new_counts[2024 * num] = new_counts.get(2024 * num, 0) + count
                else:
                    mid = len(s) // 2
                    left, right = int(s[:mid]), int(s[mid:])
                    new_counts[left] = new_counts.get(left, 0) + count
                    new_counts[right] = new_counts.get(right, 0) + count

            counts = new_counts

    return sum(counts.values())


print(part1())
print(part2())
