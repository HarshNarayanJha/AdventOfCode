class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def copy(self):
        return Point(self.x, self.y)


def part1() -> int:
    machines: list[tuple[Point, Point, Point]] = []
    with open("../data/input13.txt") as inp:
        but_a: Point = Point()
        but_b: Point = Point()
        prize: Point = Point()
        for line in inp.readlines():
            if not line.strip():
                machines.append((but_a.copy(), but_b.copy(), prize.copy()))
            elif "Button A" in line:
                xy = line.split(":")[1].strip()
                but_a.x = int(xy.split(", ")[0].split("+")[1])
                but_a.y = int(xy.split(", ")[1].split("+")[1])
            elif "Button B" in line:
                xy = line.split(":")[1].strip()
                but_b.x = int(xy.split(", ")[0].split("+")[1])
                but_b.y = int(xy.split(", ")[1].split("+")[1])
            elif "Prize" in line:
                xy = line.split(":")[1].strip()
                prize.x = int(xy.split(", ")[0].split("=")[1])
                prize.y = int(xy.split(", ")[1].split("=")[1])

        machines.append((but_a.copy(), but_b.copy(), prize.copy()))

    cost = 0

    for a, b, p in machines:
        # print("Doing", a, b, p)
        min_total_cost = float("inf")
        best_a = best_b = 0
        curr = Point(0, 0)

        for bp in range(100):
            curr_b = Point(b.x * bp, b.y * bp)
            for ap in range(100):
                curr = curr_b + Point(a.x * ap, a.y * ap)
                if curr == p:
                    total_cost = ap * 3 + bp * 1
                    if total_cost < min_total_cost:
                        min_total_cost = total_cost
                        best_a = ap
                        best_b = bp

        cost += min_total_cost if min_total_cost != float("inf") else 0

    return int(cost)


def part2() -> int:
    machines: list[tuple[Point, Point, Point]] = []
    with open("../data/input13.txt") as inp:
        but_a: Point = Point()
        but_b: Point = Point()
        prize: Point = Point()
        for line in inp.readlines():
            if not line.strip():
                machines.append((but_a.copy(), but_b.copy(), prize.copy()))
            elif "Button A" in line:
                xy = line.split(":")[1].strip()
                but_a.x = int(xy.split(", ")[0].split("+")[1])
                but_a.y = int(xy.split(", ")[1].split("+")[1])
            elif "Button B" in line:
                xy = line.split(":")[1].strip()
                but_b.x = int(xy.split(", ")[0].split("+")[1])
                but_b.y = int(xy.split(", ")[1].split("+")[1])
            elif "Prize" in line:
                xy = line.split(":")[1].strip()
                prize.x = int(xy.split(", ")[0].split("=")[1])
                prize.y = int(xy.split(", ")[1].split("=")[1])
                prize.x += 10000000000000
                prize.y += 10000000000000

        machines.append((but_a.copy(), but_b.copy(), prize.copy()))

    cost = 0

    for a, b, p in machines:
        # print("Doing", a, b, p)
        min_total_cost = float("inf")
        best_a = best_b = 0
        curr = Point(0, 0)

        for bp in range(1000):
            curr_b = Point(b.x * bp, b.y * bp)
            print(bp)
            for ap in range(1000):
                curr = curr_b + Point(a.x * ap, a.y * ap)
                if curr == p:
                    total_cost = ap * 3 + bp * 1
                    if total_cost < min_total_cost:
                        min_total_cost = total_cost
                        best_a = ap
                        best_b = bp

        cost += min_total_cost if min_total_cost != float("inf") else 0

    return int(cost)


# print(part1())
print(part2())
