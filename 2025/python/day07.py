from collections import deque
from pprint import pprint


def part1() -> int:
    with open("../data/input07.txt", "r") as fp:
        lines = fp.read().strip().splitlines()

    grid = [[c for c in line] for line in lines]
    H = len(grid)
    W = len(grid[0])

    S = (-1, -1)
    # pprint(grid)

    for i in range(H):
        for j in range(W):
            if grid[i][j] == "S":
                S = (i, j)
                break

    beams = deque()
    beams.append(S)

    splits = 0

    while beams:
        i, j = beams.popleft()
        ni, nj = i + 1, j

        if ni < 0 or ni >= H or nj < 0 or nj >= W:
            continue

        if grid[ni][nj] == ".":
            beams.append((ni, nj))
            grid[ni][nj] = "|"
            continue

        if grid[ni][nj] == "^":
            nia, nja = ni, nj - 1
            nib, njb = ni, nj + 1
            beams.append((nia, nja))
            beams.append((nib, njb))
            splits += 1

    # pprint(grid)
    return splits


def part2() -> int:
    with open("../data/input07.txt", "r") as fp:
        lines = fp.read().strip().splitlines()

    grid = [[c for c in line] for line in lines]
    H = len(grid)
    W = len(grid[0])

    S = (-1, -1)
    # pprint(grid)

    for i in range(H):
        for j in range(W):
            if grid[i][j] == "S":
                S = (i, j)
                break

    ways = [[0] * W for _ in range(H)]
    ways[S[0]][S[1]] = 1

    for i in range(S[0], H - 1):
        for j in range(W):
            cnt = ways[i][j]
            if cnt == 0:
                continue

            ni, nj = i + 1, j

            if ni < 0 or ni >= H or nj < 0 or nj >= W:
                continue

            if grid[ni][nj] == ".":
                ways[ni][nj] += cnt
            elif grid[ni][nj] == "^":
                if nj - 1 >= 0:
                    ways[ni][nj - 1] += cnt
                if nj + 1 < W:
                    ways[ni][nj + 1] += cnt

    # pprint(grid)
    return sum(ways[H - 1][j] for j in range(W))


print(part1())
print(part2())
