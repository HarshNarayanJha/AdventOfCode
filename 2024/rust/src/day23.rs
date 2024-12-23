use std::collections::{HashMap, HashSet};

use crate::day::{Day, Solution};

pub struct Day23 {
    day: Day,
}

impl Day23 {
    pub fn new() -> Self {
        Self { day: Day::new(23) }
    }
}

impl Solution for Day23 {
    fn part1(&self) -> u64 {
        let input = include_str!("../../data/input23.txt");

        let mut csets: HashMap<&str, HashSet<&str>> = HashMap::default();

        for line in input.lines() {
            let parts = line.splitn(2, '-').collect::<Vec<&str>>();
            let (a, b) = (parts[0], parts[1]);
            csets
                .entry(a)
                .and_modify(|set| {
                    set.insert(b);
                })
                .or_insert_with(|| HashSet::from([b]));
            csets
                .entry(b)
                .and_modify(|set| {
                    set.insert(a);
                })
                .or_insert_with(|| HashSet::from([a]));
        }

        let mut count = 0;

        for &p1 in csets.keys() {
            let at = p1.starts_with('t');

            for &p2 in csets[p1].iter() {
                let bt = p2.starts_with('t');

                for &p3 in csets[p2].iter() {
                    if p1 >= p2 || p2 >= p3 || p1 >= p3 {
                        continue;
                    }
                    if !csets[p3].contains(p1) {
                        continue;
                    }

                    let ct = p3.starts_with('t');
                    if at || bt || ct {
                        count += 1;
                    }
                }
            }
        }

        count
    }

    fn part2(&self) -> u64 {
        let input = include_str!("../../data/input23.txt");

        let mut csets: HashMap<&str, HashSet<&str>> = HashMap::default();

        for line in input.lines() {
            let parts = line.splitn(2, '-').collect::<Vec<&str>>();
            let (a, b) = (parts[0], parts[1]);
            csets
                .entry(a)
                .and_modify(|set| {
                    set.insert(b);
                })
                .or_insert_with(|| HashSet::from([b]));
            csets
                .entry(b)
                .and_modify(|set| {
                    set.insert(a);
                })
                .or_insert_with(|| HashSet::from([a]));
        }

        let mut max_group: HashSet<&str> = HashSet::default();

        for &start in csets.keys() {
            let mut visited: HashSet<&str> = HashSet::from([start]);
            let mut to_visit: Vec<&str> = csets[start].iter().cloned().collect();

            while !to_visit.is_empty() {
                let current = to_visit.pop().unwrap();

                if !visited.contains(&current) && visited.iter().all(|x| csets[current].contains(x))
                {
                    visited.insert(current);
                    to_visit.extend(csets[current].iter().filter(|&n| {
                        !visited.contains(n) && visited.iter().all(|x| csets[n].contains(x))
                    }));
                }
            }

            if visited.len() > max_group.len() {
                max_group = visited.clone();
            }
        }

        let mut lan_parties: Vec<&str> = max_group.iter().cloned().collect();
        lan_parties.sort();
        println!("{}", lan_parties.join(","));

        0
    }

    fn get_day(&self) -> u8 {
        self.day.day
    }
}

pub fn run() {
    Day23::new().solve();
}
