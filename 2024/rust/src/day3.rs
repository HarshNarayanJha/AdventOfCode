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
        let instruction = input.lines().collect::<String>();

        let mul_pat = Regex::new(r"mul\((\d+),(\d+)\)").unwrap();

        mul_pat
            .captures_iter(&instruction)
            .map(|c| c.extract())
            .map(|(_, [num1, num2])| num1.parse::<u32>().unwrap() * num2.parse::<u32>().unwrap())
            .sum()
    }

    fn part2(&self) -> u32 {
        let input = include_str!("../../data/input3.txt");
        let instruction = input.lines().collect::<String>();

        let mul_pat = Regex::new(r"(mul\((\d+),(\d+)\))|(do\(\))|(don\'t\(\))").unwrap();

        mul_pat
            .captures_iter(&instruction)
            .fold((0, true), |(result, enabled), m| {
                let captures = m.iter().filter_map(|x| x).collect::<Vec<_>>();

                match captures.len() {
                    4 if enabled => {
                        let num1 = captures[2].as_str().parse::<u32>().unwrap();
                        let num2 = captures[3].as_str().parse::<u32>().unwrap();
                        (result + num1 * num2, enabled)
                    }
                    2 => (result, captures[0].as_str() == "do()"),
                    _ => (result, enabled),
                }
            })
            .0
    }

    fn get_day(&self) -> u32 {
        self.day.day
    }
}

pub fn run() {
    Day3::new().solve();
}
