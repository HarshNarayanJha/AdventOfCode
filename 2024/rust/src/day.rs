use std::time::Instant;

pub struct Day {
    pub day: u8,
}

impl Day {
    pub fn new(day: u8) -> Self {
        Self { day }
    }
}

pub trait Solution {
    fn part1(&self) -> u64;
    fn part2(&self) -> u64;
    fn get_day(&self) -> u8;

    fn solve(&self) {
        println!("\n🎄 {}Day {}🎄", "\x1b[32m", self.get_day());

        let now = Instant::now();
        println!("🎯 Part 1 -> {}{}{}", "\x1b[36m", self.part1(), "\x1b[0m");
        let elasped1 = now.elapsed();
        println!(
            "⚡ Took {}{:.5}ms{}",
            "\x1b[33m",
            elasped1.as_secs_f64() * 1000.0,
            "\x1b[0m"
        );

        println!();

        let now = Instant::now();
        println!("🎯 Part 2 -> {}{}{}", "\x1b[36m", self.part2(), "\x1b[0m");
        let elasped2 = now.elapsed();
        println!(
            "⚡ Took {}{:.5}ms{}",
            "\x1b[33m",
            elasped2.as_secs_f64() * 1000.0,
            "\x1b[0m"
        );

        println!(
            "\n⚡ Took Total {}{:.5}ms{}",
            "\x1b[33m",
            (elasped1 + elasped2).as_secs_f64() * 1000.0,
            "\x1b[0m"
        );

        println!("{}❄️  {} ❄️ {}", "\x1b[34m", "-".repeat(20), "\x1b[0m");
    }
}
