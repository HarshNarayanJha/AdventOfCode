#!/bin/bash

year=$(date +"%Y")
if [ -z "$1" ]; then
    day=$(date +"%d")
else
    day=$1
fi

echo "Advent of Code Scaffolder!"
echo "Preparing to Scaffold Day $day"
echo "Languages selected are Python, C++, and Rust"

cd $year

for lang in "python" "cpp" "rust"; do
    cd $lang
    if [ "$lang" = "python" ]; then
        if [ ! -f "day$day.py" ]; then
            cp "_template.py" "day$day.py"
        fi
    elif [ "$lang" = "cpp" ]; then
        if [ ! -f "day$day.cpp" ]; then
            cp "_template.cpp" "day$day.cpp"
        fi
    elif [ "$lang" = "rust" ]; then
        if [ ! -f "src/day$day.rs" ]; then
            cp "src/_template.rs" "src/day$day.rs"
            sed -i "s/N/$day/g" "src/day$day.rs"
            sed -i "s/pub mod day$(($day-1));/pub mod day$(($day-1));\npub mod day$day;/" "src/main.rs"
        fi
    fi
    cd ..
done

echo "Creating input file!"
if [ ! -f "data/input$day.txt" ]; then
    touch "data/input$day.txt"
fi
