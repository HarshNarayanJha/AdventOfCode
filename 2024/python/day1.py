from collections import Counter

# part 1
list1 = []
list2 = []

with open("input1.txt", "r") as inp:
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

# part 2
list2_counts = Counter(list2)
similarity_score = 0

for k in list1:
    similarity_score += k * list2_counts[k]

print(similarity_score)
