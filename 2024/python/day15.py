from pprint import pprint


def part1() -> int:
    grid = []
    instructions = []

    with open("../data/input15.txt", "r") as inp:
        store_directions = False

        for line in inp.readlines():
            if not line.strip():
                store_directions = True
                continue

            if not store_directions:
                grid.append(list(line.strip()))
            else:
                instructions.append(line.strip())

    instructions = "".join(instructions)
    pprint(grid)
    # print(instructions)

    H = len(grid)
    W = len(grid[0])

    x, y = (0, 0)
    walls = set()
    boxes = list()

    for i in range(H):
        for j in range(W):
            match grid[i][j]:
                case "@":
                    x, y = i, j
                case "#":
                    walls.add((i, j))
                case "O":
                    boxes.append((i, j))

    directions = {"^": (-1, 0), "<": (0, -1), ">": (0, 1), "v": (1, 0)}

    print("\n\n")

    for i in instructions:
        print(f"At {(x, y)}")
        print(f"Gotta move in {i}")
        dx, dy = directions[i]
        nx, ny = x + dx, y + dy

        print(f"Checking {(nx, ny)}")

        # don't go in wall
        if (nx, ny) in walls:
            print(f"{(nx, ny)} is a wall, won't move")
            continue

        if nx < 0 or nx >= H or ny < 0 or ny >= W:
            print(f"{(nx, ny)} oob, won't move")
            continue

        # it's a box
        if (nx, ny) in boxes:
            print(f"{(nx, ny)} is a box, checking if can move, checking next to box")
            # check next in that dir
            bnx, bny = nx + dx, ny + dy
            while (bnx, bny) in boxes:
                print(f"{(bnx, bny)} is also a box")
                bnx, bny = bnx + dx, bny + dy

            if (bnx, bny) in walls:
                print(f"{(bnx, bny)} is a wall, can't move these boxes")
                continue

            if bnx < 0 or bnx >= H or bny < 0 or bny >= W:
                print(f"{(bnx, bny)} is a oob, can't move these boxes")
                continue

            print(f"{(bnx, bny)} is empty, can move all those boxes")
            tbnx, tbny = nx, ny

            while (tbnx, tbny) != (bnx, bny):
                boxes.remove((tbnx, tbny))
                tbnx, tbny = tbnx + dx, tbny + dy
                boxes.append((tbnx, tbny))

        x, y = nx, ny

    for i in range(H):
        for j in range(W):
            if (i, j) == (x, y):
                print("@", end="")
            elif (i, j) in walls:
                print("#", end="")
            elif (i, j) in boxes:
                print("O", end="")
            else:
                print(".", end="")
        print()

    gps = 0

    for bx, by in boxes:
        gps += 100 * bx + by

    return gps


def part2() -> int: ...


print(part1())
print(part2())
