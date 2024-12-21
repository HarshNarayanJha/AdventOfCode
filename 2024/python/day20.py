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
            best_time[(ex, ey)] = pico
            break

        for dx, dy in directions:
            nx = cx + dx
            ny = cy + dy

            if 0 <= nx < H and 0 <= ny < W and (nx, ny) not in walls:
                new_time = pico + 1
                if (nx, ny) not in best_time or new_time < best_time[(nx, ny)]:
                    best_time[(nx, ny)] = new_time
                    heappush(pq, (new_time, nx, ny))

    return best_time


def part1() -> int:
    maze = None
    with open("../data/input20.txt", "r") as inp:
        maze = [list(line.strip()) for line in inp.readlines()]

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
    # cost, pos
    best_times = race((sx, sy), (ex, ey), walls, H, W)
    # best_time = best_times[(ex, ey)]

    # print("Found best time", best_time)
    # print("Finding cheats")

    ans = 0

    for pos in best_times:
        this_picos = best_times[pos]
        cx, cy = pos

        for dx in range(-2, 2 + 1):
            for dy in range(-2, 2 + 1):
                cheated_picos = abs(dx) + abs(dy)
                if cheated_picos > 2:
                    continue
                nx, ny = cx + dx, cy + dy

                if (nx, ny) not in best_times:
                    continue

                target_picos = best_times[(nx, ny)]
                if target_picos < this_picos:
                    continue

                non_cheated_picos = target_picos - this_picos
                saved = non_cheated_picos - cheated_picos

                if saved >= 100:
                    ans += 1

    return ans


def part2() -> int:
    maze = None
    with open("../data/input20.txt", "r") as inp:
        maze = [list(line.strip()) for line in inp.readlines()]

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
    # cost, pos
    best_times = race((sx, sy), (ex, ey), walls, H, W)
    # best_time = best_times[(ex, ey)]

    ans = 0

    for pos in best_times:
        this_picos = best_times[pos]
        cx, cy = pos

        for dx in range(-20, 20 + 1):
            for dy in range(-20, 20 + 1):
                cheated_picos = abs(dx) + abs(dy)
                if cheated_picos > 20:
                    continue
                nx, ny = cx + dx, cy + dy

                if (nx, ny) not in best_times:
                    continue

                target_picos = best_times[(nx, ny)]
                if target_picos < this_picos:
                    continue

                non_cheated_picos = target_picos - this_picos
                saved = non_cheated_picos - cheated_picos

                if saved >= 100:
                    ans += 1

    return ans


print(part1())
print(part2())
