use std::collections::HashMap;

use crate::day::{Day, Solution};

pub struct Day7 {
    day: Day,
}

impl Day7 {
    pub fn new() -> Self {
        Self { day: Day::new(7) }
    }
}

impl Solution for Day7 {
    fn part1(&self) -> u64 {
        let input = include_str!("../../data/input7.txt");

        let equations: HashMap<u64, Vec<u64>> = input
            .lines()
            .map(|line| {
                let split = line.split(':').collect::<Vec<&str>>();
                (
                    split[0].parse::<u64>().unwrap(),
                    split[1]
                        .split_whitespace()
                        .map(|x| x.parse::<u64>().unwrap())
                        .collect::<Vec<u64>>(),
                )
            })
            .collect();

        let operators = vec!['+', '*'];
        let mut true_sum = 0;

        for (result, values) in equations {
            let count = values.len() - 1;
            let mut found = false;

            let op_combs = (0..count).fold(vec![vec![]], |acc, _| {
                let mut new_comb = Vec::new();
                for combination in acc {
                    for &operator in &operators {
                        let mut new_combination = combination.clone();
                        new_combination.push(operator);
                        new_comb.push(new_combination);
                    }
                }
                new_comb
            });

            for op_combo in op_combs {
                let mut curr = values[0];
                for (i, op) in op_combo.iter().enumerate() {
                    if op == &'+' {
                        curr += values[i + 1]
                    } else if op == &'*' {
                        curr *= values[i + 1]
                    }
                }

                if curr == result {
                    found = true;
                    break;
                }
            }

            if found {
                true_sum += result;
            }
        }

        true_sum
    }

    fn part2(&self) -> u64 {
        let input = include_str!("../../data/input7.txt");

        let equations: HashMap<u64, Vec<u64>> = input
            .lines()
            .map(|line| {
                let split = line.split(':').collect::<Vec<&str>>();
                (
                    split[0].parse::<u64>().unwrap(),
                    split[1]
                        .split_whitespace()
                        .map(|x| x.parse::<u64>().unwrap())
                        .collect::<Vec<u64>>(),
                )
            })
            .collect();

        let operators = vec!['+', '*', '|'];
        let mut true_sum = 0;

        for (result, values) in equations {
            let count = values.len() - 1;
            let mut found = false;

            let op_combs = (0..count).fold(vec![vec![]], |acc, _| {
                let mut new_comb = Vec::new();
                for combination in acc {
                    for &operator in &operators {
                        let mut new_combination = combination.clone();
                        new_combination.push(operator);
                        new_comb.push(new_combination);
                    }
                }
                new_comb
            });

            for op_combo in op_combs {
                let mut curr = values[0];
                for (i, op) in op_combo.iter().enumerate() {
                    if op == &'+' {
                        curr += values[i + 1]
                    } else if op == &'*' {
                        curr *= values[i + 1]
                    } else if op == &'|' {
                        curr = curr * (10_u64.pow(values[i + 1].ilog10() + 1)) + values[i + 1]
                    }
                }

                if curr == result {
                    found = true;
                    break;
                }
            }

            if found {
                true_sum += result;
            }
        }

        true_sum
    }

    fn get_day(&self) -> u8 {
        self.day.day
    }
}

pub fn run() {
    Day7::new().solve();
}
