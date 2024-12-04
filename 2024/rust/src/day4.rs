use std::collections::HashSet;

use crate::day::{Day, Solution};

pub struct Day4 {
    day: Day,
}

impl Day4 {
    pub fn new() -> Self {
        Self { day: Day::new(4) }
    }
}

impl Solution for Day4 {
    fn part1(&self) -> u32 {
        let input = include_str!("../../data/input4.txt");
        let grid: Vec<Vec<char>> = input.lines().map(|line| line.chars().collect()).collect();

        let directions: Vec<(i32, i32)> = (-1..=1)
            .flat_map(|dx| (-1..=1).map(move |dy| (dx, dy)))
            .filter(|&(dx, dy)| dx != 0 || dy != 0)
            .collect();

        let n = grid.len();

        let mut count = 0;

        let mut valid_coords: HashSet<(i32, i32)> = HashSet::with_capacity(n * 2);

        for m in 0..n {
            for n in 0..n {
                valid_coords.insert((m as i32, n as i32));
            }
        }

        for x in 0..n {
            for y in 0..n {
                for (dx, dy) in &directions {
                    if !valid_coords.contains(&(x as i32 + dx * 3, y as i32 + dy * 3)) {
                        continue;
                    }

                    let word: String = (0..4)
                        .map(|n| grid[x + *dx as usize * n][y + *dy as usize * n])
                        .collect();

                    if word == "XMAS" {
                        count += 1;
                    }
                }
            }
        }

        count
    }

    fn part2(&self) -> u32 {
        let input = include_str!("../../data/input4.txt");

        0
    }

    fn get_day(&self) -> u32 {
        self.day.day
    }
}

pub fn run() {
    Day4::new().solve();
}
