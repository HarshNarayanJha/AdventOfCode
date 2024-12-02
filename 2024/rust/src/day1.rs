use std::time::Instant;
use std::{collections::HashMap, iter::zip};

pub fn part1() -> u32 {
    let input = include_str!("../../data/input1.txt");

    let mut list1: Vec<u32> = vec![];
    let mut list2: Vec<u32> = vec![];

    for line in input.lines() {
        let parts: Vec<&str> = line.split_whitespace().collect();

        list1.push(parts[0].parse().expect("Input is not correct"));
        list2.push(parts[1].parse().expect("Input is not correct"));
    }

    list1.sort();
    list2.sort();

    let mut dist_sum: u32 = 0;

    for (j, k) in zip(list1, list2) {
        dist_sum += j.abs_diff(k);
    }

    dist_sum
}

pub fn part2() -> u32 {
    let input = include_str!("../../data/input1.txt");

    let mut list1: Vec<u32> = vec![];
    let mut map2: HashMap<u32, u32> = HashMap::new();

    for line in input.lines() {
        let parts: Vec<&str> = line.split_whitespace().collect();

        let m: u32 = parts[0].parse().expect("Input is not correct");
        let n: u32 = parts[1].parse().expect("Input is not correct");

        list1.push(m);
        if map2.contains_key(&n) {
            map2.insert(n, map2.get(&n).unwrap() + 1);
        } else {
            map2.insert(n, 1);
        }
    }

    let mut sim_score: u32 = 0;

    for j in list1 {
        if map2.contains_key(&j) {
            sim_score += j * map2[&j];
        }
    }

    sim_score
}

pub fn solve() {
    println!("\nDay {}", 1);

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
