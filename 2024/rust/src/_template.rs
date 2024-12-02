use crate::day::{Day, Solution};

pub struct DayN {
    day: Day,
}

impl DayN {
    pub fn new() -> Self {
        Self { day: Day::new(N) }
    }
}

impl Solution for DayN {
    fn part1(&self) -> u32 {
        let input = include_str!("../../data/inputN.txt");

        0
    }

    fn part2(&self) -> u32 {
        let input = include_str!("../../data/inputN.txt");

        0
    }

    fn get_day(&self) -> u32 {
        self.day.day
    }
}

pub fn run() {
    DayN::new().solve();
}
