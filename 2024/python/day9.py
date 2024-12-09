def part1() -> int:
    disk = None
    with open("../data/input9.txt", "r") as inp:
        lines = inp.readlines()
        disk = "".join([line.strip() for line in lines])

    fs = []
    fid = 0
    i = 0
    for b in disk:
        if i == 0:
            fs.extend([fid] * int(b))
            fid += 1
        elif i == 1:
            fs.extend([-1] * int(b))
        i = (i + 1) % 2

    # now defragment it

    for b in range(len(fs)):
        if fs[b] == -1:
            idx = -1
            while fs[idx] == -1:
                idx -= 1

            if len(fs) + idx == b - 1:
                break

            fs[b], fs[idx] = fs[idx], fs[b]
        else:
            pass

    res = sum([i * b for i, b in enumerate(fs[: fs.index(-1)])])

    return res


def part2() -> int: ...


print(part1())
print(part2())
