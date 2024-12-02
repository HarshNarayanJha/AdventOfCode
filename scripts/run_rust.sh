#!/bin/bash
year=$(date +"%Y")

cd $year
cd rust

cargo run --quiet --release
