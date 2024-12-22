from itertools import product, permutations


def possible_paths(code, keypad):
    possibles = []
    cx, cy = keypad["A"]

    for c in code:
        nx, ny = keypad[c]
        dx, dy = nx - cx, ny - cy

        moves = ""
        if dx > 0:
            moves += "v" * dx
        elif dx < 0:
            moves += "^" * -dx
        if dy > 0:
            moves += ">" * dy
        elif dy < 0:
            moves += "<" * -dy

        directions = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}

        all_combos = list(set(["".join(x) + "A" for x in permutations(moves)]))
        valid_combos = []

        for combo in all_combos:
            valid = True
            tcx, tcy = cx, cy
            for c in combo[:-1]:
                dx, dy = directions[c]
                tcx, tcy = tcx + dx, tcy + dy

                if (tcx, tcy) not in keypad.values() or keypad[" "] == (tcx, tcy):
                    valid = False
                    break
            if valid:
                valid_combos.append(combo)

        possibles.append(valid_combos)
        cx, cy = nx, ny

    return ["".join(x) for x in product(*possibles)]


def part1() -> int:
    codes = None
    with open("../data/input21.txt", "r") as inp:
        codes = [line.strip() for line in inp.readlines()]

    keypad = [
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        [" ", "0", "A"],
    ]
    keypad_pos = {k: (i, j) for i, row in enumerate(keypad) for j, k in enumerate(row)}

    dir_keypad = [
        [" ", "^", "A"],
        ["<", "v", ">"],
    ]
    dir_keypad_pos = {
        k: (i, j) for i, row in enumerate(dir_keypad) for j, k in enumerate(row)
    }

    complexities = 0

    for code in codes:
        paths_1 = possible_paths(code, keypad_pos)
        paths_2 = []
        for path in paths_1:
            paths_2.extend(possible_paths(path, dir_keypad_pos))
        paths_3 = []
        for path in paths_2:
            paths_3.extend(possible_paths(path, dir_keypad_pos))

        print(code)

        complexities += min([len(x) for x in paths_3]) * int(code.replace("A", ""))

    return complexities


def part2() -> int:
    codes = None
    with open("../data/input21.txt", "r") as inp:
        codes = [line.strip() for line in inp.readlines()]

    keypad = [
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        [" ", "0", "A"],
    ]
    keypad_pos = {k: (i, j) for i, row in enumerate(keypad) for j, k in enumerate(row)}

    dir_keypad = [
        [" ", "^", "A"],
        ["<", "v", ">"],
    ]
    dir_keypad_pos = {
        k: (i, j) for i, row in enumerate(dir_keypad) for j, k in enumerate(row)
    }

    complexities = 0

    for code in codes:
        paths = possible_paths(code, keypad_pos)
        iterations = 24

        for _ in range(iterations):
            new_paths = []
            for path in paths:
                new_paths.extend(possible_paths(path, dir_keypad_pos))
            paths = new_paths

        print(code)

        complexities += min([len(x) for x in paths]) * int(code.replace("A", ""))

    return complexities


print(part1())
# print(part2())
