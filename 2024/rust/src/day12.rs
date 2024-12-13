use std::collections::{HashMap, HashSet};

use crate::day::{Day, Solution};

pub struct Day12 {
    day: Day,
}

impl Day12 {
    pub fn new() -> Self {
        Self { day: Day::new(12) }
    }
}

impl Solution for Day12 {
    fn part1(&self) -> u64 {
        let input = include_str!("../../data/input12.txt");

        let grid = input
            .lines()
            .map(|x| x.chars().collect::<Vec<char>>())
            .collect::<Vec<Vec<char>>>();

        let h = grid.len();
        let w = grid[0].len();

        let mut regions: HashMap<u32, Vec<(usize, usize)>> = HashMap::default();
        let mut visited: HashSet<(usize, usize)> = HashSet::default();
        let mut component_id = 0_u32;

        for i in 0..h {
            for j in 0..w {
                if visited.contains(&(i, j)) {
                    continue;
                }

                let mut component: Vec<(usize, usize)> = vec![];
                let mut stack: Vec<(usize, usize)> = vec![(i, j)];

                while !stack.is_empty() {
                    let c = stack.pop().unwrap();

                    if visited.contains(&c) {
                        continue;
                    }

                    visited.insert(c);
                    component.push(c);

                    for n in [
                        (c.0 - 1, c.1),
                        (c.0 + 1, c.1),
                        (c.0, c.1 - 1),
                        (c.0, c.1 + 1),
                    ] {
                        if n.0 < h && n.1 < w {
                            if grid[i][j] == grid[n.0][n.1] && !visited.contains(&n) {
                                stack.push(n);
                            }
                        }
                    }
                }

                regions.insert(component_id, component);
                component_id += 1;
            }
        }

        let mut cost = 0_u64;

        for (_r, span) in regions {
            let area = span.len();
            let mut perimeter = 0;

            for (i, j) in span.iter() {
                for n in [(i - 1, j), (i + 1, j), (*i, &(j - 1)), (*i, &(j + 1))] {
                    if !span.contains(&(n.0, *n.1)) {
                        perimeter += 1;
                    }
                }
            }

            cost += area as u64 * perimeter as u64;
        }

        cost
    }

    fn part2(&self) -> u64 {
        let input = include_str!("../../data/input12.txt");

        let grid = input
            .lines()
            .map(|x| x.chars().collect::<Vec<char>>())
            .collect::<Vec<Vec<char>>>();

        let h = grid.len();
        let w = grid[0].len();

        let mut regions: HashMap<u32, Vec<(usize, usize)>> = HashMap::default();
        let mut visited: HashSet<(usize, usize)> = HashSet::default();
        let mut component_id = 0_u32;

        for i in 0..h {
            for j in 0..w {
                if visited.contains(&(i, j)) {
                    continue;
                }

                let mut component: Vec<(usize, usize)> = vec![];
                let mut stack: Vec<(usize, usize)> = vec![(i, j)];

                while !stack.is_empty() {
                    let c = stack.pop().unwrap();

                    if visited.contains(&c) {
                        continue;
                    }

                    visited.insert(c);
                    component.push(c);

                    for n in [
                        (c.0 - 1, c.1),
                        (c.0 + 1, c.1),
                        (c.0, c.1 - 1),
                        (c.0, c.1 + 1),
                    ] {
                        if n.0 < h && n.1 < w {
                            if grid[i][j] == grid[n.0][n.1] && !visited.contains(&n) {
                                stack.push(n);
                            }
                        }
                    }
                }

                regions.insert(component_id, component);
                component_id += 1;
            }
        }

        let mut cost = 0_u64;

        for (_r, span) in regions {
            let area = span.len();
            let mut perimeter: Vec<((usize, usize), (usize, usize))> = vec![];

            for (i, j) in span.iter() {
                for n in [(i - 1, j), (i + 1, j), (*i, &(j - 1)), (*i, &(j + 1))] {
                    if !span.contains(&(n.0, *n.1)) {
                        perimeter.push(((*i, *j), (n.0, *n.1)));
                    }
                }
            }

            let mut sides: Vec<((usize, usize), (usize, usize))> = vec![];

            for (pi, pj) in perimeter.iter() {
                let mut remove = false;

                for (ci, cj) in [(0, 1), (1, 0)] {
                    let ni = (pi.0 + ci, pi.1 + cj);
                    let nj = (pj.0 + ci, pj.1 + cj);

                    let edge = (ni, nj);
                    if perimeter.contains(&edge) {
                        remove = true;
                    }
                }

                if !remove {
                    sides.push((*pi, *pj));
                }
            }

            cost += area as u64 * sides.len() as u64;
        }

        cost
    }

    fn get_day(&self) -> u8 {
        self.day.day
    }
}

pub fn run() {
    Day12::new().solve();
}
