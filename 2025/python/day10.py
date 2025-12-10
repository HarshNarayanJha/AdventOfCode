import re
from collections import deque, namedtuple

from ortools.sat.python import cp_model


def find_target_mask(indicator: str) -> int:
    mask = 0
    for i, c in enumerate(indicator):
        if c == "#":
            mask |= 1 << i
    return mask


def find_button_masks(buttons: list[list[int]]) -> list[int]:
    button_masks = []
    for b in buttons:
        m = 0
        for idx in b:
            m |= 1 << idx
        button_masks.append(m)

    return button_masks


def part1() -> int:
    with open("../data/input10.txt", "r") as fp:
        lines = fp.read().strip().splitlines()

    pat = re.compile(r"\[([.#]+)\] (.+) \{(.+)\}")

    Machine = namedtuple("Machine", ["indicator", "button", "joltages"])

    machines: list[Machine] = []
    for line in lines:
        indicator, buttons, joltages = re.match(pat, line).groups()  # pyright: ignore
        buttons = [list(map(int, x.strip("()").split(","))) for x in buttons.split()]
        joltages = list(map(int, joltages.split(",")))

        machines.append(Machine(indicator, buttons, joltages))

    leds = ["." * len(m.indicator) for m in machines]

    total = 0
    # pprint(machines)
    # pprint(leds)

    for i, led in enumerate(leds):
        target_mask = find_target_mask(machines[i].indicator)
        button_masks = find_button_masks(machines[i].button)

        start = 0
        visited = set([start])
        # (state, pressed so far)
        q = deque([(start, 0)])

        while q:
            s, p = q.popleft()
            if s == target_mask:
                total += p
                break

            for bm in button_masks:
                nxt = s ^ bm
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, p + 1))

    return total


def min_presses_llp(button_defs, target):
    n = len(target)
    m = len(button_defs)

    model = cp_model.CpModel()

    # Variables: x_j = number of presses of button j
    x = [model.NewIntVar(0, sum(target), f"x_{j}") for j in range(m)]

    # For each dimension i: sum( A[i][j] * x_j ) == target[i]
    for i in range(n):
        involved = [x[j] for j, btn in enumerate(button_defs) if i in btn]
        model.Add(sum(involved) == target[i])

    model.Minimize(sum(x))
    solver = cp_model.CpSolver()
    result = solver.Solve(model)

    if result == cp_model.OPTIMAL:
        presses = [solver.Value(v) for v in x]
        return sum(presses), presses
    else:
        return None, None


def part2() -> int:
    with open("../data/input10.txt", "r") as fp:
        lines = fp.read().strip().splitlines()

    pat = re.compile(r"\[([.#]+)\] (.+) \{(.+)\}")

    Machine = namedtuple("Machine", ["indicator", "button", "joltages"])

    machines: list[Machine] = []
    for line in lines:
        _indicator, _buttons, _joltages = re.match(pat, line).groups()  # pyright: ignore
        _buttons = [list(map(int, x.strip("()").split(","))) for x in _buttons.split()]
        _joltages = list(map(int, _joltages.split(",")))

        machines.append(Machine(_indicator, _buttons, _joltages))

    joltages = [[0] * len(m.joltages) for m in machines]

    total = 0
    # pprint(machines)
    # pprint(joltages)

    for i, jol in enumerate(joltages):
        target = tuple(machines[i].joltages)

        k, _ = min_presses_llp(machines[i].button, target)
        total += k if k else 0

        # this totally will not work

        # start = tuple(jol)
        # visited = set([start])
        # # (state, pressed so far)
        # q = deque([(start, 0)])

        # # print(target, buttons, start, q)

        # while q:
        #     print(len(q), total)
        #     state, presses = q.popleft()
        #     if state == target:
        #         total += presses
        #         break

        #     for but in buttons:
        #         nxt = tuple(state[i] + but[i] for i in range(N))
        #         # print(state, but, nxt)
        #         if any(nxt[i] > target[i] for i in range(N)):
        #             continue

        #         if nxt not in visited:
        #             visited.add(nxt)
        #             q.append((nxt, presses + 1))

        #     # assert False

    return total


print(part1())
print(part2())
