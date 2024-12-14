

grid = []
with open("./2022/tree_heightmap.txt", 'r') as f:
    lines = f.readlines()

for l in lines:
    l = l.strip()
    grid.append([int(x) for x in l])

for g in grid:
    print(g)

visible = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if r == 0 or c == 0 or r == len(grid) - 1 or c == len(grid[r]) - 1:
            # print(r, c)
            visible += 1
        else:
            current = grid[r][c]
            col_list1 = []
            col_list2 = []
            for x, g in enumerate(grid):
                if x < r:
                    col_list1.append(g[c])
                elif x > r:
                    col_list2.append(g[c])

            # print(r, c, current, col_list1, col_list2)
            if all(i < current for i in grid[r][:c]) or all(i < current for i in grid[r][c+1:]) or \
                all(j < current for j in col_list1) or all(j < current for j in col_list2):
                    print("yes")
                    visible += 1

print(visible) # 1785

# part 2

class Grid:
    def __init__(self, grid) -> None:
        self.grid = grid

    def get_scenic_score(self, r, c):
        top_list = []
        bottom_list = []
        for x, g in enumerate(self.grid):
            if x < r:
                top_list.append(g[c])
            elif x > r:
                bottom_list.append(g[c])
        left_list = self.grid[r][:c]
        right_list = self.grid[r][c+1:]

        # print(top_list, bottom_list, left_list, right_list)

        top, left, bottom, right = 0, 0, 0, 0
        current = self.grid[r][c]
        for _t in top_list[::-1]:
            if _t < current: top += 1
            elif _t >= current:
                top += 1
                break
        for _b in bottom_list:
            if _b < current: bottom += 1
            elif _b >= current:
                bottom += 1
                break
        for _l in left_list[::-1]:
            if _l < current: left += 1
            elif _l >= current:
                left += 1
                break
        for _r in right_list:
            if _r < current: right += 1
            elif _r >= current:
                right += 1
                break
        
        return top * left * bottom * right


Gd = Grid(grid)
scores = []
for r in range(len(Gd.grid)):
    for c in range(len(Gd.grid[r])):
        if r != 0 or c != 0 or r != len(grid) - 1 or c != len(grid[r]) - 1:
            scores.append(Gd.get_scenic_score(r, c))

print(max(scores)) # 345168
# print(Gd.get_scenic_score(3, 2))