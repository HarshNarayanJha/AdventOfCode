use std::collections::HashMap;

use crate::day::{Day, Solution};

pub struct Day19 {
    day: Day,
}

impl Day19 {
    pub fn new() -> Self {
        Self { day: Day::new(19) }
    }
}

impl Solution for Day19 {
    fn part1(&self) -> u64 {
        let input = include_str!("../../data/input19.txt");

        let availables: Vec<&str> = input
            .lines()
            .take(1)
            .flat_map(|line| line.split(", ").collect::<Vec<&str>>())
            .collect();
        let to_makes: Vec<&str> = input.lines().skip(2).map(|line| line).collect();

        let mut count = 0;
        let mut dp: HashMap<String, u64> = HashMap::default();

        fn ways(words: &Vec<&str>, target: &str, dp: &mut HashMap<String, u64>) -> u64 {
            if dp.contains_key(target) {
                return dp[target];
            }

            let mut ans = if target.is_empty() { 1 } else { 0 };

            for word in words {
                if target.starts_with(word) {
                    ans += ways(words, &target[word.len()..], dp);
                }
            }

            dp.insert(target.to_string(), ans);
            ans
        }

        for make in to_makes {
            count += if ways(&availables, make, &mut dp) > 0 {
                1
            } else {
                0
            };
        }

        count
    }

    fn part2(&self) -> u64 {
        let input = include_str!("../../data/input19.txt");

        let availables: Vec<&str> = input
            .lines()
            .take(1)
            .flat_map(|line| line.split(", ").collect::<Vec<&str>>())
            .collect();
        let to_makes: Vec<&str> = input.lines().skip(2).map(|line| line).collect();

        let mut count = 0;
        let mut dp: HashMap<String, u64> = HashMap::default();

        fn ways(words: &Vec<&str>, target: &str, dp: &mut HashMap<String, u64>) -> u64 {
            if dp.contains_key(target) {
                return dp[target];
            }

            let mut ans = if target.is_empty() { 1 } else { 0 };

            for word in words {
                if target.starts_with(word) {
                    ans += ways(words, &target[word.len()..], dp);
                }
            }

            dp.insert(target.to_string(), ans);
            ans
        }

        for make in to_makes {
            count += ways(&availables, make, &mut dp);
        }

        count
    }

    fn get_day(&self) -> u8 {
        self.day.day
    }
}

pub fn run() {
    Day19::new().solve();
}
