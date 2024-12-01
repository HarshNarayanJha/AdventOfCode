with open('input6.txt', 'r') as fp:
    data = fp.read()

data = data.split("\n")

# print(data)
races = []
for t, d in zip(data[0].split()[1:], data[1].split()[1:]):
    races.append((int(t), int(d)))

print(races)

class Boat:
    def __init__(self, time, total_time) -> None:
        self.time = time
        self.distance = self.time * (total_time - self.time)

    def run(self):
        return self.distance

ways = {}
for i, r in enumerate(races):
    ways[i] = 0
    total_time = r[0]
    record_distance = r[1]
    for t in range(total_time+1):
        distance = Boat(t, total_time).run()
        if distance > record_distance:
            ways[i] += 1

product = 1
for j in ways.values():
    product *= j

print(product)