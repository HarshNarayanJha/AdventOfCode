from pprint import pprint
from heapq import heappush, heappop

def part1() -> int:
    bcoords = list()
    with open("../data/input18.txt", "r") as inp:
        for line in inp.readlines():
            bcoords.append(tuple(map(int, line.strip().split(","))))

    GRID_SIZE = 7
    to_sim = 12

    grid = []
    for i in range(GRID_SIZE):
        row = []
        for j in range(GRID_SIZE):
            if (j, i) in bcoords[:to_sim]:
                row.append("#")
            else:
                row.append(".")
        grid.append(row)

    sx, sy = 0, 0
    ex, ey = GRID_SIZE - 1, GRID_SIZE - 1

    seen = set()
    # steps, pos, direction
    pq = [(0, (sx, sy), 0)]
    least_steps = 0

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

        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and grid[nx][ny] != '#':
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

    while to_sim <= len(bcoords):

        grid = []
        for i in range(GRID_SIZE):
            row = []
            for j in range(GRID_SIZE):
                if (j, i) in bcoords[:to_sim]:
                    row.append("#")
                else:
                    row.append(".")
            grid.append(row)

        sx, sy = 0, 0
        ex, ey = GRID_SIZE - 1, GRID_SIZE - 1

        seen = set()
        # steps, pos, direction
        pq = [(0, (sx, sy), 0)]
        least_steps = 0

        while pq:
            cost, (cx, cy), direction  = heappop(pq)

            if (cx, cy) == (ex, ey):
                least_steps = cost
                break

            if (cx, cy, direction) in seen:
                continue

            seen.add((cx, cy, direction))

            dx = [0, 1, 0, -1][direction]
            dy = [1, 0, -1, 0][direction]
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and grid[nx][ny] != '#':
                heappush(pq, (cost + 1, (nx, ny), direction))

            new_direction = (direction - 1) % 4
            heappush(pq, (cost, (cx, cy), new_direction))

            new_direction = (direction + 1) % 4
            heappush(pq, (cost, (cx, cy), new_direction))

        print(to_sim, least_steps)
        to_sim += 1

        if least_steps == 0:
            print(bcoords[to_sim-2][::-1])
            return 0

    return 0


print(part1())
print(part2())
