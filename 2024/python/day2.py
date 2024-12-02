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

    safe_reports = 0

    for report in reports:
        if is_report_safe(report):
            safe_reports += 1

    return safe_reports


def part2() -> int:
    reports = []

    with open("../data/input2.txt") as inp:
        lines = inp.readlines()
        for line in lines:
            reports.append(list(map(int, line.split())))

    safe_reports = 0

    for report in reports:
        if is_report_safe(report):
            safe_reports += 1
            continue

        for i, level in enumerate(report):
            if is_report_safe(report[:i] + report[i + 1 :]):
                safe_reports += 1
                break

    return safe_reports


print(part1())
print(part2())
