from collections import namedtuple


class Point(namedtuple("Point", "x y", defaults=[0, 0])):
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


UP = Point(-1, 0)
DOWN = Point(1, 0)
LEFT = Point(0, -1)
RIGHT = Point(0, 1)


def get_valid_neighbours(pt: Point, H: int, W: int) -> tuple[Point | None, ...]:
    neighbours = []
    for direction in (UP, DOWN, LEFT, RIGHT):
        new_pt = pt + direction
        neighbours.append(new_pt if 0 <= new_pt.x < H and 0 <= new_pt.y < W else None)
    return tuple(neighbours)


def part1() -> int:
    grid = None

    with open("../data/input10.txt", "r") as inp:
        grid = [list(map(int, line.strip())) for line in inp.readlines()]

    trailheads: dict[Point, int] = {
        Point(i, j): 0
        for i, row in enumerate(grid)
        for j, c in enumerate(row)
        if c == 0
    }
    tops: list[Point] = [
        Point(i, j) for i, row in enumerate(grid) for j, c in enumerate(row) if c == 9
    ]

    H = len(grid)
    W = len(grid[0])

    for trailhead in trailheads:
        tops_visited = set()

        queue: list[Point] = []
        queue.append(trailhead)
        while queue:
            pt = queue.pop()
            if pt in tops and pt not in tops_visited:
                trailheads[trailhead] += 1
                tops_visited.add(pt)
            dirs = get_valid_neighbours(pt, H, W)
            for dir in dirs:
                if not dir:
                    continue
                if grid[dir.x][dir.y] == grid[pt.x][pt.y] + 1:
                    queue.append(dir)

    score = sum(trailheads.values())

    return score


def part2() -> int:
    grid = None

    with open("../data/input10.txt", "r") as inp:
        grid = [list(map(int, line.strip())) for line in inp.readlines()]

    trailheads: dict[Point, int] = {}
    tops: list[Point] = []

    H = len(grid)
    W = len(grid[0])

    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == 0:
                trailheads[Point(i, j)] = 0
            elif c == 9:
                tops.append(Point(i, j))

    for trailhead in trailheads:
        # start the search
        queue: list[tuple[Point, list[Point]]] = []
        queue.append((trailhead, [trailhead]))

        while queue:
            pt, path = queue.pop(0)

            if pt in tops:
                trailheads[trailhead] += 1

            dirs = get_valid_neighbours(pt, H, W)

            for dir in dirs:
                if dir:
                    if grid[dir.x][dir.y] - grid[pt.x][pt.y] == 1 and dir not in path:
                        queue.append((dir, path[:] + [dir]))

    rating = sum([trailheads[t] for t in trailheads])

    return rating


print(part1())
print(part2())
