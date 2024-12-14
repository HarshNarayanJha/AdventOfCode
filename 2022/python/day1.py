
with open('./2022/calories.txt', 'r') as f:
    data = f.read().split("\n\n")

data2 = []
for i in data:
    data2.append(i.split("\n"))

print(data2)

gps = {}
for i, d in enumerate(data2):
    gps[i] = 0
    for e in d:
        gps[i] += int(e)

print(max(gps.values()))

# Part 2
sorte = sorted(list(gps.values()))
print(sorte[-1] + sorte[-2] + sorte[-3])