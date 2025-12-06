def part1() -> int:
    with open("../data/input06.txt", "r") as fp:
        lines = fp.read().strip().splitlines()

    parts = []
    for line in lines:
        parts.append(line.split())

    nums = parts[:-1]
    ops = parts[-1]

    tot = 0

    for i in range(len(ops)):
        k = 0 if ops[i] == "+" else 1
        for c in nums:
            if ops[i] == "+":
                k += int(c[i])
            else:
                k *= int(c[i])

        tot += k

    return tot


def part2() -> int:
    with open("../data/input06.txt", "r") as fp:
        lines = fp.read().splitlines()

    ops = lines[-1]
    cols = []

    i = 1
    le = 0
    while i < len(ops):
        c = ops[i]
        if c in "+*":
            cols.append(le)
            le = 0
        else:
            le += 1

        i += 1
    cols.append(le + 1)
    le = 0

    parts = []
    for i in range(len(lines) - 1):
        sec = []
        for c in cols:
            sec.append(lines[i][:c])
            lines[i] = lines[i][c + 1 :]

        parts.append(sec)

    ops = lines[-1].split()
    nums = [[] for _ in range(len(ops))]

    for i in range(len(ops)):
        for k in parts:
            nums[i].append(k[i])

    tot = 0

    for i in range(len(nums)):
        nop = nums[i]
        op = ops[i]

        k = 0 if ops[i] == "+" else 1

        for i in range(len(nop[0])):
            col_num = ""
            for p in nop:
                col_num += p[i]

            if op == "+":
                k += int(col_num)
            else:
                k *= int(col_num)

        tot += k

    return tot


print(part1())
print(part2())
