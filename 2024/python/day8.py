from collections import defaultdict
from itertools import product


def get_two_antinodes(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    a1 = (round(x1 - dx), round(y1 - dy))
    a2 = (round(x2 + dx), round(y2 + dy))
    return a1, a2


def node_in_bound(n, w, h):
    return n[0] >= 0 and n[0] < h and n[1] >= 0 and n[1] < w


def part1() -> int:
    grid = None
    with open("../data/input8.txt") as inp:
        grid = [list(line.strip()) for line in inp.readlines()]

    W = len(grid)
    H = len(grid[0])

    antennas = defaultdict(list)
    for i in range(H):
        for j in range(W):
            if grid[i][j] != ".":
                antennas[grid[i][j]].append((i, j))
    antennas = dict(antennas)

    visited_pairs = set()
    antinodes_at = set()
    for antenna in antennas:
        pairs = product(antennas[antenna], repeat=2)
        for a, b in pairs:
            if a == b:
                continue
            if (a, b) in visited_pairs or (b, a) in visited_pairs:
                continue
            visited_pairs.add((a, b))

            a1, a2 = get_two_antinodes(a, b)
            if node_in_bound(a1, len(grid), len(grid[0])):
                antinodes_at.add(a1)
            if node_in_bound(a2, len(grid), len(grid[0])):
                antinodes_at.add(a2)

    return len(antinodes_at)


def part2() -> int:
    grid = None
    with open("../data/input8.txt") as inp:
        grid = [list(line.strip()) for line in inp.readlines()]

    W = len(grid)
    H = len(grid[0])

    antennas = defaultdict(list)
    for i in range(H):
        for j in range(W):
            if grid[i][j] != ".":
                antennas[grid[i][j]].append((i, j))
    antennas = dict(antennas)

    visited_pairs = set()
    antinodes_at = set()

    for antenna in antennas:
        pairs = product(antennas[antenna], repeat=2)
        for a, b in pairs:
            if a == b:
                continue
            if (a, b) in visited_pairs or (b, a) in visited_pairs:
                continue
            visited_pairs.add((a, b))

            a1, a2 = get_two_antinodes(a, b)
            while any(
                [
                    node_in_bound(a1, H, W),
                    node_in_bound(a2, H, W),
                    node_in_bound(a, H, W),
                    node_in_bound(b, H, W),
                ]
            ):
                if node_in_bound(a1, H, W):
                    antinodes_at.add(a1)
                if node_in_bound(a2, H, W):
                    antinodes_at.add(a2)
                if node_in_bound(a, H, W):
                    antinodes_at.add(a)
                if node_in_bound(b, H, W):
                    antinodes_at.add(b)

                new_a1, _ = get_two_antinodes(a1, a)
                a = a1
                a1 = new_a1

                _, new_a2 = get_two_antinodes(b, a2)
                b = a2
                a2 = new_a2

    return len(antinodes_at)


print(part1())
print(part2())
