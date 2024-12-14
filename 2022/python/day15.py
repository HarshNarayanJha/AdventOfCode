from math import sqrt
import re

class Grid:
    def __init__(self):
        self.sensors = []
        self.sensors_nobeacons_blocks = {}
        self.all_nobeacons_blocks = []
        self.beacons = []
    
    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def add_beacons(self, beacon):
        self.beacons.append(beacon)

    def get_block(self, x, y):
        for s in self.sensors:
            if x == s.x and y == s.y:
                return "S"
        for b in self.beacons:
            if x == b.x and y == b.y:
                return "B"
        # for n in self.all_nobeacons_blocks:
        #     if x == n[0] and y == n[1]:
        #         return "#"
        return "."

    def build_nobeacon_blocks(self):
        xs = []
        ys = []
        for s in self.sensors:
            xs.append(s.x)
            ys.append(s.y)
            self.sensors_nobeacons_blocks[s] = []
        
        # xmax, ymax = max(xs), max(ys)
        # xmin, ymin = min(xs), min(ys)

        # print(xmax, xmin, ymin, ymax)
        for s in self.sensors:
            targetdist = abs(s.y - target)
            if targetdist > s.maxdist:
                continue
            
            # print(s, targetdist, s.maxdist, "This is in range")
            # continue
            # maxdist = sqrt((s.x - s.beacon.x)**2 + (s.y - s.beacon.y)**2)
            # print(s.x - s.maxdist, s.x + s.maxdist)
            x_max_deviation = sqrt(s.maxdist**2 - targetdist**2)
            for x in range(int(s.x - x_max_deviation), int(s.x + x_max_deviation)):
                # for y in range(int(ymin - maxdist) - 1, int(ymax+maxdist) + 1):
                for y in [target]:
                    if self.get_block(x, y) in "BS": continue
                    # thisdist = sqrt((s.x - x)**2 + (s.y - y)**2)
                    thisdist = abs(s.x - x) + abs(s.y - y)
                    if thisdist <= s.maxdist:
                        # print(x, y) if y == target else ...
                        if (x, y) not in self.sensors_nobeacons_blocks:
                            self.sensors_nobeacons_blocks[s].append((x, y))
                        if (x, y) not in self.all_nobeacons_blocks:
                            self.all_nobeacons_blocks.append((x, y))

class Sensor:
    def __init__(self, x, y, beacon):
        self.x = x
        self.y = y
        self.beacon = beacon
        self.maxdist = -1
        self.calculate_maxdist()
    
    def __repr__(self) -> str:
        return f"Sensor at {self.x},{self.y}: closest beacon at {self.beacon.x}, {self.beacon.y}"

    def calculate_maxdist(self):
        # self.maxdist = sqrt((self.x - self.beacon.x)**2 + (self.y - self.beacon.y)**2)
        self.maxdist = abs(self.x - self.beacon.x) + abs(self.y - self.beacon.y)
class Beacon:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Beacon at {self.x},{self.y}"

def read_report(f, grid):
    lines = f.readlines()
    for l in lines:
        sensor, beacon = l.split(": ")
        sx, sy = re.match(r"Sensor at x=(-\d+|\d+), y=(-\d+|\d+)", sensor).groups()
        bx, by = re.match(r"closest beacon is at x=(-\d+|\d+), y=(-\d+|\d+)", beacon.strip()).groups()
        b = Beacon(int(bx), int(by))
        s = Sensor(int(sx), int(sy), b)

        grid.add_sensor(s)
        grid.add_beacons(b)

grid = Grid()

target = 2000000

with open("./2022/sensors_report.txt", "r") as f:
    read_report(f, grid)

grid.build_nobeacon_blocks()

j = []

for i in grid.all_nobeacons_blocks:
    if i[1] == target:
        j.append(i)

print(len(j))