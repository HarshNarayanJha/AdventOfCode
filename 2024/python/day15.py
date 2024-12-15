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


def print_grid(grid, boxes, walls, pos):
    x, y = pos
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) == (x, y):
                print("@", end="")
            elif (i, j) in walls:
                print("#", end="")
            elif (i, j) in boxes:
                print("[", end="")
            elif j - 1 > 0 and j - 1 <= len(grid[0]) and (i, j - 1) in boxes:
                print("]", end="")
            else:
                print(".", end="")
        print()


def part2() -> int:
    grid = []
    instructions = []

    with open("../data/input15.txt", "r") as inp:
        store_directions = False

        for line in inp.readlines():
            if not line.strip():
                store_directions = True
                continue

            if not store_directions:
                # Expand row width by replacing characters
                expanded_row = []
                for c in line.strip():
                    if c == "#":
                        expanded_row.extend(["#", "#"])
                    elif c == "O":
                        expanded_row.extend(["[", "]"])
                    elif c == ".":
                        expanded_row.extend([".", "."])
                    elif c == "@":
                        expanded_row.extend(["@", "."])
                grid.append(expanded_row)
            else:
                instructions.append(line.strip())

    instructions = "".join(instructions)

    H = len(grid)
    W = len(grid[0])

    x, y = (0, 0)
    walls = set()
    boxes = list()  # Store both coordinates of box

    for i in range(H):
        for j in range(0, W, 2):
            if grid[i][j] == "@":
                x, y = i, j
            elif grid[i][j] == "#":
                walls.add((i, j))
                walls.add((i, j + 1))
            elif grid[i][j] == "[":
                boxes.append((i, j))
                # boxes.add((i, j + 1))

    print_grid(grid, boxes, walls, (x, y))

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

        if nx < 0 or nx >= H or ny < 0 or ny + 1 >= W:
            print(f"{(nx, ny)} oob, won't move")
            continue

        # it's a box
        if (nx, ny) in boxes or (nx, ny - 1) in boxes:
            if (nx, ny) in boxes:
                print(f"{(nx, ny), (nx, ny + 1)} is a box, checking if can move, checking next to box")
            else:
                print(f"{(nx, ny), (nx, ny - 1)} is a box, checking if can move, checking next to box")
            # check next in that dir
            bnx, bny = nx + dx, ny + (dy * 2)

            boxes_to_move = set()

            while (bnx, bny) in boxes or (bnx, bny - 1) in boxes:
                if (bnx, bny) in boxes:
                    print(f"{(bnx, bny), (bnx, bny + 1)} is also a box")
                    boxes_to_move.add((bnx, bny))
                else:
                    print(f"{(bnx, bny), (bnx, bny - 1)} is also a box")
                    boxes_to_move.add((bnx, bny - 1))
                    print("checking for any touching boxes")
                    if (bnx + dx, bny - 1 + (dy * 2)) in boxes:
                        boxes_to_move.add((bnx + dx, bny - 1 + (dy * 2)))
                    elif (bnx + dx, bny - 1 + (dy * 2) - 1) in boxes:
                        boxes_to_move.add((bnx + dx, bny - 1 + (dy * 2) - 1))

                bnx, bny = bnx + dx, bny + (dy * 2)

            if (bnx, bny) in walls:
                print(f"{(bnx, bny)} is a wall, can't move these boxes")
                continue

            if bnx < 0 or bnx >= H or bny < 0 or bny + 1 >= W:
                print(f"{(bnx, bny)} is a oob, can't move these boxes")
                continue

            print(f"{(bnx, bny)} is empty, can move all those boxes")
            tbnx, tbny = nx, ny

            num_boxes = abs(tbnx - bnx) or abs(tbny - bny) // 2

            if (tbnx, tbny) not in boxes:
                tbny -= 1

            print("Begin moving boxes")
            print(boxes_to_move)
            for _ in range(num_boxes):
                print(f"Remove {(tbnx, tbny)} from boxes")
                boxes.remove((tbnx, tbny))
                # boxes.remove((tbnx, tbny + 1))
                tbnx, tbny = tbnx + dx, tbny + dy
                print(f"Add {(tbnx, tbny)} to boxes")
                boxes.append((tbnx, tbny))
                tbnx, tbny = tbnx + dx, tbny + dy
                # boxes.add((tbnx, tbny + 1))
        x, y = nx, ny

        print_grid(grid, boxes, walls, (x, y))

        import time

        # time.sleep(1)

    print_grid(grid, boxes, walls, (x, y))

    gps = 0

    # Calculate distances from edges for each box
    for bx, by in boxes:
        if by % 2 == 0:  # Only count left edge of each box
            gps += 100 * bx + (by // 2)

    return gps


# print(part1())
print(part2())
