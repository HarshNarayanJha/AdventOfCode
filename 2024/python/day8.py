from collections import defaultdict
from itertools import product
from math import sqrt


def get_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def get_two_antinodes(p1, p2):
    dist = get_distance(p1, p2)
    x1, y1 = p1
    x2, y2 = p2

    # Get direction vector
    dx = x2 - x1
    dy = y2 - y1

    # Normalize direction vector
    line_len = sqrt(dx * dx + dy * dy)
    dx = dx / line_len
    dy = dy / line_len

    # Scale direction vector by distance
    dx = dx * dist
    dy = dy * dist

    # Get points by extending outward in direction vector
    a1 = (round(x1 - dx), round(y1 - dy))
    a2 = (round(x2 + dx), round(y2 + dy))

    return a1, a2


def part1() -> int:
    grid = []
    with open("../data/input8.txt") as inp:
        lines = inp.readlines()
        for line in lines:
            grid.append(list(line.strip()))

    antennas = defaultdict(list)
    antinodes_at = set()

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != ".":
                antennas[grid[i][j]].append((i, j))

    antennas = dict(antennas)

    for antenna in antennas:
        points = antennas[antenna]
        for a, b in product(points, repeat=2):
            if a == b:
                continue
            a1, a2 = get_two_antinodes(a, b)
            if a1[0] >= 0 and a1[0] < len(grid) and a1[1] >= 0 and a1[1] < len(grid[0]):
                antinodes_at.add(a1)
            if a2[0] >= 0 and a2[0] < len(grid) and a2[1] >= 0 and a2[1] < len(grid[0]):
                antinodes_at.add(a2)

    return len(antinodes_at)


def node_in_bound(n, w, h):
    return n[0] >= 0 and n[0] < h and n[1] >= 0 and n[1] < w


def part2() -> int:
    ...


print(part1())
print(part2())
