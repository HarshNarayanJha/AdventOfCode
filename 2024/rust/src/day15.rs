use std::collections::{HashMap, HashSet};

use crate::day::{Day, Solution};

pub struct Day15 {
    day: Day,
}

impl Day15 {
    pub fn new() -> Self {
        Self { day: Day::new(15) }
    }
}

impl Solution for Day15 {
    fn part1(&self) -> u64 {
        let input = include_str!("../../data/input15.txt");

        let grid: Vec<Vec<char>> = input
            .lines()
            .take_while(|line| !line.is_empty())
            .map(|line| line.chars().collect())
            .collect();

        let h = grid.len();
        let w = grid[0].len();

        let instructions: String = input
            .lines()
            .filter_map(|line| {
                if !line.contains('#') && !line.is_empty() {
                    return Some(line);
                } else {
                    None
                }
            })
            .collect();

        let walls: HashSet<(i32, i32)> = grid
            .iter()
            .enumerate()
            .flat_map(|(i, row)| {
                row.iter().enumerate().filter_map(move |(j, c)| {
                    if *c == '#' {
                        Some((i as i32, j as i32))
                    } else {
                        None
                    }
                })
            })
            .collect();

        let mut boxes: Vec<(i32, i32)> = grid
            .iter()
            .enumerate()
            .flat_map(|(i, row)| {
                row.iter().enumerate().filter_map(move |(j, c)| {
                    if *c == 'O' {
                        Some((i as i32, j as i32))
                    } else {
                        None
                    }
                })
            })
            .collect();

        let (mut x, mut y): (i32, i32) = grid
            .iter()
            .enumerate()
            .flat_map(|(i, row)| {
                row.iter().enumerate().filter_map(move |(j, c)| {
                    if *c == '@' {
                        Some((i as i32, j as i32))
                    } else {
                        None
                    }
                })
            })
            .collect::<Vec<(i32, i32)>>()[0];

        let directions = HashMap::from([
            ('^', (-1, 0)),
            ('<', (0, -1)),
            ('>', (0, 1)),
            ('v', (1, 0)),
        ]);

        for i in instructions.chars() {
            let (dx, dy) = directions.get(&i).unwrap().clone();
            let (nx, ny) = (x + dx, y + dy);

            if walls.contains(&(nx, ny)) {
                continue;
            }

            if !(nx >= 0 && nx < (h as i32) && ny >= 0 && ny < (w as i32)) {
                continue;
            }

            if boxes.contains(&(nx, ny)) {
                let (mut bnx, mut bny) = (nx + dx, ny + dy);

                while boxes.contains(&(bnx, bny)) {
                    (bnx, bny) = (bnx + dx, bny + dy);
                }

                if walls.contains(&(bnx, bny)) {
                    continue;
                }

                if !(bnx >= 0 && bnx < h as i32 && bny >= 0 && bny < w as i32) {
                    continue;
                }

                let (mut tbnx, mut tbny) = (nx, ny);

                while (tbnx, tbny) != (bnx, bny) {
                    let pos = boxes.iter().position(|&x| x == (tbnx, tbny)).unwrap();
                    boxes.remove(pos);
                    (tbnx, tbny) = (tbnx + dx, tbny + dy);
                    boxes.push((tbnx, tbny));
                }
            }

            (x, y) = (nx, ny);
        }

        boxes
            .iter()
            .fold(0, |acc, &(bx, by)| acc + (bx as u64) * 100 + (by as u64))
    }

    fn part2(&self) -> u64 {
        let input = include_str!("../../data/input15.txt");

        let grid: Vec<Vec<char>> = input
            .lines()
            .take_while(|line| !line.is_empty())
            .map(|line| {
                let mut expanded = vec![];
                for c in line.chars() {
                    if c == '#' {
                        expanded.extend_from_slice(&vec!['#', '#']);
                    } else if c == 'O' {
                        expanded.extend_from_slice(&vec!['[', ']']);
                    } else if c == '.' {
                        expanded.extend_from_slice(&vec!['.', '.']);
                    } else if c == '@' {
                        expanded.extend_from_slice(&vec!['@', '.']);
                    }
                }
                expanded
            })
            .collect();

        let instructions: String = input
            .lines()
            .skip_while(|line| !line.is_empty())
            .skip(1)
            .collect();

        let mut boxes: Vec<(i32, i32)> = grid
            .iter()
            .enumerate()
            .flat_map(|(i, row)| {
                row.iter().enumerate().filter_map(move |(j, c)| {
                    if *c == '[' {
                        Some((i as i32, j as i32))
                    } else {
                        None
                    }
                })
            })
            .collect();

        let (mut x, mut y): (i32, i32) = grid
            .iter()
            .enumerate()
            .flat_map(|(i, row)| {
                row.iter().enumerate().filter_map(move |(j, c)| {
                    if *c == '@' {
                        Some((i as i32, j as i32))
                    } else {
                        None
                    }
                })
            })
            .collect::<Vec<(i32, i32)>>()[0];

        let directions = HashMap::from([
            ('^', (-1, 0)),
            ('<', (0, -1)),
            ('>', (0, 1)),
            ('v', (1, 0)),
        ]);

        for i in instructions.chars() {
            let (dx, dy) = directions.get(&i).unwrap().clone();

            let mut to_move = vec![(x, y)];
            let mut i = 0;
            let mut can_move = true;

            while i < to_move.len() {
                let (_x, _y) = to_move[i];
                let (_nx, _ny) = (_x + dx, _y + dy);

                if boxes.contains(&(_nx, _ny)) || boxes.contains(&(_nx, _ny - 1)) {
                    if !to_move.contains(&(_nx, _ny)) {
                        to_move.push((_nx, _ny));
                    }

                    if boxes.contains(&(_nx, _ny)) {
                        if !to_move.contains(&(_nx, _ny + 1)) {
                            to_move.push((_nx, _ny + 1));
                        }
                    }
                    if boxes.contains(&(_nx, _ny - 1)) {
                        if !to_move.contains(&(_nx, _ny - 1)) {
                            to_move.push((_nx, _ny - 1));
                        }
                    }
                } else if grid[_nx as usize][_ny as usize] == '#' {
                    can_move = false;
                    break;
                }

                i += 1;
            }

            if !can_move {
                continue;
            }

            let (nx, ny) = (x + dx, y + dy);

            to_move.retain(|x| boxes.contains(x));

            for &(mx, my) in to_move.iter() {
                if (mx, my) == (x, y) {
                    continue;
                }
                if boxes.contains(&(mx, my)) {
                    boxes.retain(|&x| x != (mx, my));
                    boxes.push((mx + dx, my + dy))
                }
            }

            (x, y) = (nx, ny);
        }

        boxes
            .iter()
            .fold(0, |acc, &(bx, by)| acc + (bx as u64) * 100 + (by as u64))
    }

    fn get_day(&self) -> u8 {
        self.day.day
    }
}

pub fn run() {
    Day15::new().solve();
}
