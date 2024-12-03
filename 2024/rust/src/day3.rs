use crate::day::{Day, Solution};
use regex::Regex;

pub struct Day3 {
    day: Day,
}

impl Day3 {
    pub fn new() -> Self {
        Self { day: Day::new(3) }
    }
}

impl Solution for Day3 {
    fn part1(&self) -> u32 {
        let input = include_str!("../../data/input3.txt");
        let instruction = input.lines().fold(String::new(), |acc, x| acc + x);

        let mul_pat = Regex::new(r"mul\((\d+),(\d+)\)").unwrap();

        let mut results = vec![];
        for (_, [num1, num2]) in mul_pat.captures_iter(&instruction).map(|c| c.extract()) {
            results.push((num1.parse::<u32>().unwrap(), num2.parse::<u32>().unwrap()));
        }

        let result: u32 = results.iter().map(|(a, b)| a * b).sum();

        result
    }

    fn part2(&self) -> u32 {
        let input = include_str!("../../data/input3.txt");

        0
    }

    fn get_day(&self) -> u32 {
        self.day.day
    }
}

pub fn run() {
    Day3::new().solve();
}
