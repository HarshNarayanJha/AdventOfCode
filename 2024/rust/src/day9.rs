use crate::day::{Day, Solution};

pub struct Day9 {
    day: Day,
}

impl Day9 {
    pub fn new() -> Self {
        Self { day: Day::new(9) }
    }
}

impl Solution for Day9 {
    fn part1(&self) -> u64 {
        let input = include_str!("../../data/input9.txt");

        let mut i = 1;
        let mut fid = -1;
        let fs = input
            .lines()
            .collect::<Vec<&str>>()
            .first()
            .unwrap()
            .chars()
            .map(|x| {
                i ^= 1;
                if i == 0 {
                    fid += 1;
                    [fid].repeat(x.to_digit(10).unwrap() as usize)
                } else {
                    [-1].repeat(x.to_digit(10).unwrap() as usize)
                }
            })
            .flatten()
            .collect::<Vec<i32>>();

        let n = fs.len();
        let num_files = fs.iter().filter(|&&x| x != -1).count();

        let mut checksum: u64 = 0;
        let mut last_checked = n;

        for b in 0..n {
            if b == num_files {
                break;
            }

            if fs[b] == -1 {
                let mut idx = last_checked - 1;
                while fs[idx] == -1 {
                    idx -= 1;
                }

                checksum += (b as i32 * fs[idx]) as u64;
                last_checked = idx;
            } else {
                checksum += (b as i32 * fs[b]) as u64;
            }
        }

        checksum
    }

    fn part2(&self) -> u64 {
        let input = include_str!("../../data/input9.txt");

        let mut i = 1;
        let mut fid = -1;
        let mut fs = input
            .lines()
            .collect::<Vec<&str>>()
            .first()
            .unwrap()
            .chars()
            .map(|x| {
                i ^= 1;
                if i == 0 {
                    fid += 1;
                    [fid].repeat(x.to_digit(10).unwrap() as usize)
                } else {
                    [-1].repeat(x.to_digit(10).unwrap() as usize)
                }
            })
            .flatten()
            .collect::<Vec<i32>>();

        let n = fs.len() as i32;
        let mut b: i32 = n - 1;

        while b >= 0 {
            if fs[b as usize] != -1 {
                let file_from = b;
                let mut file_to = file_from;
                let fid = fs[file_from as usize];
                while file_to >= 0 && fs[file_to as usize] == fid {
                    file_to -= 1;
                }
                let fsize = file_from - file_to;

                // find empty space
                let mut empty_from = 0;
                let mut esize = 0;
                while empty_from < b {
                    while empty_from < b && fs[empty_from as usize] != -1 {
                        empty_from += 1;
                    }
                    while empty_from + esize < b && fs[empty_from as usize + esize as usize] == -1 {
                        esize += 1;
                    }
                    if esize >= fsize {
                        break;
                    }

                    empty_from += 1;
                    esize = 0;
                }

                if fsize <= esize {
                    for i in 0..fsize {
                        let temp = fs[(empty_from + i) as usize];
                        fs[(empty_from + i) as usize] = fs[(file_from - i) as usize];
                        fs[(file_from - i) as usize] = temp;
                    }
                }

                b = b - fsize;
            } else {
                b -= 1;
            }
        }

        fs.iter().enumerate().fold(0, |acc, (i, &x)| {
            if x == -1 {
                acc + 0
            } else {
                acc + (i as u64 * x as u64)
            }
        })
    }

    fn get_day(&self) -> u8 {
        self.day.day
    }
}

pub fn run() {
    Day9::new().solve();
}
