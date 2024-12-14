use crate::day::{Day, Solution};

pub struct Day13 {
    day: Day,
}

impl Day13 {
    pub fn new() -> Self {
        Self { day: Day::new(13) }
    }
}

impl Solution for Day13 {
    fn part1(&self) -> u64 {
        let input = include_str!("../../data/input13.txt");
        let mut machines: Vec<[(u64, u64); 3]> = vec![];

        let mut _a: (u64, u64) = (0, 0);
        let mut _b: (u64, u64) = (0, 0);
        let mut _p: (u64, u64) = (0, 0);
        for line in input.lines() {
            if line.is_empty() {
                machines.push([_a, _b, _p]);
            } else if line.contains("Button A") {
                let parts: Vec<&str> = line.split(": ").collect::<Vec<&str>>()[1]
                    .split(", ")
                    .take(2)
                    .collect();
                let (x, y) = (parts[0], parts[1]);

                let (x, y) = (
                    x.split("+").skip(1).collect::<Vec<&str>>()[0]
                        .parse::<u64>()
                        .unwrap(),
                    y.split("+").skip(1).collect::<Vec<&str>>()[0]
                        .parse::<u64>()
                        .unwrap(),
                );

                _a = (x, y);
            } else if line.contains("Button B") {
                let parts: Vec<&str> = line.split(": ").collect::<Vec<&str>>()[1]
                    .split(", ")
                    .take(2)
                    .collect();
                let (x, y) = (parts[0], parts[1]);

                let (x, y) = (
                    x.split("+").skip(1).collect::<Vec<&str>>()[0]
                        .parse::<u64>()
                        .unwrap(),
                    y.split("+").skip(1).collect::<Vec<&str>>()[0]
                        .parse::<u64>()
                        .unwrap(),
                );

                _b = (x, y);
            } else if line.contains("Prize") {
                let parts: Vec<&str> = line.split(": ").collect::<Vec<&str>>()[1]
                    .split(", ")
                    .take(2)
                    .collect();
                let (x, y) = (parts[0], parts[1]);

                let (x, y) = (
                    x.split("=").skip(1).collect::<Vec<&str>>()[0]
                        .parse::<u64>()
                        .unwrap(),
                    y.split("=").skip(1).collect::<Vec<&str>>()[0]
                        .parse::<u64>()
                        .unwrap(),
                );

                _p = (x, y);
            }
        }
        machines.push([_a, _b, _p]);

        let mut cost: u64 = 0;

        for [(x1, y1), (x2, y2), (x3, y3)] in machines {
            let x1 = x1 as i64;
            let y1 = y1 as i64;
            let x2 = x2 as i64;
            let y2 = y2 as i64;
            let x3 = x3 as i64;
            let y3 = y3 as i64;

            let det: i64 = x1 * y2 - x2 * y1;
            if det != 0 {
                let det_a: i64 = x3 * y2 - x2 * y3;
                let det_b: i64 = x1 * y3 - x3 * y1;

                let a: i64 = det_a / det;
                let b: i64 = det_b / det;

                if det_a % det == 0 && det_b % det == 0 && a >= 0 && b >= 0 {
                    let total_cost = a * 3 + b;
                    if total_cost > 0 {
                        cost += total_cost as u64;
                    }
                }
            }
        }

        cost
    }

    fn part2(&self) -> u64 {
        let input = include_str!("../../data/input13.txt");
        let mut machines: Vec<[(u64, u64); 3]> = vec![];

        let mut _a: (u64, u64) = (0, 0);
        let mut _b: (u64, u64) = (0, 0);
        let mut _p: (u64, u64) = (0, 0);
        for line in input.lines() {
            if line.is_empty() {
                machines.push([_a, _b, _p]);
            } else if line.contains("Button A") {
                let parts: Vec<&str> = line.split(": ").collect::<Vec<&str>>()[1]
                    .split(", ")
                    .take(2)
                    .collect();
                let (x, y) = (parts[0], parts[1]);

                let (x, y) = (
                    x.split("+").skip(1).collect::<Vec<&str>>()[0]
                        .parse::<u64>()
                        .unwrap(),
                    y.split("+").skip(1).collect::<Vec<&str>>()[0]
                        .parse::<u64>()
                        .unwrap(),
                );

                _a = (x, y);
            } else if line.contains("Button B") {
                let parts: Vec<&str> = line.split(": ").collect::<Vec<&str>>()[1]
                    .split(", ")
                    .take(2)
                    .collect();
                let (x, y) = (parts[0], parts[1]);

                let (x, y) = (
                    x.split("+").skip(1).collect::<Vec<&str>>()[0]
                        .parse::<u64>()
                        .unwrap(),
                    y.split("+").skip(1).collect::<Vec<&str>>()[0]
                        .parse::<u64>()
                        .unwrap(),
                );

                _b = (x, y);
            } else if line.contains("Prize") {
                let parts: Vec<&str> = line.split(": ").collect::<Vec<&str>>()[1]
                    .split(", ")
                    .take(2)
                    .collect();
                let (x, y) = (parts[0], parts[1]);

                let (x, y) = (
                    x.split("=").skip(1).collect::<Vec<&str>>()[0]
                        .parse::<u64>()
                        .unwrap(),
                    y.split("=").skip(1).collect::<Vec<&str>>()[0]
                        .parse::<u64>()
                        .unwrap(),
                );

                _p = (x + 10000000000000, y + 10000000000000);
            }
        }
        machines.push([_a, _b, _p]);

        let mut cost: u64 = 0;

        for [(x1, y1), (x2, y2), (x3, y3)] in machines {
            let x1 = x1 as i64;
            let y1 = y1 as i64;
            let x2 = x2 as i64;
            let y2 = y2 as i64;
            let x3 = x3 as i64;
            let y3 = y3 as i64;

            let det: i64 = x1 * y2 - x2 * y1;
            if det != 0 {
                let det_a: i64 = x3 * y2 - x2 * y3;
                let det_b: i64 = x1 * y3 - x3 * y1;

                let a: i64 = det_a / det;
                let b: i64 = det_b / det;

                if det_a % det == 0 && det_b % det == 0 && a >= 0 && b >= 0 {
                    let total_cost = a * 3 + b;
                    if total_cost > 0 {
                        cost += total_cost as u64;
                    }
                }
            }
        }

        cost
    }

    fn get_day(&self) -> u8 {
        self.day.day
    }
}

pub fn run() {
    Day13::new().solve();
}
