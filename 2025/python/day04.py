def part1() -> int:
    with open("../data/input04.txt", "r") as fp:
        lines = fp.read().strip().splitlines()

    ct = 0

    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if lines[x][y] != "@":
                continue

            thiscount = 0
            dirs = [(-1, 0), (0, -1), (1, 0), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1)]

            # check 8 dirs
            for dx, dy in dirs:
                tx = x + dx
                ty = y + dy

                if tx >= 0 and tx < len(lines) and ty >= 0 and ty < len(lines[x]):
                    if lines[tx][ty] == "@":
                        thiscount += 1

            if thiscount < 4:
                ct += 1

    return ct


def part2() -> int:
    with open("../data/input04.txt", "r") as fp:
        lines = fp.read().strip().splitlines()

    ct = 0
    removed_last = True

    lines = [list(li) for li in lines]

    while removed_last:
        removed_last = False
        for x in range(len(lines)):
            for y in range(len(lines[x])):
                if lines[x][y] != "@":
                    continue

                thiscount = 0
                dirs = [(-1, 0), (0, -1), (1, 0), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1)]

                # check 8 dirs
                for dx, dy in dirs:
                    tx = x + dx
                    ty = y + dy

                    if tx >= 0 and tx < len(lines) and ty >= 0 and ty < len(lines[x]):
                        if lines[tx][ty] == "@":
                            thiscount += 1

                if thiscount < 4:
                    ct += 1
                    lines[x][y] = "."
                    removed_last = True

    return ct


print(part1())
print(part2())
