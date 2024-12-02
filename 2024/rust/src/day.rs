use std::time::Instant;

pub struct Day {
    pub day: u32,
}

impl Day {
    pub fn new(day: u32) -> Self {
        Self { day }
    }
}

pub trait Solution {
    fn part1(&self) -> u32;
    fn part2(&self) -> u32;
    fn get_day(&self) -> u32;

    fn solve(&self) {
        println!("\n🎄 {}Day {}🎄", "\x1b[32m", self.get_day());

        let now = Instant::now();
        println!("🎯 Part 1 -> {}{}{}", "\x1b[36m", self.part1(), "\x1b[0m");
        let elasped = now.elapsed();
        println!(
            "⚡ Took {}{:.5}ms{}",
            "\x1b[33m",
            elasped.as_secs_f64() * 1000.0,
            "\x1b[0m"
        );

        println!();

        let now = Instant::now();
        println!("🎯 Part 2 -> {}{}{}", "\x1b[36m", self.part2(), "\x1b[0m");
        let elasped = now.elapsed();
        println!(
            "⚡ Took {}{:.5}ms{}",
            "\x1b[33m",
            elasped.as_secs_f64() * 1000.0,
            "\x1b[0m"
        );

        println!("{}❄️  {} ❄️ {}", "\x1b[34m", "-".repeat(20), "\x1b[0m");
    }
}
