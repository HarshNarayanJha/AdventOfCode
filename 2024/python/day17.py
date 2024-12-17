def part1() -> int:
    RA = 0
    RB = 0
    RC = 0
    program = []

    with open("../data/input17.txt", "r") as inp:
        registers_done = False
        for line in inp.readlines():
            if not line.strip():
                registers_done = True
                continue

            if not registers_done:
                _, reg, val = line.split()
                if "A" in reg:
                    RA = int(val.strip())
                elif "B" in reg:
                    RB = int(val.strip())
                elif "C" in reg:
                    RC = int(val.strip())
            else:
                program = list(map(int, line.split(": ")[1].split(",")))

    ip = 0
    out = []

    while ip < len(program) - 1:
        inst = program[ip]
        literal_operand = program[ip + 1]
        combo_operand = 0

        if literal_operand <= 3:
            combo_operand = literal_operand
        elif literal_operand == 4:
            combo_operand = RA
        elif literal_operand == 5:
            combo_operand = RB
        elif literal_operand == 6:
            combo_operand = RC

        jumped = False

        match inst:
            case 0:
                # adv = right shift
                RA >>= combo_operand
            case 1:
                # blx = bitwise
                RB ^= literal_operand
            case 2:
                # bst = combo operand modulo 8 -> B
                RB = combo_operand & 7
            case 3:
                # jnz = jump to literal operand if A != 0. if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
                if RA != 0:
                    jumped = True
                    ip = literal_operand
            case 4:
                # bxc = B ^ C-> B (ignores operand)
                RB ^= RC
            case 5:
                # out = combo % 8 -> output spearated by comma
                out.append(combo_operand & 7)
            case 6:
                # bdv = adv but store in b
                RB = RA >> combo_operand
            case 7:
                # cdv = adv but store in c
                RC = RA >> combo_operand

        if not jumped:
            ip += 2

    print(",".join(map(str, out)))
    return 0


def part2() -> int:
    RA, RB, RC = 0, 0, 0
    program = []

    with open("../data/input17.txt", "r") as inp:
        program = inp.read().split("\n\n")[1]
        program = list(map(int, program.split(": ")[1].split(",")))

    # 35184372088832 start of 16 digits
    # 281475483175314 start of 17
    # lies somewhere inbetween
    ## IMP
    # a = 35184372088832
    # b = 281475483175314

    matching_As = {0}

    for expected in program[::-1]:
        for A in matching_As.copy():
            matching_As.remove(A)

            A *= 8
            for offset in range(8):
                RA = A + offset
                RB = 0
                RC = 0

                ip = 0
                out = []
                program_len = len(program) - 1

                while ip < program_len:
                    inst = program[ip]
                    literal_operand = program[ip + 1]
                    combo_operand = 0

                    if literal_operand <= 3:
                        combo_operand = literal_operand
                    elif literal_operand == 4:
                        combo_operand = RA
                    elif literal_operand == 5:
                        combo_operand = RB
                    elif literal_operand == 6:
                        combo_operand = RC

                    jumped = False

                    match inst:
                        case 0:
                            RA >>= combo_operand
                        case 1:
                            RB ^= literal_operand
                        case 2:
                            RB = combo_operand & 7
                        case 3:
                            if RA != 0:
                                jumped = True
                                ip = literal_operand
                        case 4:
                            RB ^= RC
                        case 5:
                            out.append(combo_operand & 7)
                        case 6:
                            RB = RA >> combo_operand
                        case 7:
                            RC = RA >> combo_operand

                    if not jumped:
                        ip += 2

                if out and out[0] == expected:
                    matching_As.add(A + offset)

    return min(matching_As)


print(part1())
print(part2())
