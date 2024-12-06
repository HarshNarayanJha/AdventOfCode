from collections import namedtuple


def part1() -> int:
    maze = []
    Point = namedtuple("Point", "x y")
    start = Point(0, 0)
    line_count = 0

    with open("../data/input6.txt") as inp:
        for line in inp.readlines():
            line_count += 1
            maze.append(list(line.strip()))
            if "^" in line:
                start = Point(line_count - 1, line.index("^"))

    visited_locs: set[Point] = set()
    visited_locs.add(start)

    obstacles: set[Point] = set()

    for x, row in enumerate(maze):
        for y, c in enumerate(row):
            if c == "#":
                obstacles.add(Point(x, y))

    current = start
    directions = [Point(-1, 0), Point(0, 1), Point(1, 0), Point(0, -1)]
    direction = 0

    while True:
        if current.x >= len(maze) or current.x < 0:
            break

        if current.y >= len(maze[0]) or current.y < 0:
            break

        next_point = Point(
            current.x + directions[direction].x, current.y + directions[direction].y
        )

        if next_point in obstacles:
            # rotate 90deg right
            direction = (direction + 1) % 4
        else:
            # move forward
            current = next_point
            visited_locs.add(current)

    visited_locs.pop()
    return len(visited_locs)


def part2() -> int: ...


print(part1())
print(part2())
