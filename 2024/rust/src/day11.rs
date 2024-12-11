use std::collections::HashMap;

use crate::day::{Day, Solution};

pub struct Day11 {
    day: Day,
}

impl Day11 {
    pub fn new() -> Self {
        Self { day: Day::new(11) }
    }
}

impl Solution for Day11 {
    fn part1(&self) -> u64 {
        let input = include_str!("../../data/input11.txt");
        let line = input
            .split_whitespace()
            .map(|x| x.parse::<u64>().unwrap())
            .collect::<Vec<u64>>();

        let blinks = 25;
        let mut counts: HashMap<u64, u64> = HashMap::new();
        counts.reserve(line.len());
        for k in line {
            counts.entry(k).and_modify(|e| *e += 1).or_insert(1);
        }

        for _ in 0..blinks {
            let mut new_counts: HashMap<u64, u64> = HashMap::new();
            new_counts.reserve(counts.len() * 2);
            new_counts.entry(1).or_insert(*counts.get(&0).unwrap_or(&0));

            for (&num, &count) in counts.iter() {
                if num == 0 {
                    continue;
                }

                let mut n = num;
                let mut len = 1;
                while n >= 10 {
                    n /= 10;
                    len += 1;
                }

                if len % 2 == 1 {
                    new_counts
                        .entry(2024 * num)
                        .and_modify(|x| *x += count)
                        .or_insert(count);
                } else {
                    let divisor = 10u64.pow((len / 2) as u32);
                    let right = num % divisor;
                    let left = num / divisor;

                    new_counts
                        .entry(left)
                        .and_modify(|x| *x += count)
                        .or_insert(count);
                    new_counts
                        .entry(right)
                        .and_modify(|x| *x += count)
                        .or_insert(count);
                }
            }

            counts = new_counts;
        }

        counts.values().sum()
    }

    fn part2(&self) -> u64 {
        let input = include_str!("../../data/input11.txt");
        let line = input
            .split_whitespace()
            .map(|x| x.parse::<u64>().unwrap())
            .collect::<Vec<u64>>();

        let blinks = 75;
        let mut counts: HashMap<u64, u64> = HashMap::new();
        counts.reserve(line.len());
        for k in line {
            counts.entry(k).and_modify(|e| *e += 1).or_insert(1);
        }

        for _ in 0..blinks {
            let mut new_counts: HashMap<u64, u64> = HashMap::new();
            new_counts.reserve(counts.len() * 2);
            new_counts.entry(1).or_insert(*counts.get(&0).unwrap_or(&0));

            for (&num, &count) in counts.iter() {
                if num == 0 {
                    continue;
                }

                let mut n = num;
                let mut len = 1;
                while n >= 10 {
                    n /= 10;
                    len += 1;
                }

                if len % 2 == 1 {
                    new_counts
                        .entry(2024 * num)
                        .and_modify(|x| *x += count)
                        .or_insert(count);
                } else {
                    let divisor = 10u64.pow((len / 2) as u32);
                    let right = num % divisor;
                    let left = num / divisor;

                    new_counts
                        .entry(left)
                        .and_modify(|x| *x += count)
                        .or_insert(count);
                    new_counts
                        .entry(right)
                        .and_modify(|x| *x += count)
                        .or_insert(count);
                }
            }

            counts = new_counts;
        }

        counts.values().sum()
    }

    fn get_day(&self) -> u8 {
        self.day.day
    }
}

pub fn run() {
    Day11::new().solve();
}
