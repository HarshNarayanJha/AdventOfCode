

import math


class Grid:
    def __init__(self, paths: "list[Path]"):
        self.paths = paths
        self.sands: "list[Sand]" = []
        self.rocks = {}
        self.leftmost_x = 0
        self.rightmost_x = 0
        self.baseline_y = -1
        self.floor = self.baseline_y + 2 # Part two adds an infinitrly long floor at highest y + 2
        self.build_points()

    def build_points(self):
        for p in self.paths:
            for l in p.lines:
                for p in l.all_points:
                    self.rocks[(p.x, p.y)] = p
                    if self.leftmost_x > p.x:
                        self.leftmost_x = p.x
                    if self.rightmost_x < p.x:
                        self.rightmost_x = p.x
                    if self.baseline_y < p.y:
                        self.baseline_y = p.y
        self.floor = self.baseline_y + 2
        self.rightmost_x += 100 # Safe margin

    def construct(self):
        ...

    def add_sand(self, sand: "Sand"):
        result = sand.try_move_down()
        if result:
            self.sands.append(sand)
        return result

    def get_point(self, x: int, y: int) -> str:
        # for p in self.all_points:
        #     if (p.x == x and p.y == y):
        #         return "#"
        if (x, y) in self.rocks:
            return "#"
        for s in self.sands:
            if s.x == x and s.y == y:
                return "O"

        return "."

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"{self.x},{self.y}"

class Line:
    def __init__(self, point_from: Point, point_to: Point):
        self.point_from = point_from
        self.point_to = point_to
        self.all_points = []
        self.generate_all_points()
    
    def generate_all_points(self) -> "list[Point]":
        if self.point_from.x == self.point_to.x:
            if self.point_from.y < self.point_to.y:
                ys = range(self.point_from.y, self.point_to.y + 1, 1)
            else:
                ys = range(self.point_from.y, self.point_to.y - 1, -1)

            for y in ys:
                self.all_points.append(Point(self.point_from.x, y))

        elif self.point_from.y == self.point_to.y:
            if self.point_from.x < self.point_to.x:
                xs = range(self.point_from.x, self.point_to.x + 1, 1)
            else:
                xs = range(self.point_from.x, self.point_to.x - 1, -1)

            for x in xs:
                self.all_points.append(Point(x, self.point_from.y))

    def __repr__(self) -> str:
        return f"{self.point_from} -> {self.point_to}"

class Path:
    def __init__(self, lines: "list[Line]"):
        self.lines = lines

    def __repr__(self) -> str:
        return f"{[l for l in self.lines]}"

class Sand:
    def __init__(self, grid, start_x, start_y):
        self.grid: "Grid" = grid
        self.start_x = start_x
        self.start_y = start_y
        self.x = self.start_x
        self.y = self.start_y

    def __repr__(self) -> str:
        return f"Sand {self.start_x},{self.start_y} -> {self.x},{self.y}"
    
    def try_move_down(self):
        dest = (self.x, self.y + 1)
        # if dest[1] > self.grid.baseline_y:
            # The particle has died into the endless void
            # return False
        if dest[1] == self.grid.floor:
            print("Reached Floor")
            return True

        point = self.grid.get_point(dest[0], dest[1])
        # Point is empty, move there
        if point == ".":
            self.x = dest[0]
            self.y = dest[1]
            return self.try_move_down()
        # It's blocked (either rock or another sand)
        elif point == "#" or point == "O":
            return self.try_move_down_left()

    def try_move_down_left(self):
        dest = (self.x - 1, self.y + 1)
        point = self.grid.get_point(dest[0], dest[1])
        # Point is empty, move there
        if point == ".":
            self.x = dest[0]
            self.y = dest[1]
            return self.try_move_down()
        # It's blocked (either rock or another sand)
        elif point == "#" or point == "O":
            return self.try_move_down_right()

    def try_move_down_right(self):
        dest = (self.x + 1, self.y + 1)
        point = self.grid.get_point(dest[0], dest[1])
        # Point is empty, move there
        if point == ".":
            self.x = dest[0]
            self.y = dest[1]
            return self.try_move_down()
        # It's blocked (either rock or another sand)
        else:
            # Now come to rest!
            return True


# Read the scans
with open("./2022/rock_scan.txt", "r") as f:
    _paths = f.readlines()

paths = []

for p in _paths:
    points = p.split(" -> ")
    lines = []
    for p1, p2 in zip(points, points[1:]):
        x1, y1 = p1.split(",")
        x2, y2 = p2.split(",")
        line = Line(Point(int(x1), int(y1)), Point(int(x2), int(y2)))
        lines.append(line)

    path = Path(lines)
    paths.append(path)

# for i in paths: print(i)
# run = True
# grid = Grid(paths)
# while run:
#     if grid.get_point(500, 0) != ".":
#         # Sand pore is blocked out
#         break
#     sand = Sand(grid, 500, 0)
#     run = grid.add_sand(sand)

# for s in grid.sands:
#     print(s)

# print(len(grid.sands))

# Part 2, with the floor
print("\n\nPart2\n")
new_paths = paths #+ [Path([Line(Point(grid.leftmost_x - 1000, grid.floor), Point(grid.rightmost_x + 1000, grid.floor))])]
new_grid = Grid(new_paths) ## This new_grid.floor is unconsistent/not interactable at all

run2 = True
while run2:
    if new_grid.get_point(500, 0) == "O":
        # Sand pore is blocked out
        break
    sand = Sand(new_grid, 500, 0)
    run2 = new_grid.add_sand(sand)
    print(sand)

print(len(new_grid.sands))