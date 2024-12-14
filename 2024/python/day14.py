def part1() -> int:
    robots = []

    with open("../data/input14.txt", "r") as inp:
        for line in inp.readlines():
            robo = []
            p, v = line.split()
            px, py = p.split("=")[1].split(",")
            robo.append((int(px), int(py)))

            vx, vy = v.split("=")[1].split(",")
            robo.append((int(vx), int(vy)))

            robots.append(tuple(robo))

    state = []

    W = 101
    H = 103

    for r in robots:
        px, py = r[0]
        vx, vy = r[1]

        px = (px + vx * 100) % W
        py = (py + vy * 100) % H

        state.append((px, py))

    quadrant_counts = []

    count = 0
    for i in range(0, W // 2):
        for j in range(0, H // 2):
            count += state.count((i, j))
    quadrant_counts.append(count)

    count = 0
    for i in range(W // 2 + 1, W):
        for j in range(0, H // 2):
            count += state.count((i, j))
    quadrant_counts.append(count)

    count = 0
    for i in range(0, W // 2):
        for j in range(H // 2 + 1, H):
            count += state.count((i, j))
    quadrant_counts.append(count)

    count = 0
    for i in range(W // 2 + 1, W):
        for j in range(H // 2 + 1, H):
            count += state.count((i, j))
    quadrant_counts.append(count)

    res = 1

    for q in quadrant_counts:
        res *= q

    return res


def part2() -> int:
    robots = []

    with open("../data/input14.txt", "r") as inp:
        for line in inp.readlines():
            robo = []
            p, v = line.split()
            px, py = p.split("=")[1].split(",")
            robo.append((int(px), int(py)))

            vx, vy = v.split("=")[1].split(",")
            robo.append((int(vx), int(vy)))

            robots.append(tuple(robo))

    W = 101
    H = 103

    state = {i: r[0] for i, r in enumerate(robots)}

    # with open("state.txt", "w") as fp:
    #     pass

    order_at = 0

    for s in range(7890, 7900):
        for i, r in enumerate(robots):
            px, py = r[0]
            vx, vy = r[1]

            px = (px + vx * s) % W
            py = (py + vy * s) % H

            state[i] = (px, py)

        grid = [
            [list(state.values()).count((i, j)) for i in range(W)] for j in range(H)
        ]

        visited = set()
        for i in range(H):
            for j in range(W):
                if grid[i][j] == 0:
                    continue

                if (i, j) in visited:
                    continue

                stack = [(i, j)]

                locations = set()
                while stack:
                    x, y = stack.pop()
                    locations.add((x, y))
                    visited.add((x, y))
                    dirs = ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
                    for nx, ny in dirs:
                        if nx < 0 or nx >= H or ny < 0 or ny >= W:
                            continue
                        if grid[nx][ny] == 0:
                            continue
                        if (nx, ny) in visited:
                            continue

                        stack.append((nx, ny))

                if len(locations) >= 50:
                    order_at = s

        # with open("state.txt", "a") as fp:
        #     fp.write(str(s))
        #     fp.write("\n")
        #     for row in grid:
        #         fp.write(" ".join('.' if x == 0 else str(x) for x in row))
        #         fp.write("\n")
        #     fp.write("\n\n")

    # so there are multiple ways to solve this one
    # one includes detecting large amounts of area covered by robots (using flood fill) and that is probably the tree
    # but it takes a lot of iterations
    # I found mine at 7892
    #
    # another approach is to find bands of robots repeating the frames, which will repeat at intervals of 101 and 103
    # and where they both form, it forms a beautiful christmas tree.
    # For me the bands form at 14, 64, 115, 167, see exactly a 101 and 103 intervals
    # where both forms, is the tree
    #
    # 64 + 103n = 14 + 101m
    # the values of m and n are the solution
    #
    # and the frame/second is the answer.
    #
    # This can be solved by the CRT (Chinese Reminder Theorem) (it seems complex right now, not for long)
    # It gives the solution of 7892
    #
    # so....
    return order_at


print(part1())
print(part2())
