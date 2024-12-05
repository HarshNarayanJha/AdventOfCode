use std::collections::HashMap;

use crate::day::{Day, Solution};

pub struct Day5 {
    day: Day,
}

impl Day5 {
    pub fn new() -> Self {
        Self { day: Day::new(5) }
    }
}

impl Solution for Day5 {
    fn part1(&self) -> u32 {
        let input = include_str!("../../data/input5.txt");

        let mut rules: HashMap<u32, Vec<u32>> = HashMap::new();
        input
            .lines()
            .filter(|line| line.contains('|'))
            .for_each(|line| {
                let parts: Vec<&str> = line.split('|').collect();
                let bef: u32 = parts[0].parse().unwrap();
                let after: u32 = parts[1].parse().unwrap();
                rules.entry(bef).or_insert_with(Vec::new).push(after);
            });

        let orders: Vec<Vec<u32>> = input
            .lines()
            .filter(|line| line.contains(','))
            .map(|line| {
                line.split(',')
                    .map(|page| page.parse::<u32>().unwrap())
                    .collect()
            })
            .collect();

        let mut valids: Vec<u32> = vec![];

        for (o, order) in orders.iter().enumerate() {
            let mut correct_so_far = true;

            for (i, page) in order.iter().enumerate() {
                if !rules.contains_key(&page) {
                    continue;
                }

                if (0..i).map(|x| order[x]).any(|x| rules[page].contains(&x)) {
                    correct_so_far = false;
                    break;
                }
            }

            if correct_so_far {
                valids.push(o as u32);
            }
        }

        valids
            .iter()
            .map(|&o| orders[o as usize][orders[o as usize].len() / 2])
            .sum()
    }

    fn part2(&self) -> u32 {
        let input = include_str!("../../data/input5.txt");

        let mut rules: HashMap<u32, Vec<u32>> = HashMap::new();
        input
            .lines()
            .filter(|line| line.contains('|'))
            .for_each(|line| {
                let parts: Vec<&str> = line.split('|').collect();
                let bef: u32 = parts[0].parse().unwrap();
                let after: u32 = parts[1].parse().unwrap();
                rules.entry(bef).or_insert_with(Vec::new).push(after);
            });

        let mut orders: Vec<Vec<u32>> = input
            .lines()
            .filter(|line| line.contains(','))
            .map(|line| {
                line.split(',')
                    .map(|page| page.parse::<u32>().unwrap())
                    .collect()
            })
            .collect();

        let mut invalids: Vec<u32> = vec![];

        for (o, order) in orders.iter().enumerate() {
            let mut correct_so_far = true;

            for (i, page) in order.iter().enumerate() {
                if !rules.contains_key(&page) {
                    continue;
                }

                if (0..i).map(|x| order[x]).any(|x| rules[page].contains(&x)) {
                    correct_so_far = false;
                    break;
                }
            }

            if !correct_so_far {
                invalids.push(o as u32);
            }
        }

        invalids.iter().for_each(|inv| {
            let order = &mut orders[*inv as usize];
            for _ in 0..order.len() {
                for j in 1..order.len() {
                    if !rules.contains_key(&order[j]) {
                        continue;
                    }

                    if rules[&order[j as usize]].contains(&order[j - 1]) {
                        order.swap(j, j - 1);
                    }
                }
            }
        });

        invalids
            .iter()
            .map(|&o| orders[o as usize][orders[o as usize].len() / 2])
            .sum()
    }

    fn get_day(&self) -> u32 {
        self.day.day
    }
}

pub fn run() {
    Day5::new().solve();
}
