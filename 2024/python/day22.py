def next_secret(init):
    secret = init

    secret = secret ^ (secret * 64)
    secret = secret % 16777216

    secret = secret ^ (secret // 32)
    secret = secret % 16777216

    secret = secret ^ (secret * 2048)
    secret = secret % 16777216

    return secret


def part1() -> int:
    initials = []
    with open("../data/input22.txt", "r") as inp:
        initials = [int(x.strip()) for x in inp.readlines()]

    ITERS = 2000
    secrets_iterth = []

    for init in initials:
        secret = init
        for _ in range(ITERS):
            secret = next_secret(secret)

        secrets_iterth.append(secret)

    return sum(secrets_iterth)


def part2() -> int:
    initials = []
    with open("../data/input22.txt", "r") as inp:
        initials = [int(x.strip()) for x in inp.readlines()]

    ITERS = 2000
    secrets_changes: dict[int, list[None | int]] = {k: list([None]) for k in initials}

    for init in initials:
        secret = init
        for _ in range(ITERS):
            prev_ones = secret % 10
            secret = next_secret(secret)
            next_ones = secret % 10
            change = next_ones - prev_ones
            secrets_changes[init].append(change)

    sequnces: dict[tuple[int, ...], int] = {}

    num_first_secret_positives = len(
        list(filter(lambda x: x is not None and x > 0, secrets_changes[initials[0]]))
    )

    for _ in range(num_first_secret_positives):
        this_sum = 0
        seq_a = None
        seq_b = None
        seq_c = None
        seq_d = None

        # find next max in first secret changes
        max_so_far = -200000
        for i, _ in enumerate(secrets_changes[initials[0]][1:-3]):
            c = secrets_changes[initials[0]][i + 4]

            if c in seen.keys():
                continue

            if c is not None and c > max_so_far:
                max_so_far = c
                seq_a = secrets_changes[initials[0]][i]
                seq_b = secrets_changes[initials[0]][i + 1]
                seq_c = secrets_changes[initials[0]][i + 2]
                seq_d = secrets_changes[initials[0]][i + 3]

        if max_so_far < 0:
            continue

        print(
            "Found the highest yielding sequence in first number list:",
            seq_a,
            seq_b,
            seq_c,
            seq_d,
        )

        print("it gives:", max_so_far)

        # print("Adding other secrets to it for this sequence")
        for init2 in secrets_changes:
            for i2, _ in enumerate(secrets_changes[init2][1:-3]):
                c = secrets_changes[init2][i2 + 4]

                seq_a2 = secrets_changes[init2][i2]
                seq_b2 = secrets_changes[init2][i2 + 1]
                seq_c2 = secrets_changes[init2][i2 + 2]
                seq_d2 = secrets_changes[init2][i2 + 3]
                if (
                    seq_a2 == seq_a
                    and seq_b2 == seq_b
                    and seq_c2 == seq_c
                    and seq_d2 == seq_d
                ):
                    if c is not None:
                        # print(
                        #     "Found the next number for the current sequence in",
                        #     init2,
                        #     "list:",
                        #     n,
                        # )
                        this_sum += c
                        break
            else:
                pass
                # print("Didn't found sequence in", init2)

        # print()
        if this_sum > 0:
            print("This is the sum we got for this sequence", this_sum)
        seen[max_so_far] = this_sum

    # print(secrets_changes)
    # print([max(x[1:]) for x in secrets_changes.values()])
    print(seen)
    print(max(seen.values()))

    return 0


# print(part1())
print(part2())
