def part1() -> int:
    registers = {}
    program = []

    with open("../data/input17.txt", "r") as inp:
        registers_done = False
        lines = inp.readlines()

        for line in lines:
            if not line.strip():
                registers_done = True
                continue

            if not registers_done:
                _, reg, val = line.split()
                registers[reg.strip(":").strip()] = int(val.strip())
            else:
                program = list(map(int, line.split(": ")[1].split(",")))

    print(registers, program)

    ip = 0
    out = []

    while ip < len(program) - 1:
        inst = program[ip]
        literal_operand = program[ip + 1]
        combo_operand = 0

        # valid = True
        if literal_operand in (0, 1, 2, 3):
            combo_operand = literal_operand
        elif literal_operand == 4:
            combo_operand = registers["A"]
        elif literal_operand == 5:
            combo_operand = registers["B"]
        elif literal_operand == 6:
            combo_operand = registers["C"]

        jumped = False

        match inst:
            case 0:
                # adv = division
                numerator = registers["A"]
                denominator = 2**combo_operand
                result = numerator // denominator
                registers["A"] = result
            case 1:
                # blx = bitwise
                result = registers["B"] ^ literal_operand
                registers["B"] = result
            case 2:
                # bst = combo operand modulo 8 -> B
                registers["B"] = combo_operand % 8
            case 3:
                # jnz = jump to literal operand if A != 0. if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
                if registers["A"] != 0:
                    jumped = True
                    ip = literal_operand
            case 4:
                # bxc = B ^ C-> B (ignores operand)
                registers["B"] = registers["B"] ^ registers["C"]
            case 5:
                # out = combo % 8 -> output spearated by comma
                out.append(combo_operand % 8)
            case 6:
                # bdv = adv but store in b
                numerator = registers["A"]
                denominator = 2 ** (combo_operand)
                result = numerator // denominator
                registers["B"] = result
            case 7:
                # cdv = adv but store in c
                numerator = registers["A"]
                denominator = 2 ** (combo_operand)
                result = numerator // denominator
                registers["C"] = result

        if not jumped:
            ip += 2

    print(",".join(map(str, out)))
    return 0


def part2() -> int:
    ...

print(part1())
print(part2())
