from collections import namedtuple


def part1() -> int:
    Connection = namedtuple("Connection", "in1 in2 gate out", defaults=("", "", "", ""))

    initial_inputs: dict[str, int] = {}
    connections: list[Connection] = []

    with open("../data/input24.txt", "r") as inp:
        inputs, wires = inp.read().split("\n\n")
        for input in inputs.splitlines():
            wire, val = input.strip().split(": ")
            initial_inputs[wire.strip()] = int(val.strip())

        for conn in wires.splitlines():
            _in, _out = conn.strip().split(" -> ")
            _in1, gate, _in2 = _in.strip().split(" ")
            connections.append(Connection(in1=_in1, in2=_in2, gate=gate, out=_out))

    inputs = initial_inputs.copy()

    left_over = []

    for conn in connections:
        in1, in2 = conn.in1, conn.in2
        out = conn.out
        gate = conn.gate

        if in1 in inputs and in2 in inputs:
            if out in inputs:
                continue

            in1 = inputs[in1]
            in2 = inputs[in2]
            o = 0
            if gate == "AND":
                o = in1 and in2
            elif gate == "OR":
                o = in1 or in2
            elif gate == "XOR":
                o = in1 ^ in2

            inputs[out] = o
        else:
            left_over.append(conn)

    print(inputs)

    while len(left_over) != 0:
        print(len(left_over), "left")
        conn = left_over.pop(0)
        in1, in2 = conn.in1, conn.in2
        out = conn.out
        gate = conn.gate

        if in1 in inputs and in2 in inputs:
            if out in inputs:
                continue

            in1 = inputs[in1]
            in2 = inputs[in2]
            o = 0
            if gate == "AND":
                o = in1 and in2
            elif gate == "OR":
                o = in1 or in2
            elif gate == "XOR":
                o = in1 ^ in2

            inputs[out] = o
        else:
            left_over.append(conn)

    print(initial_inputs)
    print(connections)
    print(inputs)

    zOutputs = {}
    for n, o in inputs.items():
        if n.startswith("z"):
            zOutputs[n] = o

    keys = sorted(zOutputs, reverse=True)
    result = ""

    for k in keys:
        result += str(zOutputs[k])

    print(result)

    return int(result, base=2)


def part2() -> int: ...


print(part1())
print(part2())
