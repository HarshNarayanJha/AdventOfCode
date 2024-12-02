use std::time::Instant;

fn is_report_safe(report: &Vec<u32>) -> bool {
    let mut all_increasing = true;
    let mut all_decreasing = true;

    for i in 0..report.len() - 1 {
        if report[i] < report[i + 1] && (report[i + 1] - report[i] <= 3) {
            all_increasing = all_increasing && true;
        } else {
            all_increasing = false
        }

        if report[i] > report[i + 1] && (report[i] - report[i + 1] <= 3) {
            all_decreasing = all_decreasing && true;
        } else {
            all_decreasing = false
        }
    }

    all_increasing || all_decreasing
}

pub fn part1() -> u32 {
    let input = include_str!("../../data/input2.txt");

    let mut reports: Vec<Vec<u32>> = vec![];

    for line in input.lines() {
        let report: Vec<u32> = line
            .split_whitespace()
            .map(|e| e.parse().unwrap())
            .collect();
        reports.push(report);
    }

    let mut num_safe = 0;

    for report in reports {
        num_safe += if is_report_safe(&report) { 1 } else { 0 }
    }

    num_safe
}

pub fn part2() -> u32 {
    let input = include_str!("../../data/input2.txt");

    let mut reports: Vec<Vec<u32>> = vec![];

    for line in input.lines() {
        let report: Vec<u32> = line
            .split_whitespace()
            .map(|e| e.parse().unwrap())
            .collect();
        reports.push(report);
    }

    let mut num_safe = 0;

    for report in reports {
        if is_report_safe(&report) {
            num_safe += 1;
            continue;
        }

        for i in 0..report.len() {
            let mut unsafe_report: Vec<&u32> = report.iter().take(i).collect();
            let rest: Vec<&u32> = report.iter().skip(i + 1).collect();
            unsafe_report.extend(rest);

            if is_report_safe(&unsafe_report.iter().map(|&&x| x).collect()) {
                num_safe += 1;
                break;
            }
        }
    }

    num_safe
}

pub fn solve() {
    println!("\nDay {}", 2);

    let now = Instant::now();
    println!("Part 1 -> {}", part1());
    let elasped = now.elapsed();

    println!("Took {:.5}ms", elasped.as_secs_f64() * 1000.0);

    println!();

    let now = Instant::now();
    println!("Part 2 -> {}", part2());
    let elasped = now.elapsed();
    println!("Took {:.5}ms", elasped.as_secs_f64() * 1000.0);

    println!("{:-^30}", "-");
}
