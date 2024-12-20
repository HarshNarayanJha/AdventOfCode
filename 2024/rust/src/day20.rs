use crate::day::{Day, Solution};

pub struct Day20 {
    day: Day,
}

impl Day20 {
    pub fn new() -> Self {
        Self { day: Day::new(20) }
    }
}

impl Solution for Day20 {
    fn part1(&self) -> u64 {
        let input = include_str!("../../data/input20.txt");

        0
    }

    fn part2(&self) -> u64 {
        let input = include_str!("../../data/input20.txt");

        0
    }

    fn get_day(&self) -> u8 {
        self.day.day
    }
}

pub fn run() {
    Day20::new().solve();
}
