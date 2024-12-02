def is_report_safe(report: list[int]) -> bool:
    increasing_safes = [
        report[i + 1] > report[i] and (report[i + 1] - report[i]) <= 3
        for i in range(0, len(report) - 1)
    ]
    decreasing_safes = [
        report[i + 1] < report[i] and (report[i] - report[i + 1]) <= 3
        for i in range(0, len(report) - 1)
    ]

    return all(increasing_safes) or all(decreasing_safes)


def part1() -> int:
    reports = []

    with open("../data/input2.txt") as inp:
        lines = inp.readlines()
        for line in lines:
            reports.append(list(map(int, line.split())))

    results = []

    for report in reports:
        if is_report_safe(report):
            results.append(True)
        else:
            results.append(False)

    return results.count(True)


def part2() -> int:
    reports = []

    with open("../data/input2.txt") as inp:
        lines = inp.readlines()
        for line in lines:
            reports.append(list(map(int, line.split())))

    results = []

    for report in reports:
        if (
            is_report_safe(report)
            or is_report_safe(results[1:])
            or is_report_safe(results[:-1])
        ):
            results.append(True)
            continue

        for i, level in enumerate(report):
            if is_report_safe(report[:i] + report[i + 1 :]):
                results.append(True)
                break
        else:
            results.append(False)

    return results.count(True)


print(part1())
print(part2())
