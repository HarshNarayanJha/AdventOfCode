from heapq import heappush, heappop


def part1() -> int:
    maze = []
    with open("../data/input16.txt", "r") as inp:
        lines = inp.readlines()
        for line in lines:
            maze.append(list(line.strip()))

    walls = set()
    sx, sy = 0, 0
    ex, ey = 0, 0

    H = len(maze)
    W = len(maze[0])

    for i in range(H):
        for j in range(W):
            if maze[i][j] == "#":
                walls.add((i, j))
            elif maze[i][j] == "S":
                sx, sy = i, j
            elif maze[i][j] == "E":
                ex, ey = i, j

    # 0=east, 1=south, 2=west, 3=north
    seen = set()
    # cost, pos, direction, path
    pq = [(0, (sx, sy), 0)]
    best_cost = 0

    while pq:
        cost, (cx, cy), direction = heappop(pq)

        if (cx, cy) == (ex, ey):
            best_cost = cost
            break

        if (cx, cy, direction) in seen:
            continue

        seen.add((cx, cy, direction))

        dx = [0, 1, 0, -1][direction]
        dy = [1, 0, -1, 0][direction]
        nx, ny = cx + dx, cy + dy

        if (nx, ny) not in walls and 0 <= nx < H and 0 <= ny < W:
            heappush(pq, (cost + 1, (nx, ny), direction))

        new_direction = (direction - 1) % 4
        heappush(pq, (cost + 1000, (cx, cy), new_direction))

        new_direction = (direction + 1) % 4
        heappush(pq, (cost + 1000, (cx, cy), new_direction))

    return best_cost


def part2() -> int:
    maze = []
    with open("../data/input16.txt", "r") as inp:
        lines = inp.readlines()
        for line in lines:
            maze.append(list(line.strip()))

    walls = set()
    sx, sy = 0, 0
    ex, ey = 0, 0

    H = len(maze)
    W = len(maze[0])

    for i in range(H):
        for j in range(W):
            if maze[i][j] == "#":
                walls.add((i, j))
            elif maze[i][j] == "S":
                sx, sy = i, j
            elif maze[i][j] == "E":
                ex, ey = i, j

    # 0=east, 1=south, 2=west, 3=north
    scores = dict()
    tiles = set()

    # cost, pos, direction, path
    pq = [(0, (sx, sy), 0, [(sx, sy)])]
    best_cost = float("inf")

    while pq:
        cost, (cx, cy), direction, path = heappop(pq)

        if ((cx, cy), direction) in scores and scores[((cx, cy), direction)] < cost:
            continue

        if (cx, cy) == (ex, ey) and cost <= best_cost:
            best_cost = cost
            tiles |= set(path)

        scores[((cx, cy), direction)] = cost

        dx = [0, 1, 0, -1][direction]
        dy = [1, 0, -1, 0][direction]
        nx, ny = cx + dx, cy + dy

        if (nx, ny) not in walls and 0 <= nx < H and 0 <= ny < W:
            heappush(pq, (cost + 1, (nx, ny), direction, path[:] + [(nx, ny)]))

        new_direction = (direction - 1) % 4
        heappush(pq, (cost + 1000, (cx, cy), new_direction, path))

        new_direction = (direction + 1) % 4
        heappush(pq, (cost + 1000, (cx, cy), new_direction, path))

    return len(tiles)


print(part1())
print(part2())
