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

    for i in instructions:
        dx, dy = directions[i]
        nx, ny = x + dx, y + dy

        # don't go in wall
        if (nx, ny) in walls:
            continue

        if nx < 0 or nx >= H or ny < 0 or ny >= W:
            continue

        # it's a box
        if (nx, ny) in boxes:
            # check next in that dir
            bnx, bny = nx + dx, ny + dy
            while (bnx, bny) in boxes:
                bnx, bny = bnx + dx, bny + dy

            if (bnx, bny) in walls:
                continue

            if bnx < 0 or bnx >= H or bny < 0 or bny >= W:
                continue

            tbnx, tbny = nx, ny

            while (tbnx, tbny) != (bnx, bny):
                boxes.remove((tbnx, tbny))
                tbnx, tbny = tbnx + dx, tbny + dy
                boxes.append((tbnx, tbny))

        x, y = nx, ny

    gps = 0

    for bx, by in boxes:
        gps += 100 * bx + by

    return gps


def print_grid(H, W, boxes, walls, pos):
    x, y = pos
    for i in range(H):
        for j in range(W):
            if (i, j) == (x, y):
                print("@", end="")
            elif (i, j) in walls:
                print("#", end="")
            elif (i, j) in boxes:
                print("[", end="")
            elif j - 1 > 0 and j - 1 <= W and (i, j - 1) in boxes:
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
    boxes = list()

    for i in range(H):
        for j in range(0, W, 2):
            if grid[i][j] == "@":
                x, y = i, j
            elif grid[i][j] == "#":
                walls.add((i, j))
                walls.add((i, j + 1))
            elif grid[i][j] == "[":
                boxes.append((i, j))

    directions = {"^": (-1, 0), "<": (0, -1), ">": (0, 1), "v": (1, 0)}

    for i in instructions:
        dx, dy = directions[i]

        to_move = [(x, y)]
        i = 0
        can_move = True
        while i < len(to_move):
            _x, _y = to_move[i]
            _nx, _ny = _x + dx, _y + dy

            if (_nx, _ny) in boxes or (_nx, _ny - 1) in boxes:
                if (_nx, _ny) not in to_move:
                    to_move.append((_nx, _ny))
                if (_nx, _ny) in boxes:
                    if (_nx, _ny + 1) not in to_move:
                        to_move.append((_nx, _ny + 1))
                if (_nx, _ny - 1) in boxes:
                    if (_nx, _ny - 1) not in to_move:
                        to_move.append((_nx, _ny - 1))
            elif grid[_nx][_ny] == "#":
                can_move = False
                break
            i += 1

        if not can_move:
            continue

        nx, ny = x + dx, y + dy
        to_move = list(filter(lambda x: x in boxes, to_move))

        for mx, my in to_move:
            if (mx, my) == (x, y):
                continue
            if (mx, my) in boxes:
                boxes.remove((mx, my))
                boxes.append((mx + dx, my + dy))
        x, y = nx, ny
    gps = 0

    for bx, by in boxes:
        gps += 100 * bx + by

    return gps


print(part1())
print(part2())
