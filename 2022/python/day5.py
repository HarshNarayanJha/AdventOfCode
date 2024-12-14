import re

with open('./2022/crates_rearrangement.txt', 'r') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    lines[i] = l.strip("\n")

_structure = lines[:lines.index("")]
procedure = lines[lines.index("")+1:]
structure = {}
numbers = _structure.pop().split("  ")
crates = []

for i in range(len(_structure)):
    structure[int(i+1)] = []

# print(_structure)
num = 1
for line in _structure:
    while line:
        if line.startswith("["):
            c = line[:3]
            line = line[4:]
        elif line.startswith("    "):
            c = ""
            line = line[4:]
        elif line.startswith("   "):
            c = ""
            break
        structure[num].append(c)
    num += 1

stack = {}
for i in numbers:
    stack[int(i)] = []
for i in list(structure.values())[::-1]:
    for n, j in enumerate(i, 1):
        stack[n].append(j) if j else ...

print(stack)

pro_regex = re.compile(r"^move (\d+) from (\d) to (\d)$")
for p in procedure:
    print(p)
    ct, frm, to = re.match(pro_regex, p).groups()
    for j in range(int(ct)):
        e = stack[int(frm)].pop()
        stack[int(to)].append(e)

print(stack)

tops = ""
for i, j in stack.items():
    tops += j[-1].replace("[","").replace("]","")

print(tops) # CFFHVVHNC

# Part 2 -> reatin order instead of pop, push

stack2 = {}
for i in numbers:
    stack2[int(i)] = []
for i in list(structure.values())[::-1]:
    for n, j in enumerate(i, 1):
        stack2[n].append(j) if j else ...

for p in procedure:
    print(p)
    ct, frm, to = re.match(pro_regex, p).groups()
    elms = []
    for i in range(int(ct)):
        elms.append(stack2[int(frm)].pop())
    stack2[int(to)].extend(elms[::-1])

tops2 = ""
for i, j in stack2.items():
    tops2 += j[-1].replace("[","").replace("]","")
print(stack2)
print(tops2) # FSZWBPTBG