use crate::day::{Day, Solution};

pub struct Day18 {
    day: Day,
}

impl Day18 {
    pub fn new() -> Self {
        Self { day: Day::new(18) }
    }
}

impl Solution for Day18 {
    fn part1(&self) -> u64 {
        let input = include_str!("../../data/input18.txt");

        0
    }

    fn part2(&self) -> u64 {
        let input = include_str!("../../data/input18.txt");

        0
    }

    fn get_day(&self) -> u8 {
        self.day.day
    }
}

pub fn run() {
    Day18::new().solve();
}
