from heapq import heappush, heappop


def part1() -> int:
    bcoords = list()
    with open("../data/input18.txt", "r") as inp:
        for line in inp.readlines():
            bcoords.append(tuple(map(int, line.strip().split(","))))

    GRID_SIZE = 71
    to_sim = 1024

    sx, sy = 0, 0
    ex, ey = GRID_SIZE - 1, GRID_SIZE - 1

    seen = set()
    pq = [(0, (sx, sy), 0)]
    least_steps = 0

    blocks = set(bcoords[:to_sim])

    while pq:
        cost, (cx, cy), direction = heappop(pq)

        if (cx, cy) == (ex, ey):
            least_steps = cost
            break

        if (cx, cy, direction) in seen:
            continue

        seen.add((cx, cy, direction))

        dx = [0, 1, 0, -1][direction]
        dy = [1, 0, -1, 0][direction]
        nx, ny = cx + dx, cy + dy

        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and (ny, nx) not in blocks:
            heappush(pq, (cost + 1, (nx, ny), direction))

        new_direction = (direction - 1) % 4
        heappush(pq, (cost, (cx, cy), new_direction))

        new_direction = (direction + 1) % 4
        heappush(pq, (cost, (cx, cy), new_direction))

    return least_steps


def part2() -> int:
    bcoords = list()
    with open("../data/input18.txt", "r") as inp:
        for line in inp.readlines():
            bcoords.append(tuple(map(int, line.strip().split(","))))

    GRID_SIZE = 71
    to_sim = 1024

    pi = to_sim
    qj = len(bcoords) - 1

    while pi < qj:
        m = pi + (qj - pi) // 2

        sx, sy = 0, 0
        ex, ey = GRID_SIZE - 1, GRID_SIZE - 1

        seen = set()
        pq = [(0, (sx, sy), 0)]
        least_steps = 0

        blocked = set(bcoords[:m])

        while pq:
            cost, (cx, cy), direction = heappop(pq)

            if (cx, cy) == (ex, ey):
                least_steps = cost
                break

            if (cx, cy, direction) in seen:
                continue

            seen.add((cx, cy, direction))

            dx = [0, 1, 0, -1][direction]
            dy = [1, 0, -1, 0][direction]
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and (ny, nx) not in blocked:
                heappush(pq, (cost + 1, (nx, ny), direction))

            new_direction = (direction - 1) % 4
            heappush(pq, (cost, (cx, cy), new_direction))

            new_direction = (direction + 1) % 4
            heappush(pq, (cost, (cx, cy), new_direction))

        if least_steps == 0:
            qj = m - 1
        else:
            pi = m + 1

    assert pi == qj

    print(pi, bcoords[pi - 1])
    return 0


print(part1())
print(part2())
