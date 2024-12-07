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

    maze_height = len(maze)
    maze_width = len(maze[0])

    obstacles: set[Point] = set(
        [
            Point(x, y)
            for x in range(maze_height)
            for y in range(maze_width)
            if maze[x][y] == "#"
        ]
    )

    current = start
    directions = (Point(-1, 0), Point(0, 1), Point(1, 0), Point(0, -1))
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


def part2() -> int:
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

    directions = (Point(-1, 0), Point(0, 1), Point(1, 0), Point(0, -1))
    maze_height = len(maze)
    maze_width = len(maze[0])
    loop_obs = 0

    for x, row in enumerate(maze):
        for y, c in enumerate(row):
            if c in "#^":
                continue

            maze[x][y] = "#"
            visited_locs = set()
            current = start
            direction = 0
            visited_locs.add((direction, start))

            while True:
                dx, dy = directions[direction]
                next_point = Point(current.x + dx, current.y + dy)

                if not (
                    0 <= next_point.x < maze_height and 0 <= next_point.y < maze_width
                ):
                    break

                if maze[next_point.x][next_point.y] == "#":
                    direction = (direction + 1) % 4
                else:
                    current = next_point
                    state = (direction, current)
                    if state in visited_locs:
                        loop_obs += 1
                        break
                    visited_locs.add(state)

            maze[x][y] = "."

    return loop_obs


print(part1())
# print(part2())
