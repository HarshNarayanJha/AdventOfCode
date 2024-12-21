from collections import defaultdict
from itertools import product


def path_to(target, current, keypad):
    # print("Going from", current, "to", target, "in", keypad)
    visited = set()
    # Store (pos, path, path_length) in queue
    queue = [(current, "", 0)]
    shortest_paths = []
    shortest_len = float("inf")

    while queue:
        (curr_x, curr_y), path, path_len = queue.pop(0)

        if path_len > shortest_len:
            continue

        if (curr_x, curr_y) == target:
            if path_len < shortest_len:
                shortest_paths = [path + "A"]
                shortest_len = path_len
            elif path_len == shortest_len:
                shortest_paths.append(path + "A")
            continue

        # Try all 4 directions
        for dx, dy, dir_char in [(0, 1, ">"), (0, -1, "<"), (-1, 0, "^"), (1, 0, "v")]:
            new_x = curr_x + dx
            new_y = curr_y + dy

            # Check if valid move
            if (
                new_x < 0
                or new_x >= len(keypad)
                or new_y < 0
                or new_y >= len(keypad[0])
                or keypad[new_x][new_y] == " "
            ):
                continue

            queue.append(((new_x, new_y), path + dir_char, path_len + 1))

    return shortest_paths if shortest_paths else []


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

    arm_initial_1 = (3, 2)
    arm_initial_2 = (0, 2)
    arm_initial_3 = (0, 2)

    current_1 = arm_initial_1
    current_2 = arm_initial_2
    current_3 = arm_initial_3

    complexities = 0

    for code in codes:
        paths_1 = []
        paths_2 = []
        paths_3 = []

        possible_paths_1 = []
        possible_paths_2 = []
        possible_paths_3 = []

        for k in code:
            dest_1 = keypad_pos[k]
            seqs_1 = path_to(dest_1, current_1, keypad)

            possible_paths_1.append(seqs_1)

            print("Processing the code for", k, "found", seqs_1)
            current_1 = dest_1

        paths_1 = ["".join(c) for c in product(*possible_paths_1)]
        paths_1 = paths_1[:1]
        print(f"Found {len(paths_1)} paths 1")
        print(paths_1)

        for p in paths_1:
            for s1 in p:
                # print("Processing level 1 for", s1)
                dest_2 = dir_keypad_pos[s1]
                seqs_2 = path_to(dest_2, current_2, dir_keypad)

                possible_paths_2.append(seqs_2)

                current_2 = dest_2

            current_2 = arm_initial_2

        paths_2 = ["".join(c) for c in product(*possible_paths_2)]
        # paths_2 = [paths_2[16]]

        print(f"Found {len(paths_2)} paths 2")
        print(paths_2)

        for p in paths_2:
            for s2 in p:
                dest_3 = dir_keypad_pos[s2]
                seqs_3 = path_to(dest_3, current_3, dir_keypad)

                possible_paths_3.append(seqs_3)

                current_3 = dest_3

            current_3 = arm_initial_3

        paths_3 = ["".join(c) for c in product(*possible_paths_3)]
        paths_3 = paths_3[:1]
        print(f"Found {len(paths_3)} paths 3")

        print(paths_3)
        print(paths_2)
        print(paths_1)
        print(code)

        print(len(min(paths_3)), "*", int(code.replace("A", "")))
        print()
        complexities += len(min(paths_3)) * int(code.replace("A", ""))

    return complexities


def part2() -> int: ...


print(part1())
print(part2())
