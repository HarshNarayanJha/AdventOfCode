def part1() -> int:
    grid = []
    with open("../data/input4.txt") as inp:
        for line in inp.readlines():
            grid.append(list(line.strip()))

    count = 0

    valid_coords = set((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            directions = [
                (i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0)
            ]
            for dx, dy in directions:
                if (x + dx * 3, y + dy * 3) not in valid_coords:
                    continue

                if [grid[x + dx * n][y + dy * n] for n in range(4)] == list("XMAS"):
                    count += 1

    return count


def part2() -> int: ...


print(part1())
print(part2())
