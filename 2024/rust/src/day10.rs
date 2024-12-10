use std::collections::HashSet;

use crate::day::{Day, Solution};

pub struct Day10 {
    day: Day,
}

impl Day10 {
    pub fn new() -> Self {
        Self { day: Day::new(10) }
    }
}

impl Solution for Day10 {
    fn part1(&self) -> u64 {
        let input = include_str!("../../data/input10.txt");

        let grid: Vec<Vec<u32>> = input
            .lines()
            .map(|l| l.chars().map(|c| c.to_digit(10).unwrap()).collect())
            .collect();

        let trailheads: HashSet<(usize, usize)> = grid
            .iter()
            .enumerate()
            .flat_map(|(i, r)| {
                r.iter()
                    .enumerate()
                    .filter(|(_, &c)| c == 0)
                    .map(move |(j, _)| (i, j))
            })
            .collect();

        let tops: HashSet<(usize, usize)> = grid
            .iter()
            .enumerate()
            .flat_map(|(i, r)| {
                r.iter()
                    .enumerate()
                    .filter(|(_, &c)| c == 9)
                    .map(move |(j, _)| (i, j))
            })
            .collect();

        let directions: HashSet<(i32, i32)> =
            vec![(0, 1), (1, 0), (0, -1), (-1, 0)].into_iter().collect();

        let mut score = 0;

        let h = grid.len() as i32;
        let w = grid[0].len() as i32;

        trailheads.iter().for_each(|&trailhead| {
            let mut seen = HashSet::new();
            let mut stack = vec![trailhead];

            while !stack.is_empty() {
                let pt = stack.pop().unwrap();
                let (x, y) = pt;

                if tops.contains(&pt) && !seen.contains(&pt) {
                    score += 1;
                    seen.insert(pt);
                }

                directions.iter().for_each(|&(dx, dy)| {
                    let (new_x, new_y) = (x as i32 + dx, y as i32 + dy);

                    if 0 <= new_x
                        && new_x < h
                        && 0 <= new_y
                        && new_y < w
                        && grid[new_x as usize][new_y as usize] == grid[x][y] + 1
                    {
                        stack.push((new_x as usize, new_y as usize))
                    }
                });
            }
        });

        score
    }

    fn part2(&self) -> u64 {
        let input = include_str!("../../data/input10.txt");

        let grid: Vec<Vec<u32>> = input
            .lines()
            .map(|l| l.chars().map(|c| c.to_digit(10).unwrap()).collect())
            .collect();

        let trailheads: HashSet<(usize, usize)> = grid
            .iter()
            .enumerate()
            .flat_map(|(i, r)| {
                r.iter()
                    .enumerate()
                    .filter(|(_, &c)| c == 0)
                    .map(move |(j, _)| (i, j))
            })
            .collect();

        let tops: HashSet<(usize, usize)> = grid
            .iter()
            .enumerate()
            .flat_map(|(i, r)| {
                r.iter()
                    .enumerate()
                    .filter(|(_, &c)| c == 9)
                    .map(move |(j, _)| (i, j))
            })
            .collect();

        let directions: HashSet<(i32, i32)> =
            vec![(0, 1), (1, 0), (0, -1), (-1, 0)].into_iter().collect();

        let mut rating = 0;

        let h = grid.len() as i32;
        let w = grid[0].len() as i32;

        trailheads.into_iter().for_each(|trailhead| {
            let mut stack = vec![trailhead];

            while !stack.is_empty() {
                let pt = stack.pop().unwrap();
                let (x, y) = pt;

                if tops.contains(&pt) {
                    rating += 1;
                }

                directions.iter().for_each(|&(dx, dy)| {
                    let (new_x, new_y) = (x as i32 + dx, y as i32 + dy);

                    if 0 <= new_x
                        && new_x < h
                        && 0 <= new_y
                        && new_y < w
                        && grid[new_x as usize][new_y as usize] == grid[x][y] + 1
                    {
                        stack.push((new_x as usize, new_y as usize))
                    }
                });
            }
        });

        rating
    }

    fn get_day(&self) -> u8 {
        self.day.day
    }
}

pub fn run() {
    Day10::new().solve();
}
