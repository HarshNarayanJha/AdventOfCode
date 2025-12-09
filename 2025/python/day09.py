import math


def part1() -> int:
    with open("../data/input09.txt", "r") as fp:
        lines = fp.read().strip().splitlines()

    coords = [tuple(map(int, line.split(","))) for line in lines]
    # print(coords)

    maxArea = 0

    for i in range(len(coords)):
        for j in range(i, len(coords)):
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            # print((x1, y1), (x2, y2), area)
            maxArea = max(maxArea, area)

    return maxArea


cache = {}


def check_if_inside_the_shape(R, P):
    if P in cache:
        return cache[P]

    s = 0.0
    n = len(R)

    px, py = P

    for i in range(len(R)):
        x1, y1 = R[i]
        x2, y2 = R[(i + 1) % n]

        v1x, v1y = x1 - px, y1 - py
        v2x, v2y = x2 - px, y2 - py

        a1 = math.atan2(v1y, v1x)
        a2 = math.atan2(v2y, v2x)

        da = a2 - a1

        if da <= -math.pi:
            da += 2 * math.pi
        elif da > math.pi:
            da -= 2 * math.pi

        s += da

    cache[P] = abs(abs(s) - 2 * math.pi) < 1e-6

    return cache[P]


def part2() -> int:
    with open("../data/input09.txt", "r") as fp:
        lines = fp.read().strip().splitlines()

    coords = [tuple(map(int, line.split(","))) for line in lines]
    # print(coords)
    greens = set()

    for i in range(len(coords)):
        c1, c2 = coords[i], coords[(i + 1) % len(coords)]
        c1x, c1y = c1
        c2x, c2y = c2
        if c1x == c2x:
            for y in range(min(c1y, c2y), max(c1y, c2y) + 1):
                greens.add((c1x, y))
        elif c1y == c2y:
            for x in range(min(c1x, c2x), max(c1x, c2x) + 1):
                greens.add((x, c1y))

    maxArea = 0
    maxCoor = None

    total = set(coords) | greens

    for i in range(len(coords)):
        print(i / len(coords) * 100)
        for j in range(i + 1, len(coords)):
            x1, y1 = coords[i]
            x2, y2 = coords[j]

            x3, y3 = (x1, y2)
            x4, y4 = (x2, y1)

            if len(set([(x1, y1), (x2, y2), (x3, y3), (x4, y4)])) != 4:
                continue

            # check all linear points, it must cross with a gap somewhere

            if not all(
                check_if_inside_the_shape(coords, (x1, _y)) and check_if_inside_the_shape(coords, (x2, _y))
                for _y in range(min(y1, y2) + 1, max(y1, y2), 1000)
            ):
                continue

            # if not all(
            #     check_if_inside_the_shape(coords, (_x, y1)) and check_if_inside_the_shape(coords, (_x, y2))
            #     for _x in range(min(x1, x2) + 1, max(x1, x2), 10000)
            # ):
            #     continue

            A = (x1, y1)
            B = (x2, y2)
            C = (x3, y3)
            D = (x4, y4)

            if C in total and D in total:
                area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
                # print((x1, y1), (x2, y2), area)
                maxArea = max(maxArea, area)
                continue

            # print(A, B, C, D)

            C_in = check_if_inside_the_shape(coords, C)
            D_in = check_if_inside_the_shape(coords, D)

            if (C_in and D_in) or (C in total and D_in) or (C_in and D in total):
                area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
                # print((x1, y1), (x2, y2), area)
                if area > maxArea:
                    maxArea = area
                    maxCoor = (x1, y1), (x2, y2), (x3, y3), (x4, y4)
                # print(area, maxArea)

    print(maxCoor)
    return maxArea


print(part1())
print(part2())
