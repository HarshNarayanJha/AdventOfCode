def part1() -> int:
    disk = None
    with open("../data/input9.txt", "r") as inp:
        disk = inp.read().strip()

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


def part2() -> int:
    disk = None
    with open("../data/input9.txt", "r") as inp:
        disk = inp.read().strip()

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

    # defragment whole disk, file in groups
    b = len(fs) - 1
    while b >= 0:
        if fs[b] != -1:
            # start of file
            # calculate file size
            file_from = b
            file_to = file_from
            fid = fs[file_from]
            while fs[file_to] == fid:
                file_to -= 1
            fsize = file_from - file_to

            # search for empty space before the start of the current file
            empty_from = 0
            esize = 0
            while empty_from < b:
                while empty_from < b and fs[empty_from] != -1:
                    empty_from += 1

                # calculate it's size
                while empty_from + esize < b and fs[empty_from + esize] == -1:
                    esize += 1

                if esize >= fsize:
                    break

                empty_from += 1
                esize = 0

            if fsize <= esize:
                # move blocks
                for i in range(fsize):
                    fs[empty_from + i], fs[file_from - i] = (
                        fs[file_from - i],
                        fs[empty_from + i],
                    )
            else:
                # can't move
                pass

            b = b - fsize
        else:
            b -= 1

    res = sum([i * b for i, b in enumerate(fs) if b != -1])

    return res


print(part1())
print(part2())
