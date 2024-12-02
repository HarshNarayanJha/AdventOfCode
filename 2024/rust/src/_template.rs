use std::time::Instant;

pub fn part1() -> u32 {
    let input = include_str!("../../data/input0.txt");

    0
}

pub fn part2() -> u32 {
    let input = include_str!("../../data/input0.txt");

    0
}

pub fn solve() {
    println!("\nDay {}", 0);

    let now = Instant::now();
    println!("Part 1 -> {}", part1());
    let elasped = now.elapsed();

    println!("Took {:.5}ms", elasped.as_secs_f64() * 1000.0);

    println!();

    let now = Instant::now();
    println!("Part 2 -> {}", part2());
    let elasped = now.elapsed();
    println!("Took {:.5}ms", elasped.as_secs_f64() * 1000.0);

    println!("{:-^30}", "-");
}
