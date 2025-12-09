import math

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def is_point_inside_angle_sum(pt, poly, eps=1e-6):
    if pt in poly:
        return True

    px, py = pt
    total = 0.0
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        v1x, v1y = x1 - px, y1 - py
        v2x, v2y = x2 - px, y2 - py
        a1 = math.atan2(v1y, v1x)
        a2 = math.atan2(v2y, v2x)
        da = a2 - a1
        if da <= -math.pi:
            da += 2 * math.pi
        elif da > math.pi:
            da -= 2 * math.pi
        total += da
    return abs(abs(total) - 2 * math.pi) < eps


with open("../data/input09.txt", "r") as fp:
    lines = fp.read().strip().splitlines()

R = [tuple(map(int, line.split(","))) for line in lines]

# Test points
test_points = {
    "a": (4898, 50147),
    "b": (4898, 66535),
    "c": (94808, 50147),
    "d": (94808, 66535),
    "e": (17710, 49440),
}

inside_pts = []
outside_pts = []

for name, p in test_points.items():
    inside = is_point_inside_angle_sum(p, R)
    print(name, p, "→", "inside" if inside else "outside")
    if inside:
        inside_pts.append(p)
    else:
        outside_pts.append(p)

# Plot
fig, ax = plt.subplots()
polygon_patch = Polygon(R, closed=True, edgecolor="black", facecolor="lightblue", alpha=0.4)
ax.add_patch(polygon_patch)

if inside_pts:
    xs, ys = zip(*inside_pts)
    ax.scatter(xs, ys, c="green", marker="o", label="inside")

if outside_pts:
    xs, ys = zip(*outside_pts)
    ax.scatter(xs, ys, c="red", marker="x", label="outside")

ax.set_aspect("equal")
ax.set_xlim(min(x for x, y in R) - 1, max(x for x, y in R) + 1)
ax.set_ylim(min(y for x, y in R) - 1, max(y for x, y in R) + 1)
ax.legend()
plt.title("Polygon")
plt.show()
