from numpy.linalg import solve


def part1() -> int:
    machines = []
    with open("../data/input13.txt") as inp:
        but_a = None
        but_b = None
        prize = None
        for line in inp.readlines():
            if not line.strip():
                machines.append((but_a, but_b, prize))
            elif "Button A" in line:
                xy = line.split(":")[1].strip()
                but_a = (
                    int(xy.split(", ")[0].split("+")[1]),
                    int(xy.split(", ")[1].split("+")[1]),
                )
            elif "Button B" in line:
                xy = line.split(":")[1].strip()
                but_b = (
                    int(xy.split(", ")[0].split("+")[1]),
                    int(xy.split(", ")[1].split("+")[1]),
                )
            elif "Prize" in line:
                xy = line.split(":")[1].strip()
                prize = (
                    int(xy.split(", ")[0].split("=")[1]),
                    int(xy.split(", ")[1].split("=")[1]),
                )

        machines.append((but_a, but_b, prize))

    cost = 0

    for a, b, p in machines:
        min_total_cost = float("inf")
        best_a = best_b = 0
        curr_x, curr_y = (0, 0)

        for bp in range(100):
            curr_b_x, curr_b_y = b[0] * bp, b[1] * bp
            for ap in range(100):
                curr_x, curr_y = curr_b_x + a[0] * ap, curr_b_y + a[1] * ap
                if (curr_x, curr_y) == p:
                    total_cost = ap * 3 + bp * 1
                    if total_cost < min_total_cost:
                        min_total_cost = total_cost
                        best_a = ap
                        best_b = bp

        cost += min_total_cost if min_total_cost != float("inf") else 0

    return int(cost)


def part2() -> int:
    machines = []
    with open("../data/input13.txt") as inp:
        but_a = None
        but_b = None
        prize = None
        for line in inp.readlines():
            if not line.strip():
                machines.append((but_a, but_b, prize))
            elif "Button A" in line:
                xy = line.split(":")[1].strip()
                but_a = (
                    int(xy.split(", ")[0].split("+")[1]),
                    int(xy.split(", ")[1].split("+")[1]),
                )
            elif "Button B" in line:
                xy = line.split(":")[1].strip()
                but_b = (
                    int(xy.split(", ")[0].split("+")[1]),
                    int(xy.split(", ")[1].split("+")[1]),
                )
            elif "Prize" in line:
                xy = line.split(":")[1].strip()
                prize = (
                    int(xy.split(", ")[0].split("=")[1]) + 10000000000000,
                    int(xy.split(", ")[1].split("=")[1]) + 10000000000000,
                )

        machines.append((but_a, but_b, prize))

    cost = 0

    for a, b, p in machines:
        x1, y1 = a
        x2, y2 = b
        x3, y3 = p

        # so this was easy after all, linear algebra!
        # x1 y1, x2 y2 and x3, y3
        # need to find ax1 + bx2 = x3 and ay1 + by2 = y3
        # this is just a system of equation in 2 variables a and b
        # ⎡ x1 y1 ⎤ ⎡ a ⎤   ⎡ x3 ⎤
        # ⎣ x2 y2 ⎦ ⎣ b ⎦ = ⎣ y3 ⎦
        # Using the powers of linear algebra, we will be solving for a and b
        # that solution will exists, and it will be unique (not neccesarily integers)
        # we find it using the inverse of the matrix
        #         ⎡ x1 y1 ⎤
        # let A = ⎣ x2 y2 ⎦
        #
        # Then find A^-1, which is inverse of A, multiplying both sides of the inverse of A reveals a and b
        # ⎡ a ⎤   ⎡ x3 ⎤ ⎡ x1 y1 ⎤^-1
        # ⎣ b ⎦ = ⎣ y3 ⎦ ⎣ x2 y2 ⎦
        #
        # this is just what we need to do!

        solution = solve([[x1, x2], [y1, y2]], [x3, y3])
        solution = [round(solution[0], 4), round(solution[1], 4)]
        if solution[0].is_integer() and solution[1].is_integer():
            cost += solution[0] * 3 + solution[1]

    return int(cost)


print(part1())
print(part2())
