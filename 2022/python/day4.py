

with open("./2022/section_assignments.txt", "r") as f:
    lines = f.readlines()

totally_enclosing = 0
for l in lines:
    e1, e2 = l.split(",")

    e1_from, e1_to = e1.split("-")
    e2_from, e2_to = e2.split("-")
    e1range = list(range(int(e1_from), int(e1_to)+1))
    e2range = list(range(int(e2_from), int(e2_to)+1))

    smaller = min(e1range, e2range, key=len)
    larger = e2range if smaller == e1range else e1range

    flag = True
    for s in smaller:
        if s not in larger:
            flag = False
    if flag:
        totally_enclosing += 1
    print(smaller, larger, flag)

print(totally_enclosing) # 524


# Part 2
del l, e1, e2, e1_from, e2_from

partially_enclosing = 0
for l in lines:
    e1, e2 = l.split(",")

    e1_from, e1_to = e1.split("-")
    e2_from, e2_to = e2.split("-")
    
    if int(e2_from) <= int(e1_to) and int(e2_to) >= int(e1_from):
        partially_enclosing += 1

print(partially_enclosing) # 524