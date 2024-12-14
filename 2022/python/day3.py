
from string import ascii_lowercase, ascii_uppercase


priorities = {}
for i, a in enumerate(ascii_lowercase, 1):
    priorities[a] = i
for i, a in enumerate(ascii_uppercase, 27):
    priorities[a] = i


with open('./2022/rucksacks.txt', 'r') as f:
    bags = f.readlines()

grand_commons = []
for b in bags:
    c1, c2 = b[:len(b)//2], b[len(b)//2:]

    commons = []
    for c in c1:
        if c in c2:
            commons.append(c)
    
    # print(commons)
    grand_commons.append(set(commons))

total = 0
for c in grand_commons:
    for c1 in c:
        total += priorities[c1]

print(total) # 8243

# Part 2

groups = {}
n = 1
for i, b in enumerate(bags, 1):
    # print(i, n)
    if n not in groups:
        groups[n] = []
    groups[n].append(b.strip())
    if i % 3 == 0:
        n += 1

badges = []
for g in groups.values():
    badge = None
    for s in g[0]:
        if s in g[1] and s in g[2]: badge = s
    badges.append(badge)

print(badges)
total = 0
for b in badges:
    total += priorities[b]
print(total)
