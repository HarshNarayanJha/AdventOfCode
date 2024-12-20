# Advent Of Code 2024

This year I will do all questions first in python, then c++, finally rust for sure.

### Benchmarks

<details>

<summary>C++</summary>

```fish
./bin/day1
  Time (mean ± σ):       2.1 ms ±   0.3 ms    [User: 0.7 ms, System: 1.2 ms]
  Range (min … max):     1.7 ms …   3.5 ms    940 runs
./bin/day2
  Time (mean ± σ):       5.0 ms ±   0.4 ms    [User: 3.3 ms, System: 1.4 ms]
  Range (min … max):     4.3 ms …   7.1 ms    563 runs
./bin/day3
  Time (mean ± σ):       2.5 ms ±   0.3 ms    [User: 0.9 ms, System: 1.3 ms]
  Range (min … max):     2.0 ms …   5.2 ms    1002 runs
./bin/day4
  Time (mean ± σ):       5.1 ms ±   0.4 ms    [User: 3.4 ms, System: 1.4 ms]
  Range (min … max):     4.4 ms …   7.0 ms    594 runs
./bin/day5
  Time (mean ± σ):       5.1 ms ±   0.5 ms    [User: 3.4 ms, System: 1.3 ms]
  Range (min … max):     4.3 ms …   7.0 ms    448 runs
./bin/day6
  Time (mean ± σ):     14.778 s ±  0.481 s    [User: 14.508 s, System: 0.006 s]
  Range (min … max):   14.438 s … 15.118 s    2 runs
./bin/day7
  Time (mean ± σ):      7.536 s ±  0.046 s    [User: 6.892 s, System: 0.519 s]
  Range (min … max):    7.504 s …  7.568 s    2 runs
./bin/day8
  Time (mean ± σ):       2.9 ms ±   0.4 ms    [User: 1.4 ms, System: 1.2 ms]
  Range (min … max):     2.1 ms …   5.0 ms    808 runs
./bin/day9
  Time (mean ± σ):     214.8 ms ±   8.8 ms    [User: 207.4 ms, System: 3.2 ms]
  Range (min … max):   203.2 ms … 231.3 ms    14 runs
./bin/day10
  Time (mean ± σ):       3.7 ms ±   0.4 ms    [User: 2.2 ms, System: 1.2 ms]
  Range (min … max):     2.9 ms …   5.9 ms    788 runs
./bin/day11
  Time (mean ± σ):      20.4 ms ±   1.1 ms    [User: 17.7 ms, System: 1.7 ms]
  Range (min … max):    18.2 ms …  23.7 ms    135 runs
./bin/day12
  Time (mean ± σ):      33.2 ms ±   2.2 ms    [User: 30.6 ms, System: 1.7 ms]
  Range (min … max):    30.1 ms …  43.8 ms    93 runs
./bin/day13
  Time (mean ± σ):       3.2 ms ±   0.4 ms    [User: 1.8 ms, System: 1.2 ms]
  Range (min … max):     2.6 ms …   5.0 ms    838 runs
```

</details>

<details>

<summary>Python</summary>

