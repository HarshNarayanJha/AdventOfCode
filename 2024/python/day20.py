from collections import defaultdict
from heapq import heappop, heappush


def race(s, e, walls, H, W):
    sx, sy = s
    ex, ey = e

    pq = [(0, sx, sy)]
    best_time = {(sx, sy): 0}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while pq:
        pico, cx, cy = heappop(pq)

        if (cx, cy) == (ex, ey):
            return pico

        for dx, dy in directions:
            nx = cx + dx
            ny = cy + dy

            if 0 <= nx < H and 0 <= ny < W and (nx, ny) not in walls:
                new_time = pico + 1
                if (nx, ny) not in best_time or new_time < best_time[(nx, ny)]:
                    best_time[(nx, ny)] = new_time
                    heappush(pq, (new_time, nx, ny))

    return best_time[(sx, sy)]


def part1() -> int:
    maze = []
    with open("../data/input20.txt", "r") as inp:
        lines = inp.readlines()
        for line in lines:
            maze.append(list(line.strip()))

    walls = set()
    sx, sy = 0, 0
    ex, ey = 0, 0

    H = len(maze)
    W = len(maze[0])

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(H):
        for j in range(W):
            if maze[i][j] == "#":
                walls.add((i, j))
            elif maze[i][j] == "S":
                sx, sy = i, j
            elif maze[i][j] == "E":
                ex, ey = i, j
    # cost, pos
    best_time = race((sx, sy), (ex, ey), walls, H, W)

    print("Found best time", best_time)
    print("Finding cheats")

    cheats = defaultdict(int)

    removed = set()

    for i in range(H):
        print("Row", i)
        for j in range(W):
            if (i, j) in walls:
                continue
            for dx, dy in directions:
                nx, ny = i + dx, j + dy

                if (nx, ny) not in walls or (nx, ny) in removed:
                    continue

                nx2, ny2 = nx + dx, ny + dy

                if (nx2, ny2) not in walls and 0 <= nx2 < H and 0 <= ny2 < W:
                    # okay so this wall is removable
                    # remove it
                    walls.remove((nx, ny))
                    removed.add((nx, ny))

                    picos = race((sx, sy), (ex, ey), walls, H, W)
                    if best_time - picos > 0:
                        cheats[best_time - picos] += 1

                    walls.add((nx, ny))

    print(cheats)
    res = 0
    for c in cheats:
        if c >= 100:
            res += cheats[c]
    return res


def part2() -> int: ...


print(part1())
print(part2())
