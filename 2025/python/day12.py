from pprint import pprint


def part1() -> int:
    presents = {}
    regions = []

    with open("../data/input12.txt", "r") as f:
        lines = f.read().strip().split("\n\n")

    raw_presents = lines[:-1]
    raw_regions = lines[-1]

    for p in raw_presents:
        ps = p.splitlines()
        idx = int(ps[0].strip().strip(":"))
        shape = [line.strip() for line in ps[1:]]
        presents[idx] = [shape]

        # all variants
        shape_flip = ["".join(list(reversed(row))) for row in shape]
        presents[idx].append(shape_flip)

        shape_rot = [list(zip(*reversed(shape))) for shape in presents[idx]]
        shape_rot = [["".join(x) for x in y] for y in shape_rot]
        presents[idx].extend(shape_rot)

    for r in raw_regions.splitlines():
        shape, quantity = r.split(": ")
        quantity = list(map(int, quantity.split()))
        regions.append((tuple(map(int, shape.split("x"))), quantity))

    # pprint(presents)
    # pprint(regions)

    completes = 0
    # check each region one by one
    for reg in regions:
        (w, h), preq = reg
        grid = ["." * w] * h

        req = {i: c for i, c in enumerate(preq)}
        pres = [(presents[i], req[i]) for i in req if req[i] > 0]

        grid_area = w * h
        total_shapes_area = 0

        for p, q in pres:
            # total_shapes_area += "".join(p[0]).count("#") * q
            total_shapes_area += len(p[0]) * len(p[0][0]) * q

        if total_shapes_area > grid_area:
            # print("Impossible", total_shapes_area, grid_area)
            continue

        # if any(len(p[0]) * len(p[0][0]) > grid_area for p, _ in pres):
        #     print("Impossible")
        #     continue

        # valid
        # print("Valid", total_shapes_area, grid_area)
        completes += 1

        # # visualize
        # for g in grid:
        #     print(g)

        # print()
        # for p, q in pres:
        #     for x in p:
        #         for v in x:
        #             print(*v, sep="")
        #         print()

        # print()

    return completes


def part2() -> int:
    print("You help the Elves decorate the Christmas trees with all 24 stars!")
    return 24


print(part1())
print(part2())