```fish
python day1.py
  Time (mean ± σ):     112.4 ms ±   3.2 ms    [User: 43.8 ms, System: 68.7 ms]
  Range (min … max):   109.0 ms … 125.3 ms    23 runs
python day2.py
  Time (mean ± σ):     126.3 ms ±   2.6 ms    [User: 58.8 ms, System: 68.0 ms]
  Range (min … max):   122.7 ms … 132.1 ms    24 runs
python day3.py
  Time (mean ± σ):     123.6 ms ±   2.8 ms    [User: 56.3 ms, System: 67.6 ms]
  Range (min … max):   120.0 ms … 129.8 ms    24 runs
python day4.py
  Time (mean ± σ):     315.6 ms ±   3.7 ms    [User: 240.1 ms, System: 70.2 ms]
  Range (min … max):   311.6 ms … 324.8 ms    10 runs
python day5.py
  Time (mean ± σ):     135.7 ms ±   3.2 ms    [User: 75.6 ms, System: 59.7 ms]
  Range (min … max):   131.6 ms … 143.5 ms    21 runs
python day6.py
  Time (mean ± σ):     127.1 ms ±   3.9 ms    [User: 56.7 ms, System: 68.9 ms]
  Range (min … max):   119.6 ms … 136.9 ms    21 runs
python day7.py
  Time (mean ± σ):     30.418 s ±  0.177 s    [User: 30.011 s, System: 0.086 s]
  Range (min … max):   30.292 s … 30.543 s    2 runs
python day8.py
  Time (mean ± σ):     121.9 ms ±   3.4 ms    [User: 50.1 ms, System: 70.5 ms]
  Range (min … max):   116.9 ms … 127.3 ms    25 runs
python day9.py
  Time (mean ± σ):     21.105 s ±  0.323 s    [User: 20.673 s, System: 0.077 s]
  Range (min … max):   20.877 s … 21.333 s    2 runs
python day10.py
  Time (mean ± σ):     125.9 ms ±   4.0 ms    [User: 62.0 ms, System: 63.5 ms]
  Range (min … max):   120.3 ms … 137.2 ms    22 runs
python day11.py
  Time (mean ± σ):     186.3 ms ±   6.7 ms    [User: 108.6 ms, System: 75.5 ms]
  Range (min … max):   178.3 ms … 199.8 ms    16 runs
python day12.py
  Time (mean ± σ):     331.5 ms ±   7.5 ms    [User: 294.0 ms, System: 36.7 ms]
  Range (min … max):   321.6 ms … 340.9 ms    10 runs
python day13.py
  Time (mean ± σ):      1.010 s ±  0.026 s    [User: 1.078 s, System: 1.247 s]
  Range (min … max):    0.962 s …  1.045 s    10 runs
python day14.py
  Time (mean ± σ):      1.433 s ±  0.041 s    [User: 1.382 s, System: 0.039 s]
  Range (min … max):    1.378 s …  1.508 s    10 runs
python day15.py
  Time (mean ± σ):      1.422 s ±  0.020 s    [User: 1.380 s, System: 0.038 s]
  Range (min … max):    1.386 s …  1.451 s    10 runs
python day16.py
  Time (mean ± σ):      3.180 s ±  0.205 s    [User: 3.036 s, System: 0.062 s]
  Range (min … max):    3.035 s …  3.326 s    2 runs
python day17.py
  Time (mean ± σ):      68.2 ms ±   3.5 ms    [User: 32.8 ms, System: 36.0 ms]
  Range (min … max):    62.9 ms …  75.3 ms    43 runs
python day18.py
  Time (mean ± σ):     295.1 ms ±   8.5 ms    [User: 216.1 ms, System: 71.3 ms]
  Range (min … max):   282.5 ms … 310.4 ms    10 runs
python day19.py
  Time (mean ± σ):      2.382 s ±  0.113 s    [User: 2.253 s, System: 0.076 s]
  Range (min … max):    2.243 s …  2.541 s    10 runs
python day20.py
  Time (mean ± σ):      1.825 s ±  0.052 s    [User: 1.771 s, System: 0.038 s]
  Range (min … max):    1.762 s …  1.912 s    10 runs
```

</details>

<details>
<summary>>Rust</summary>

