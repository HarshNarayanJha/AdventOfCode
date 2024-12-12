def part1() -> int:
    grid = None
    with open("../data/input12.txt", "r") as inp:
        grid = [list(list(line.strip())) for line in inp.readlines()]

    H = len(grid)
    W = len(grid[0])

    cost = 0

    regions = {}
    visited = set()
    component_id = 0

    def dfs(i, j, label):
        stack = [(i, j)]
        component = []

        while stack:
            ci, cj = stack.pop()
            if (ci, cj) in visited:
                continue

            visited.add((ci, cj))
            component.append((ci, cj))

            for ni, nj in [
                (ci - 1, cj),
                (ci + 1, cj),
                (ci, cj - 1),
                (ci, cj + 1),
            ]:
                if 0 <= ni < H and 0 <= nj < W:
                    if grid[ni][nj] == label and (ni, nj) not in visited:
                        stack.append((ni, nj))

        return component

    for i in range(H):
        for j in range(W):
            if (i, j) not in visited:
                label = grid[i][j]
                component = dfs(i, j, label)
                key = (label, component_id)
                regions[key] = component
                component_id += 1

    for r in regions:
        span = regions[r]
        area = len(span)
        perimeter = 0

        for i, j in span:
            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for ni, nj in neighbors:
                if (ni, nj) not in span:
                    perimeter += 1

        cost += area * perimeter

    return cost


def part2() -> int: ...


print(part1())
print(part2())
