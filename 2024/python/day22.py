from collections import defaultdict
from functools import cache


@cache
def next_secret(init):
    secret = init
    secret = (secret ^ (secret << 6)) % 16777216
    secret = (secret ^ (secret >> 5)) % 16777216
    secret = (secret ^ (secret << 11)) % 16777216
    return secret


def part1() -> int:
    with open("../data/input22.txt", "r") as inp:
        initials = [int(x) for x in inp.read().splitlines()]

    ITERS = 2000
    s = 0

    for init in initials:
        secret = init
        for _ in range(ITERS):
            secret = next_secret(secret)
        s += secret

    return s


def part2() -> int:
    with open("../data/input22.txt", "r") as inp:
        initials = [int(x) for x in inp.read().splitlines()]

    ITERS = 2000
    sequnces = defaultdict(int)

    for init in initials:
        seq = [0] * 4
        seen = set()
        secret = init
        prev_ones = secret % 10

        for i in range(ITERS):
            secret = next_secret(secret)
            next_ones = secret % 10
            change = next_ones - prev_ones

            if i < 4:
                seq[i] = change
            else:
                seq.pop(0)
                seq.append(change)
                seq_tuple = tuple(seq)

                if seq_tuple not in seen:
                    sequnces[seq_tuple] += next_ones
                    seen.add(seq_tuple)

            prev_ones = next_ones

    return max(sequnces.values())


print(part1())
print(part2())
