use crate::day::{Day, Solution};

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

pub struct Day2 {
    day: Day,
}

impl Day2 {
    pub fn new() -> Self {
        Self { day: Day::new(2) }
    }
}


impl Solution for Day2 {
    fn part1(&self) -> u64 {
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

    fn part2(&self) -> u64 {
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

    fn get_day(&self) -> u8 {
        self.day.day as u8
    }
}

pub fn run() {
    Day2::new().solve();
}
