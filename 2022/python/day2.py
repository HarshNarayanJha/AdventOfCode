




elf_moves = {
    "A": '',
    "B": '',
    "C": '',
}

my_moves = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

# Winner : Loser
winning = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}

elf_my = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}

with open("./2022/rock_paper_scissor_startegy.txt") as f:
    lines = f.readlines()

total_points = []

for l in lines:
    l = l.strip()
    point = 0
    elf, my = l.split(" ")

    if winning[elf] == my:
        # print("Win")
        point += 6
    elif elf_my[elf] == my:
        # print("Tie")
        point += 3
    else:
        # print("Lose")
        point += 0

    point += my_moves[my]

    total_points.append(point)

print(total_points)
print(len(total_points))
print(sum(total_points)) # 11386

# Part 2

# Elf : Me
losing = {
    "A": 'Z',
    "B": 'X',
    "C": 'Y',
}

total_points = []

for l in lines:
    l = l.strip()
    point = 0
    elf, outcome = l.split(" ")

    if outcome == "X":
        my = losing[elf]
        point += 0
    elif outcome == "Y":
        my = elf_my[elf]
        point += 3
    elif outcome == "Z":
        my = winning[elf]
        point += 6

    point += my_moves[my]

    total_points.append(point)

print(total_points)
print(len(total_points))
print(sum(total_points)) # 13600