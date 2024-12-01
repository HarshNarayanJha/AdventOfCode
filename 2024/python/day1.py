list1 = []
list2 = []

with open("input1.txt", 'r') as inp:
    while line := inp.readline():
        n, m = line.split()
        list1.append(int(n))
        list2.append(int(m))

    list1.sort()
    list2.sort()

dist_sum = 0

for j, k in zip(list1, list2):
    dist_sum += abs(j - k)

print(dist_sum)
