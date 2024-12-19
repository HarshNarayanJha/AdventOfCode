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

        let mut RA: u64 = 0;
        let mut RB: u64 = 0;
        let mut RC: u64 = 0;

        let _ = input
            .lines()
            .take_while(|line| !line.is_empty())
            .map(|line| {
                let parts: Vec<&str> = line.split_whitespace().collect();
                let (reg, val) = (parts[1], parts[2]);
                if reg.contains('A') {
                    RA = val.parse().unwrap();
                } else if reg.contains('B') {
                    RB = val.parse().unwrap();
                } else if reg.contains('B') {
                    RC = val.parse().unwrap();
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
        let mut out: Vec<u64> = vec![];

        while ip < program.len() - 1 {
            let inst = program[ip];
            let literal_operand = program[ip + 1];
            let combo_operand = match literal_operand {
                0..=3 => literal_operand as u64,
                4 => RA,
                5 => RB,
                6 => RC,
                _ => 0,
            };

            let mut jumped = false;

            match inst {
                0 => RA >>= combo_operand,
                1 => RA ^= literal_operand as u64,
                2 => RB = combo_operand & 7,
                3 if RA != 0 => {
                    jumped = true;
                    ip = literal_operand as usize
                }
                4 => RB ^= RC,
                5 => out.push(combo_operand & 7),
                6 => RB = RA >> combo_operand,
                7 => RC = RC >> combo_operand,
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

        let mut RA: u64 = 0;
        let mut RB: u64 = 0;
        let mut RC: u64 = 0;

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
            for A in matching_as.clone() {
                matching_as.remove(&A);

                let A = A * 8;

                for x in 0..8 {
                    RA = A + x;
                    RB = 0;
                    RC = 0;

                    let mut ip: usize = 0;
                    let mut out: Vec<u64> = vec![];

                    while ip < program.len() - 1 {
                        let inst = program[ip];
                        let literal_operand = program[ip + 1];
                        let combo_operand = match literal_operand {
                            0..=3 => literal_operand as u64,
                            4 => RA,
                            5 => RB,
                            6 => RC,
                            _ => 0,
                        };

                        let mut jumped = false;

                        match inst {
                            0 => RA >>= combo_operand,
                            1 => RA ^= literal_operand as u64,
                            2 => RB = combo_operand & 7,
                            3 if RA != 0 => {
                                jumped = true;
                                ip = literal_operand as usize
                            }
                            4 => RB ^= RC,
                            5 => out.push(combo_operand & 7),
                            6 => RB = RA >> combo_operand,
                            7 => RC = RC >> combo_operand,
                            _ => {}
                        }

                        if !jumped {
                            ip += 2;
                        }
                    }

                    if !out.is_empty() && out[0] == expected as u64 {
                        matching_as.insert(A + x);
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
