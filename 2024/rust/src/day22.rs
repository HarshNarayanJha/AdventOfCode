use crate::day::{Day, Solution};

pub struct Day22 {
    day: Day,
}

impl Day22 {
    pub fn new() -> Self {
        Self { day: Day::new(22) }
    }
}

impl Solution for Day22 {
    fn part1(&self) -> u64 {
        let input = include_str!("../../data/input22.txt");

        0
    }

    fn part2(&self) -> u64 {
        let input = include_str!("../../data/input22.txt");

        0
    }

    fn get_day(&self) -> u8 {
        self.day.day
    }
}

pub fn run() {
    Day22::new().solve();
}
