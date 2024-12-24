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

    zOutputs = {}
    for n, o in inputs.items():
        if n.startswith("z"):
            zOutputs[n] = o

    keys = sorted(zOutputs, reverse=True)
    result = ""

    for k in keys:
        result += str(zOutputs[k])

    return int(result, base=2)


def part2() -> int:
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

    swapped1 = set()
    swapped2 = set()

    for conn in connections:
        in1, in2 = conn.in1, conn.in2
        out = conn.out
        gate = conn.gate

        if out.startswith("z") and "45" not in out and gate != "XOR":
            swapped1.add(conn)

        if not out.startswith("z") and in1[0] not in ("x", "y") and in2[0] not in ("x", "y") and gate == "XOR":
            swapped2.add(conn)

    # need to find 2 more

    for s in swapped2:
        seen = set()
        to_visit = {s}
        while to_visit:
            n = to_visit.pop()
            if n in seen:
                continue

            if n.out.startswith("z"):
                num = int(n.out.strip("z"))
                n1 = list(filter(lambda x: f"z{num-1:002}" in x.out, connections))[0]

                # swap
                so, no = s.out, n1.out
                ss = Connection(in1=s.in1, in2=s.in2, gate=s.gate, out=no)
                n1s = Connection(in1=n1.in1, in2=n1.in2, gate=n1.gate, out=so)
                connections.remove(s)
                connections.append(ss)
                connections.remove(n1)
                connections.append(n1s)
                break

            # add neighbours
            for c in connections:
                if c.in1 == n.out or c.in2 == n.out:
                    to_visit.add(c)

            seen.add(n)

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

    while len(left_over) != 0:
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

    xOutputs = {}
    for n, o in inputs.items():
        if n.startswith("x"):
            xOutputs[n] = o
    xKeys = sorted(xOutputs, reverse=True)
    xResult = ""
    for k in xKeys:
        xResult += str(xOutputs[k])

    yOutputs = {}
    for n, o in inputs.items():
        if n.startswith("y"):
            yOutputs[n] = o
    yKeys = sorted(yOutputs, reverse=True)
    yResult = ""
    for k in yKeys:
        yResult += str(yOutputs[k])

    zOutputs = {}
    for n, o in inputs.items():
        if n.startswith("z"):
            zOutputs[n] = o
    zKeys = sorted(zOutputs, reverse=True)
    zResult = ""
    for k in zKeys:
        zResult += str(zOutputs[k])

    xResult = int(xResult, base=2)
    yResult = int(yResult, base=2)
    zResult = int(zResult, base=2)

    correct = xResult + yResult

    delta = correct ^ zResult
    delta = format(delta, "b")

    zeroes = delta.count("0")
    print(zeroes)

    swapped3 = set()

    for c in connections:
        x = f"x{zeroes:002}"
        y = f"y{zeroes:002}"
        if c.in1 in (x, y) and c.in2 in (x, y) and c.gate in ("AND", "XOR"):
            swapped3.add(c.out)

    print(swapped1)
    print(swapped2)
    print(swapped3)

    result = []

    for k in swapped1:
        result.append(k.out)
    for k in swapped2:
        result.append(k.out)

    result += list(swapped3)

    print(','.join(sorted(result)))

    return 0


# print(part1())
print(part2())
