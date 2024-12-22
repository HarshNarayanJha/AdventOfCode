use crate::day::{Day, Solution};

pub struct Day21 {
    day: Day,
}

impl Day21 {
    pub fn new() -> Self {
        Self { day: Day::new(21) }
    }
}

impl Solution for Day21 {
    fn part1(&self) -> u64 {
        let input = include_str!("../../data/input21.txt");

        0
    }

    fn part2(&self) -> u64 {
        let input = include_str!("../../data/input21.txt");

        0
    }

    fn get_day(&self) -> u8 {
        self.day.day
    }
}

pub fn run() {
    Day21::new().solve();
}
