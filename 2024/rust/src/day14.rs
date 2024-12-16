use crate::day::{Day, Solution};

pub struct Day14 {
    day: Day,
}

impl Day14 {
    pub fn new() -> Self {
        Self { day: Day::new(14) }
    }
}

impl Solution for Day14 {
    fn part1(&self) -> u64 {
        let input = include_str!("../../data/input14.txt");

        let mut grid = vec![vec![0u64; 103]; 101];

        input.lines().for_each(|line| {
            let mut parts = line.split_whitespace();
            let p = parts.next().unwrap();
            let v = parts.next().unwrap();

            let mut p_iter = p
                .split('=')
                .nth(1)
                .unwrap()
                .split(',')
                .map(|x| x.parse::<u64>().unwrap());
            let px = p_iter.next().unwrap();
            let py = p_iter.next().unwrap();

            let mut v_iter = v
                .split('=')
                .nth(1)
                .unwrap()
                .split(',')
                .map(|x| x.parse::<i64>().unwrap());
            let vx = v_iter.next().unwrap();
            let vy = v_iter.next().unwrap();

            let px = (px as i64 + vx * 100).rem_euclid(101) as usize;
            let py = (py as i64 + vy * 100).rem_euclid(103) as usize;

            grid[px][py] += 1;
        });

        let w = 101;
        let h = 103;
        let mut factor = 1u64;

        let mut count = 0;
        for i in 0..w / 2 {
            for j in 0..h / 2 {
                count += grid[i][j];
            }
        }
        factor *= count;

        let mut count = 0;
        for i in w / 2 + 1..w {
            for j in 0..h / 2 {
                count += grid[i][j];
            }
        }
        factor *= count;

        let mut count = 0;
        for i in 0..w / 2 {
            for j in h / 2 + 1..h {
                count += grid[i][j];
            }
        }
        factor *= count;

        let mut count = 0;
        for i in w / 2 + 1..w {
            for j in h / 2 + 1..h {
                count += grid[i][j];
            }
        }
        factor *= count;

        factor
    }

    fn part2(&self) -> u64 {
        // let input = include_str!("../../data/input14.txt");
        // need to admit part 2 of this is a bit harder to implement actually
        0
    }

    fn get_day(&self) -> u8 {
        self.day.day
    }
}

pub fn run() {
    Day14::new().solve();
}
