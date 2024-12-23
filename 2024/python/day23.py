from collections import defaultdict


def part1() -> int:
    csets = defaultdict(tuple)
    with open("../data/input23.txt", "r") as inp:
        lines = inp.readlines()
        for line in lines:
            a, b = tuple(line.strip().split("-"))
            csets[a] = csets[a] + (b,)
            csets[b] = csets[b] + (a,)

    lan_parties = []

    for s in csets:
        p1 = s
        for p2 in csets[p1]:
            for p3 in csets[p2]:
                if p3 == p1:
                    continue
                if p1 in csets[p3]:
                    group = tuple(sorted([p1, p2, p3]))
                    if group not in lan_parties:
                        lan_parties.append(group)

    lan_parties.sort()

    count = 0
    for p in lan_parties:
        if any([x.startswith("t") for x in p]):
            count += 1

    return count


def part2() -> int:
    csets = defaultdict(tuple)
    with open("../data/input23.txt", "r") as inp:
        lines = inp.readlines()
        for line in lines:
            a, b = tuple(line.strip().split("-"))
            csets[a] = csets[a] + (b,)
            csets[b] = csets[b] + (a,)

    max_group = set()

    for start in csets:
        visited = set([start])
        to_visit = set(csets[start])

        while to_visit:
            current = to_visit.pop()
            if current not in visited and all([x in csets[current] for x in visited]):
                visited.add(current)
                to_visit.update(
                    n
                    for n in csets[current]
                    if n not in visited and all([x in csets[n] for x in visited])
                )

        if len(visited) > len(max_group):
            max_group = visited.copy()

    lan_parties = list(sorted(max_group))

    print(",".join(lan_parties))

    return 0


print(part1())
print(part2())
