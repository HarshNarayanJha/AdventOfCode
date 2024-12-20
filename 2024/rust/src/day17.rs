use std::collections::HashSet;

use crate::day::{Day, Solution};

pub struct Day17 {
    day: Day,
}

impl Day17 {
    pub fn new() -> Self {
        Self { day: Day::new(17) }
    }
}

impl Solution for Day17 {
    fn part1(&self) -> u64 {
        let input = include_str!("../../data/input17.txt");

        let mut ra: u64 = 0;
        let mut rb: u64 = 0;
        let mut rc: u64 = 0;

        input
            .lines()
            .take_while(|line| !line.is_empty())
            .for_each(|line| {
                let parts: Vec<&str> = line.split_whitespace().collect();
                let (reg, val) = (parts[1], parts[2]);
                if reg.contains('A') {
                    ra = val.parse().unwrap();
                } else if reg.contains('B') {
                    rb = val.parse().unwrap();
                } else if reg.contains('C') {
                    rc = val.parse().unwrap();
                }
            });

        let program: Vec<u8> = input
            .lines()
            .skip_while(|line| !line.is_empty())
            .skip(1)
            .flat_map(|line| {
                let program = line.split_whitespace().collect::<Vec<&str>>()[1];
                program.split(',').map(|c| c.parse::<u8>().unwrap())
            })
            .collect();

        let mut ip: usize = 0;
        let mut out: Vec<u64> = Vec::with_capacity(program.len());

        while ip < program.len() - 1 {
            let inst = program[ip];
            let literal_operand = program[ip + 1];
            let combo_operand = match literal_operand {
                0..=3 => literal_operand as u64,
                4 => ra,
                5 => rb,
                6 => rc,
                _ => 0,
            };

            let mut jumped = false;

            match inst {
                0 => ra >>= combo_operand,
                1 => ra ^= literal_operand as u64,
                2 => rb = combo_operand & 7,
                3 if ra != 0 => {
                    jumped = true;
                    ip = literal_operand as usize;
                }
                4 => rb ^= rc,
                5 => out.push(combo_operand & 7),
                6 => rb = ra >> combo_operand,
                7 => rc = rc >> combo_operand,
                _ => {}
            }

            if !jumped {
                ip += 2;
            }
        }

        println!(
            "{}",
            out.iter()
                .map(|n| n.to_string())
                .collect::<Vec<String>>()
                .join(",")
        );

        0
    }

    fn part2(&self) -> u64 {
        let input = include_str!("../../data/input17.txt");

        let program: Vec<u8> = input
            .lines()
            .skip_while(|line| !line.is_empty())
            .skip(1)
            .flat_map(|line| {
                let program = line.split_whitespace().collect::<Vec<&str>>()[1];
                program.split(',').map(|c| c.parse::<u8>().unwrap())
            })
            .collect();

        let mut matching_as: HashSet<u64> = HashSet::from([0]);

        for &expected in program.iter().rev() {
            for a in matching_as.clone() {
                matching_as.remove(&a);

                let a = a * 8;

                for x in 0..8 {
                    let mut ra = a + x;
                    let mut rb = 0;
                    let mut rc = 0;

                    let mut ip: usize = 0;
                    let mut out: Vec<u64> = vec![];

                    while ip < program.len() - 1 {
                        let inst = program[ip];
                        let literal_operand = program[ip + 1];
                        let combo_operand = match literal_operand {
                            0..=3 => literal_operand as u64,
                            4 => ra,
                            5 => rb,
                            6 => rc,
                            _ => 0,
                        };

                        let mut jumped = false;

                        match inst {
                            0 => ra >>= combo_operand,
                            1 => ra ^= literal_operand as u64,
                            2 => rb = combo_operand & 7,
                            3 if ra != 0 => {
                                jumped = true;
                                ip = literal_operand as usize;
                            }
                            4 => rb ^= rc,
                            5 => out.push(combo_operand & 7),
                            6 => rb = ra >> combo_operand,
                            7 => rc = rc >> combo_operand,
                            _ => {}
                        }

                        if !jumped {
                            ip += 2;
                        }
                    }

                    if !out.is_empty() && out[0] == expected as u64 {
                        matching_as.insert(a + x);
                    }
                }
            }
        }

        *matching_as.iter().min().unwrap()
    }

    fn get_day(&self) -> u8 {
        self.day.day
    }
}

pub fn run() {
    Day17::new().solve();
}
