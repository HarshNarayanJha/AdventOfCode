use crate::day::{Day, Solution};

pub struct Day6 {
    day: Day,
}

impl Day6 {
    pub fn new() -> Self {
        Self { day: Day::new(6) }
    }
}

impl Solution for Day6 {
    fn part1(&self) -> u32 {
        let input = include_str!("../../data/input6.txt");

        let mut start: (i32, i32) = (0, 0);
        let maze: Vec<Vec<char>> = input
            .lines()
            .enumerate()
            .map(|(i, line)| {
                if line.contains('^') {
                    start = (i as i32, line.find('^').unwrap() as i32);
                }
                line.chars().collect()
            })
            .collect();

        let (mut dx, mut dy) = (-1, 0);
        let mut current = start;
        let mut visited: Vec<(i32, i32)> = vec![];
        visited.push(current);

        loop {
            let (tx, ty) = (current.0 + dx, current.1 + dy);
            if !(tx >= 0 && tx < maze.len() as i32 && ty >= 0 && ty < maze[0].len() as i32) {
                break;
            }

            if maze[tx as usize][ty as usize] == '#' {
                (dx, dy) = (dy, -dx);
            } else {
                current = (tx, ty);
                if !visited.contains(&current) {
                    visited.push(current);
                }
            }
        }

        visited.len() as u32
    }

    fn part2(&self) -> u32 {
        let input = include_str!("../../data/input6.txt");

        let mut start: (i32, i32) = (0, 0);
        let maze: Vec<Vec<char>> = input
            .lines()
            .enumerate()
            .map(|(i, line)| {
                if line.contains('^') {
                    start = (i as i32, line.find('^').unwrap() as i32);
                }
                line.chars().collect()
            })
            .collect();

        let mut loop_walls = 0;

        for (i, line) in maze.iter().enumerate() {
            for (j, _c) in line.iter().enumerate() {
                if maze[i][j] == '^' {
                    continue;
                }

                if maze[i][j] == '#' {
                    continue;
                }

                let new_wall = (i as i32, j as i32);

                let (mut dx, mut dy) = (-1, 0);
                let mut current = start;
                let mut visited: Vec<((i32, i32), (i32, i32))> = vec![];
                visited.push(((dx, dy), current));

                loop {
                    let (tx, ty) = (current.0 + dx, current.1 + dy);
                    if !(tx >= 0 && tx < maze.len() as i32 && ty >= 0 && ty < maze[0].len() as i32)
                    {
                        break;
                    }

                    if maze[tx as usize][ty as usize] == '#' {
                        (dx, dy) = (dy, -dx);
                    } else if (tx, ty) == new_wall {
                        (dx, dy) = (dy, -dx);
                    } else {
                        current = (tx, ty);
                        if visited.contains(&((dx, dy), current)) {
                            loop_walls += 1;
                            break;
                        }
                        visited.push(((dx, dy), current));
                    }
                }
            }
        }

        loop_walls
    }

    fn get_day(&self) -> u32 {
        self.day.day
    }
}

pub fn run() {
    Day6::new().solve();
}
