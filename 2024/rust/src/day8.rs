use std::collections::{BTreeMap, BTreeSet};

use crate::day::{Day, Solution};

pub struct Day8 {
    day: Day,
}

impl Day8 {
    pub fn new() -> Self {
        Self { day: Day::new(8) }
    }
}

fn get_two_antinodes(p1: &(u32, u32), p2: &(u32, u32)) -> ((u32, u32), (u32, u32)) {
    let (x1, y1) = p1;
    let (x2, y2) = p2;
    let dx = x2 - x1;
    let dy = y2 - y1;
    let a1 = (x1 - dx, y1 - dy);
    let a2 = (x2 + dx, y2 + dy);

    (a1, a2)
}

impl Solution for Day8 {
    fn part1(&self) -> u64 {
        let input = include_str!("../../data/input8.txt");

        let mut antennas: BTreeMap<char, Vec<(u32, u32)>> = BTreeMap::default();

        let h = input.lines().count() as u32;
        let w = input.lines().next().unwrap().len() as u32;

        for (i, line) in input.lines().enumerate() {
            for (j, c) in line.chars().enumerate() {
                if c == '.' {
                    continue;
                }
                antennas
                    .entry(c)
                    .and_modify(|points| points.push((i as u32, j as u32)))
                    .or_insert(vec![(i as u32, j as u32)]);
            }
        }

        let mut antinodes: BTreeSet<(u32, u32)> = BTreeSet::default();

        for (_antenna, points) in antennas.iter() {
            let mut pairs: BTreeSet<((u32, u32), (u32, u32))> = BTreeSet::default();

            for i in 0..points.len() {
                for j in i + 1..points.len() {
                    if i == j {
                        continue;
                    }
                    pairs.insert((points[i], points[j]));
                }
            }

            for (a, b) in pairs.iter() {
                let (a1, a2) = get_two_antinodes(a, b);

                if a1.0 < h && a1.1 < w {
                    antinodes.insert(a1);
                }
                if a2.0 < h && a2.1 < w {
                    antinodes.insert(a2);
                }
            }
        }

        antinodes.len() as u64
    }

    fn part2(&self) -> u64 {
        let input = include_str!("../../data/input8.txt");

        let mut antennas: BTreeMap<char, Vec<(u32, u32)>> = BTreeMap::default();

        let h = input.lines().count() as u32;
        let w = input.lines().next().unwrap().len() as u32;

        for (i, line) in input.lines().enumerate() {
            for (j, c) in line.chars().enumerate() {
                if c == '.' {
                    continue;
                }
                antennas
                    .entry(c)
                    .and_modify(|points| points.push((i as u32, j as u32)))
                    .or_insert(vec![(i as u32, j as u32)]);
            }
        }

        let mut antinodes: BTreeSet<(u32, u32)> = BTreeSet::default();

        for (_antenna, points) in antennas.iter() {
            let mut pairs: BTreeSet<((u32, u32), (u32, u32))> = BTreeSet::default();

            for i in 0..points.len() {
                for j in i + 1..points.len() {
                    if i == j {
                        continue;
                    }
                    pairs.insert((points[i], points[j]));
                }
            }

            for (a, b) in pairs.into_iter() {
                let mut a = a.clone();
                let mut b = b.clone();

                let (mut a1, mut a2) = get_two_antinodes(&a, &b).clone();

                while [a1, a2, a, b].iter().any(|x| x.0 < h && x.1 < w) {
                    if a1.0 < h && a1.1 < w {
                        antinodes.insert(a1);
                    }
                    if a2.0 < h && a2.1 < w {
                        antinodes.insert(a2);
                    }
                    if a.0 < h && a.1 < w {
                        antinodes.insert(a);
                    }
                    if b.0 < h && b.1 < w {
                        antinodes.insert(b);
                    }

                    let new_a1 = get_two_antinodes(&a1, &a).0;
                    a = a1;
                    a1 = new_a1;
                    let new_a2 = get_two_antinodes(&b, &a2).1;
                    b = a2;
                    a2 = new_a2;
                }
            }
        }

        antinodes.len() as u64
    }

    fn get_day(&self) -> u8 {
        self.day.day
    }
}

pub fn run() {
    Day8::new().solve();
}