```fish
🎄 Day 1🎄
🎯 Part 1 -> 2264607
⚡ Took 0.19217ms

🎯 Part 2 -> 19457120
⚡ Took 0.17835ms

⚡ Took Total 0.37052ms
❄️  -------------------- ❄️

🎄 Day 2🎄
🎯 Part 1 -> 279
⚡ Took 0.29730ms

🎯 Part 2 -> 343
⚡ Took 0.67139ms

⚡ Took Total 0.96869ms
❄️  -------------------- ❄️

🎄 Day 3🎄
🎯 Part 1 -> 187825547
⚡ Took 1.19724ms

🎯 Part 2 -> 85508223
⚡ Took 0.95990ms

⚡ Took Total 2.15714ms
❄️  -------------------- ❄️

🎄 Day 4🎄
🎯 Part 1 -> 2685
⚡ Took 10.56872ms

🎯 Part 2 -> 2048
⚡ Took 3.29451ms

⚡ Took Total 13.86324ms
❄️  -------------------- ❄️

🎄 Day 5🎄
🎯 Part 1 -> 6267
⚡ Took 0.72528ms

🎯 Part 2 -> 5184
⚡ Took 1.49941ms

⚡ Took Total 2.22469ms
❄️  -------------------- ❄️

🎄 Day 6🎄
🎯 Part 1 -> 4778
⚡ Took 14.11720ms

🎯 Part 2 -> 1618
⚡ Took 161777.42168ms

⚡ Took Total 161791.53888ms
❄️  -------------------- ❄️

🎄 Day 7🎄
🎯 Part 1 -> 5540634308362
⚡ Took 63.94769ms

🎯 Part 2 -> 472290821152397
⚡ Took 3426.54246ms

⚡ Took Total 3490.49015ms
❄️  -------------------- ❄️

🎄 Day 8🎄
🎯 Part 1 -> 313
⚡ Took 0.08501ms

🎯 Part 2 -> 1064
⚡ Took 0.28682ms

⚡ Took Total 0.37183ms
❄️  -------------------- ❄️

🎄 Day 9🎄
🎯 Part 1 -> 6225730762521
⚡ Took 2.59738ms

🎯 Part 2 -> 6250605700557
⚡ Took 250.01418ms

⚡ Took Total 252.61157ms
❄️  -------------------- ❄️

🎄 Day 10🎄
🎯 Part 1 -> 820
⚡ Took 0.78264ms

🎯 Part 2 -> 1786
⚡ Took 0.67895ms

⚡ Took Total 1.46159ms
❄️  -------------------- ❄️

🎄 Day 11🎄
🎯 Part 1 -> 211306
⚡ Took 0.25853ms

🎯 Part 2 -> 250783680217283
⚡ Took 8.78496ms

⚡ Took Total 9.04349ms
❄️  -------------------- ❄️

🎄 Day 12🎄
🎯 Part 1 -> 1550156
⚡ Took 7.18058ms

🎯 Part 2 -> 946084
⚡ Took 8.00808ms

⚡ Took Total 15.18866ms
❄️  -------------------- ❄️

🎄 Day 13🎄
🎯 Part 1 -> 37686
⚡ Took 0.23682ms

🎯 Part 2 -> 77204516023437
⚡ Took 0.22998ms

⚡ Took Total 0.46680ms
❄️  -------------------- ❄️

🎄 Day 14🎄
🎯 Part 1 -> 224969976
⚡ Took 0.14965ms

🎯 Part 2 -> 0
⚡ Took 0.00004ms

⚡ Took Total 0.14969ms

❄️  -------------------- ❄️
🎄 Day 15🎄
🎯 Part 1 -> 1568399
⚡ Took 7.78773ms

🎯 Part 2 -> 1219474
⚡ Took 18.70000ms

⚡ Took Total 26.48773ms
❄️  -------------------- ❄️

🎄 Day 16🎄
🎯 Part 1 -> 109516
⚡ Took 15.52170ms

🎯 Part 2 -> 568
⚡ Took 2259.50076ms

⚡ Took Total 2275.02245ms
❄️  -------------------- ❄️

🎄 Day 18🎄
🎯 Part 1 -> 364
⚡ Took 6.16400ms

(52, 28)
🎯 Part 2 -> 0
⚡ Took 7.70778ms

⚡ Took Total 13.87178ms
❄️  -------------------- ❄️

🎄 Day 19🎄
🎯 Part 1 -> 347
⚡ Took 33.56446ms

🎯 Part 2 -> 919219286602165
⚡ Took 33.12376ms

⚡ Took Total 66.68822ms
❄️  -------------------- ❄️
```

</details>
