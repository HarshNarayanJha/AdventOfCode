def part1() -> int:
    list1 = []
    list2 = []

    with open("../input1.txt", "r") as inp:
        while line := inp.readline():
            n, m = line.split()
            list1.append(int(n))
            list2.append(int(m))

    list1.sort()
    list2.sort()

    dist_sum = 0

    for j, k in zip(list1, list2):
        dist_sum += abs(j - k)

    return dist_sum


def part2() -> int:
    list1 = []
    list2 = {}

    with open("../input1.txt", "r") as inp:
        while line := inp.readline():
            n, m = line.split()
            list1.append(int(n))

            m = int(m)
            if m in list2:
                list2[m] += 1
            else:
                list2[m] = 1

    similarity_score = 0

    for k in list1:
        similarity_score += k * list2.get(k, 0)

    return similarity_score

print(part1())
print(part2())
