from collections import deque
from pprint import pprint


def part1() -> int:
    with open("../data/input11.txt", "r") as fp:
        lines = fp.read().strip().splitlines()

    conns = {}
    for line in lines:
        parts = line.split(": ")
        conns[parts[0]] = parts[1].split()

    paths = 0
    start = "you"
    finish = "out"
    q = deque([start])
    visited = set()

    while q:
        node = q.popleft()
        if node == finish:
            paths += 1
            continue

        visited.add(node)
        for neighbor in conns[node]:
            if neighbor not in visited:
                q.append(neighbor)

    # pprint(conns)
    return paths


def part2() -> int:
    with open("../data/input11.txt", "r") as fp:
        lines = fp.read().strip().splitlines()

    conns = {}
    for line in lines:
        parts = line.split(": ")
        conns[parts[0]] = parts[1].split()

    # failed dfs attempt
    #
    # paths = 0
    # start = "svr"
    # finish = "out"
    # # node, dac, fft
    # q = deque([(start, False, False)])
    # visited = set()

    # while q:
    #     print(len(q))
    #     node, dac, fft = q.popleft()
    #     if node == finish:
    #         if dac and fft:
    #             paths += 1
    #         continue

    #     visited.add(node)
    #     for neighbor in conns[node]:
    #         if neighbor not in visited:
    #             q.append((neighbor, dac or (node == "dac"), fft or (node == "fft")))

    memo = {}

    def count(node, saw_dac, saw_fft):
        if node == "out":
            return 1 if (saw_dac and saw_fft) else 0
        key = (node, saw_dac, saw_fft)
        if key in memo:
            return memo[key]
        total = 0
        for nbr in conns[node]:
            total += count(nbr, saw_dac or (nbr == "dac"), saw_fft or (nbr == "fft"))
        memo[key] = total
        return total

    # pprint(conns)
    return count("svr", False, False)


print(part1())
print(part2())
