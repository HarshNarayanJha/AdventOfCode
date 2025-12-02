def part1() -> int:
    with open("data/input1.txt", "r") as fp:
        lines = fp.read().splitlines()

    start = 50
    ct = 0

    for op in lines:
        if op[0] == "L":
            start = (start - int(op.strip("L"))) % 100
        elif op[0] == "R":
            start = (start + int(op.strip("R"))) % 100

        if start == 0:
            ct += 1

    return ct


def part2() -> int:
    with open("data/input1.txt", "r") as fp:
        lines = fp.read().splitlines()

    start = 50
    ct = 0

    for op in lines:
        print(start, op)
        if op[0] == "L":
            steps = int(op.strip("L"))
            # if start != 0 and start - steps < 0:
            #     if steps > 99:
            #         ct += (steps) // 99
            #     else:
            #         ct += (steps + 99) // 99

            # start = (start - steps) % 100

            while steps > 0:
                start -= 1

                if start == 0 and steps != 1:
                    ct += 1

                if start == -1:
                    start = 99

                steps -= 1

        elif op[0] == "R":
            steps = int(op.strip("R"))
            # if start + steps > 100:
            #     if steps > 99:
            #         ct += (steps) // 99
            #     else:
            #         ct += (steps + 99) // 99

            # start = (start + steps) % 100

            while steps > 0:
                start += 1

                if start == 100:
                    start = 0

                if start == 0 and steps != 1:
                    ct += 1

                steps -= 1

        if start == 0:
            ct += 1

        print(ct)
        print()

    return ct


print(part1())
print(part2())
