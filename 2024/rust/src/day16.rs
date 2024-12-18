use std::collections::{BinaryHeap, HashSet};

use crate::day::{Day, Solution};

pub struct Day16 {
    day: Day,
}

impl Day16 {
    pub fn new() -> Self {
        Self { day: Day::new(16) }
    }
}

impl Solution for Day16 {
    fn part1(&self) -> u64 {
        let input = include_str!("../../data/input16.txt");

        let maze: Vec<Vec<char>> = input.lines().map(|line| line.chars().collect()).collect();

        let h = maze.len() as i32;
        let w = maze[0].len() as i32;

        let walls: HashSet<(usize, usize)> =
            maze.iter()
                .enumerate()
                .filter_map(|(i, row)| {
                    Some(row.iter().enumerate().filter_map(move |(j, c)| {
                        if *c == '#' {
                            Some((i, j))
                        } else {
                            None
                        }
                    }))
                })
                .flatten()
                .collect();

        let (sx, sy) = maze
            .iter()
            .enumerate()
            .find_map(|(i, row)| row.iter().position(|&x| x == 'S').map(|j| (i, j)))
            .unwrap();

        let (ex, ey) = maze
            .iter()
            .enumerate()
            .find_map(|(i, row)| row.iter().position(|&x| x == 'E').map(|j| (i, j)))
            .unwrap();

        let mut seen: HashSet<(usize, usize, u8)> = HashSet::default();

        let mut pq: BinaryHeap<(i64, (usize, usize), u8)> = BinaryHeap::from([(-0, (sx, sy), 0)]);
        let mut best_cost: u64 = 0;

        while !pq.is_empty() {
            let (cost, (cx, cy), dir) = pq.pop().unwrap();

            if (cx, cy) == (ex, ey) {
                best_cost = (-cost) as u64;
                break;
            }

            if seen.contains(&(cx, cy, dir)) {
                continue;
            }

            seen.insert((cx, cy, dir));

            let dx = [0, 1, 0, -1][dir as usize];
            let dy = [1, 0, -1, 0][dir as usize];
            let (nx, ny) = (cx as i32 + dx, cy as i32 + dy);

            if nx >= 0 && nx < h && ny >= 0 && ny < w {
                if !walls.contains(&(nx as usize, ny as usize)) {
                    pq.push((cost - 1, (nx as usize, ny as usize), dir));
                }
            }

            let new_dir = (dir - 1).rem_euclid(4);
            pq.push((cost - 1000, (cx as usize, cy as usize), new_dir));

            let new_dir = (dir + 1).rem_euclid(4);
            pq.push((cost - 1000, (cx as usize, cy as usize), new_dir));
        }

        best_cost
    }

    fn part2(&self) -> u64 {
        let input = include_str!("../../data/input16.txt");

        0
    }

    fn get_day(&self) -> u8 {
        self.day.day
    }
}

pub fn run() {
    Day16::new().solve();
}
