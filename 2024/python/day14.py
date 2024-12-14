from numpy import quantile


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

    # print(robots)

    state = []

    W = 101
    H = 103

    for r in robots:
        px, py = r[0]
        vx, vy = r[1]

        px = (px + vx * 100) % W
        py = (py + vy * 100) % H

        state.append((px, py))

    print(state)

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

    print(quadrant_counts)
    for q in quadrant_counts:
        res *= q

    return res


def part2() -> int: ...


print(part1())
print(part2())
