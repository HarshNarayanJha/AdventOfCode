use std::collections::{BinaryHeap, HashSet};

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

        let bcoords: Vec<(u64, u64)> = input
            .lines()
            .map(|line| {
                let parts: Vec<&str> = line.split(",").collect();
                (
                    parts[0].parse::<u64>().unwrap(),
                    parts[1].parse::<u64>().unwrap(),
                )
            })
            .collect();

        let grid_size = 71;
        let to_sim = 1024;

        let (sx, sy) = (0u64, 0u64);
        let (ex, ey) = (grid_size - 1, grid_size - 1);

        let mut seen: HashSet<(u64, u64, u8)> = HashSet::default();
        let mut pq: BinaryHeap<(i64, (u64, u64), u8)> = BinaryHeap::from([(-0, (sx, sy), 0)]);
        let mut least_steps = 0;

        let blocks: HashSet<(u64, u64)> = HashSet::from_iter(bcoords[0..to_sim].iter().cloned());

        while !pq.is_empty() {
            let (cost, (cx, cy), dir) = pq.pop().unwrap();

            if (cx, cy) == (ex, ey) {
                least_steps = -cost;
                break;
            }
            if seen.contains(&(cx, cy, dir)) {
                continue;
            }
            seen.insert((cx, cy, dir));

            let dx = [0, 1, 0, -1][dir as usize];
            let dy = [1, 0, -1, 0][dir as usize];
            let (nx, ny) = (cx as i32 + dx, cy as i32 + dy);

            if nx >= 0 && nx < grid_size as i32 && ny >= 0 && ny < grid_size as i32 {
                if !blocks.contains(&(nx as u64, ny as u64)) {
                    pq.push((cost - 1, (nx as u64, ny as u64), dir));
                }
            }

            let new_dir = (dir - 1).rem_euclid(4);
            pq.push((cost, (cx, cy), new_dir));

            let new_dir = (dir + 1).rem_euclid(4);
            pq.push((cost, (cx, cy), new_dir));
        }

        least_steps as u64
    }

    fn part2(&self) -> u64 {
        let input = include_str!("../../data/input18.txt");

        let bcoords: Vec<(u64, u64)> = input
            .lines()
            .map(|line| {
                let parts: Vec<&str> = line.split(",").collect();
                (
                    parts[0].parse::<u64>().unwrap(),
                    parts[1].parse::<u64>().unwrap(),
                )
            })
            .collect();

        let grid_size = 71;
        let to_sim = 1024;

        let mut pi = to_sim;
        let mut qj = bcoords.len() - 1;

        while pi < qj {
            let m = pi + (qj - pi) / 2;

            let (sx, sy) = (0u64, 0u64);
            let (ex, ey) = (grid_size - 1, grid_size - 1);

            let mut seen: HashSet<(u64, u64, u8)> = HashSet::default();
            let mut pq: BinaryHeap<(i64, (u64, u64), u8)> = BinaryHeap::from([(-0, (sx, sy), 0)]);
            let mut least_steps = 0;

            let blocks: HashSet<(u64, u64)> = HashSet::from_iter(bcoords[0..m].iter().cloned());

            while !pq.is_empty() {
                let (cost, (cx, cy), dir) = pq.pop().unwrap();

                if (cx, cy) == (ex, ey) {
                    least_steps = -cost;
                    break;
                }
                if seen.contains(&(cx, cy, dir)) {
                    continue;
                }
                seen.insert((cx, cy, dir));

                let dx = [0, 1, 0, -1][dir as usize];
                let dy = [1, 0, -1, 0][dir as usize];
                let (nx, ny) = (cx as i32 + dx, cy as i32 + dy);

                if nx >= 0 && nx < grid_size as i32 && ny >= 0 && ny < grid_size as i32 {
                    if !blocks.contains(&(nx as u64, ny as u64)) {
                        pq.push((cost - 1, (nx as u64, ny as u64), dir));
                    }
                }

                let new_dir = (dir - 1).rem_euclid(4);
                pq.push((cost, (cx, cy), new_dir));

                let new_dir = (dir + 1).rem_euclid(4);
                pq.push((cost, (cx, cy), new_dir));
            }

            if least_steps == 0 {
                qj = m - 1;
            } else {
                pi = m + 1;
            }
        }

        assert_eq!(qj, pi);

        println!("{:?}", bcoords[pi - 1]);

        0
    }

    fn get_day(&self) -> u8 {
        self.day.day
    }
}

pub fn run() {
    Day18::new().solve();
}
