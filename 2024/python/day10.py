def part1() -> int:
    grid = None

    with open("../data/input10.txt", "r") as inp:
        grid = [list(map(int, line.strip())) for line in inp.readlines()]

    H = len(grid)
    W = len(grid[0])

    trailheads: dict[tuple[int, int], int] = {
        (i, j): 0 for i in range(H) for j in range(W) if grid[i][j] == 0
    }
    tops: set[tuple[int, int]] = {
        (i, j) for i in range(H) for j in range(W) if grid[i][j] == 9
    }

    directions = {(0, 1), (1, 0), (0, -1), (-1, 0)}

    for trailhead in trailheads:
        tops_visited = set()

        stack: list[tuple[int, int]] = [trailhead]
        while stack:
            pt = stack.pop()
            x, y = pt
            if pt in tops and pt not in tops_visited:
                trailheads[trailhead] += 1
                tops_visited.add(pt)

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if (
                    0 <= new_x < H
                    and 0 <= new_y < W
                    and grid[new_x][new_y] == grid[x][y] + 1
                ):
                    stack.append((new_x, new_y))

    score = sum(trailheads.values())

    return score


def part2() -> int:
    grid = None

    with open("../data/input10.txt", "r") as inp:
        grid = [list(map(int, line.strip())) for line in inp.readlines()]

    H = len(grid)
    W = len(grid[0])

    trailheads: dict[tuple[int, int], int] = {
        (i, j): 0 for i in range(H) for j in range(W) if grid[i][j] == 0
    }
    tops: set[tuple[int, int]] = {
        (i, j) for i in range(H) for j in range(W) if grid[i][j] == 9
    }

    directions = {(0, 1), (1, 0), (0, -1), (-1, 0)}

    for trailhead in trailheads:
        stack: list[tuple[int, int]] = [trailhead]
        while stack:
            pt = stack.pop()
            x, y = pt
            if pt in tops:
                trailheads[trailhead] += 1

            for dx, dy in directions:
                new_x, new_y = (x + dx, y + dy)
                if (
                    0 <= new_x < H
                    and 0 <= new_y < W
                    and grid[new_x][new_y] == grid[x][y] + 1
                ):
                    stack.append((new_x, new_y))

    rating = sum(trailheads.values())

    return rating


print(part1())
print(part2())
