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
                let (result, values) = line.split_once(':').unwrap();
                (
                    result.parse().unwrap(),
                    values
                        .split_whitespace()
                        .filter_map(|x| x.parse().ok())
                        .collect(),
                )
            })
            .collect();

        let operators = ['+', '*'];

        equations
            .into_iter()
            .filter(|&(result, ref values)| {
                let count = values.len() - 1;
                let op_combinations = (0..count).fold(vec![vec![]], |acc, _| {
                    acc.into_iter()
                        .flat_map(|combination| {
                            operators.iter().map(move |&op| {
                                let mut new_combination = combination.clone();
                                new_combination.push(op);
                                new_combination
                            })
                        })
                        .collect()
                });

                op_combinations.into_iter().any(|ops| {
                    let value = ops
                        .iter()
                        .enumerate()
                        .fold(values[0], |acc, (i, &op)| match op {
                            '+' => acc + values[i + 1],
                            '*' => acc * values[i + 1],
                            _ => unreachable!(),
                        });
                    value == result
                })
            })
            .map(|(result, _)| result)
            .sum()
    }

    fn part2(&self) -> u64 {
        let input = include_str!("../../data/input7.txt");

        let equations: HashMap<u64, Vec<u64>> = input
            .lines()
            .map(|line| {
                let (result, values) = line.split_once(':').unwrap();
                (
                    result.parse().unwrap(),
                    values
                        .split_whitespace()
                        .filter_map(|x| x.parse().ok())
                        .collect(),
                )
            })
            .collect();

        let operators = ['+', '*', '|'];

        equations
            .into_iter()
            .filter(|&(result, ref values)| {
                let count = values.len() - 1;

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

                op_combs.into_iter().any(|ops| {
                    let value = ops
                        .iter()
                        .enumerate()
                        .fold(values[0], |acc, (i, &op)| match op {
                            '+' => acc + values[i + 1],
                            '*' => acc * values[i + 1],
                            '|' => acc * (10_u64.pow(values[i + 1].ilog10() + 1)) + values[i + 1],
                            _ => unreachable!(),
                        });
                    value == result
                })
            })
            .map(|(result, _)| result)
            .sum()
    }

    fn get_day(&self) -> u8 {
        self.day.day
    }
}

pub fn run() {
    Day7::new().solve();
}
