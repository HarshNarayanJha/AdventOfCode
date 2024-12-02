#!/bin/bash
day=${1:-$(date +"%_d")}
year=$(date +"%Y")

cd $year
cd rust

cargo run --quiet --release -- $day
