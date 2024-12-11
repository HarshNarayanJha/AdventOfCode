def part1() -> int:
    line = None
    with open("../data/input11.txt", "r") as inp:
        line = list(map(int, inp.read().strip().split()))

    blinks = 25

    for _ in range(blinks):
        print(_)
        new_line = []
        for num in line:
            if num == 0:
                new_line.append(1)
            elif len(str(num)) % 2 == 0:
                st = str(num)
                mid = len(st) // 2
                left, right = st[:mid], st[mid:]
                new_line.extend([int(left), int(right)])
            else:
                new_line.append(2024 * num)

        line = new_line

    return len(line)

    return 0


def part2() -> int:
    ...


print(part1())
print(part2())
