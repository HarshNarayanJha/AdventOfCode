import heapq


def part1() -> int:
    with open("../data/input08.txt", "r") as fp:
        lines = fp.read().strip().splitlines()

    coords = [tuple(map(int, line.split(","))) for line in lines]

    pairs = []
    n = len(coords)

    for i in range(n):
        for j in range(n):
            if i >= j:
                continue
            d = (
                (coords[i][0] - coords[j][0]) ** 2
                + (coords[i][1] - coords[j][1]) ** 2
                + (coords[i][2] - coords[j][2]) ** 2
            )
            pairs.append((d, i, j))

    heapq.heapify(pairs)

    circuits = [{c} for c in coords]

    for i in range(1000):
        _, i, j = heapq.heappop(pairs)
        a = coords[i]
        b = coords[j]

        to_merge = [cir for cir in circuits if a in cir or b in cir]

        if not to_merge:
            circuits.append({a, b})
        else:
            new_cir = set()
            for cir in to_merge:
                new_cir.update(cir)
                circuits.remove(cir)
            new_cir.update([a, b])
            circuits.append(new_cir)

    lensss = list(len(q) for q in circuits)
    nlargest = heapq.nlargest(3, lensss)

    return nlargest[0] * nlargest[1] * nlargest[2]


def part2() -> int:
    with open("../data/input08.txt", "r") as fp:
        lines = fp.read().strip().splitlines()

    coords = [tuple(map(int, line.split(","))) for line in lines]

    pairs = []
    n = len(coords)

    for i in range(n):
        for j in range(n):
            if i >= j:
                continue
            d = (
                (coords[i][0] - coords[j][0]) ** 2
                + (coords[i][1] - coords[j][1]) ** 2
                + (coords[i][2] - coords[j][2]) ** 2
            )
            pairs.append((d, i, j))

    heapq.heapify(pairs)

    circuits = [{c} for c in coords]

    while True:
        _, i, j = heapq.heappop(pairs)
        a = coords[i]
        b = coords[j]

        to_merge = [cir for cir in circuits if a in cir or b in cir]

        if not to_merge:
            circuits.append({a, b})
        else:
            new_cir = set()
            for cir in to_merge:
                new_cir.update(cir)
                circuits.remove(cir)
            new_cir.update([a, b])
            circuits.append(new_cir)

        if len(circuits) == 1:
            break

    return a[0] * b[0]


print(part1())
print(part2())
