def part1() -> int:
    grid = None
    with open("../data/input12.txt", "r") as inp:
        grid = [list(list(line.strip())) for line in inp.readlines()]

    H = len(grid)
    W = len(grid[0])

    cost = 0

    regions = {}
    visited = set()
    component_id = 0

    def dfs(i, j, label):
        stack = [(i, j)]
        component = []

        while stack:
            ci, cj = stack.pop()
            if (ci, cj) in visited:
                continue

            visited.add((ci, cj))
            component.append((ci, cj))

            for ni, nj in [
                (ci - 1, cj),
                (ci + 1, cj),
                (ci, cj - 1),
                (ci, cj + 1),
            ]:
                if 0 <= ni < H and 0 <= nj < W:
                    if grid[ni][nj] == label and (ni, nj) not in visited:
                        stack.append((ni, nj))

        return component

    for i in range(H):
        for j in range(W):
            if (i, j) not in visited:
                label = grid[i][j]
                component = dfs(i, j, label)
                key = (label, component_id)
                regions[key] = component
                component_id += 1

    for r in regions:
        span = regions[r]
        area = len(span)
        perimeter = 0

        for i, j in span:
            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for ni, nj in neighbors:
                if (ni, nj) not in span:
                    perimeter += 1

        cost += area * perimeter

    return cost


def part2() -> int:
    grid = None
    with open("../data/input12.txt", "r") as inp:
        grid = [list(list(line.strip())) for line in inp.readlines()]

    H = len(grid)
    W = len(grid[0])

    cost = 0

    regions = {}
    visited = set()
    component_id = 0

    def dfs(i, j, label):
        stack = [(i, j)]
        component = []

        while stack:
            cur_i, cur_j = stack.pop()
            if (cur_i, cur_j) in visited:
                continue

            visited.add((cur_i, cur_j))
            component.append((cur_i, cur_j))

            for ni, nj in [
                (cur_i - 1, cur_j),
                (cur_i + 1, cur_j),
                (cur_i, cur_j - 1),
                (cur_i, cur_j + 1),
            ]:
                if 0 <= ni < H and 0 <= nj < W:
                    if grid[ni][nj] == label and (ni, nj) not in visited:
                        stack.append((ni, nj))

        return component

    for i in range(H):
        for j in range(W):
            if (i, j) not in visited:
                label = grid[i][j]
                component = dfs(i, j, label)
                key = (label, component_id)
                regions[key] = component
                component_id += 1

    print(regions)

    for r in regions:
        span = regions[r]
        area = len(span)
        sides = 0

        dx, dy = (0, 1)
        sx, sy = span[0]
        cx, cy = sx, sy

        # start going right, if it not in span, got down, then left, then up until reach back
        # each time chanage direction increment sides

        #print("Starting measure for region", r)
        visited = set()

        reached_end = False

        while not reached_end and area != 1:
            #print("At", cx, cy)

            if (cx, cy) == (sx, sy) and sides != 0:
                #print("back to start, inc side and break")
                # sides += 1
                break

            #print("Moving in direction", dx, dy)

            nx, ny = cx + dx, cy + dy

            #print("Checking", nx, ny)

            while True:
                if (nx, ny) not in span:
                    #print("next is oob, change direction and inc side")
                    dx, dy = dy, -dx
                    nx, ny = cx + dx, cy + dy
                    #print("direction changed to", dx, dy)
                    sides += 1
                else:
                    #print(nx, ny, "in bounds")
                    if (nx, ny) not in visited:
                        #print("... and not is visited, proceeding...")
                        # in span but not in visited
                        break

                    else:
                        #print(nx, ny, "but visited, checking for any unviisted neightbout")
                        neighbours = (
                            (cx, cy + 1),
                            (cx, cy - 1),
                            (cx + 1, cy),
                            (cx - 1, cy),
                        )
                        neighbours = filter(lambda x: x in span, neighbours)
                        if any([x not in visited for x in neighbours]):
                            #print("found unvisited neighbous")
                            dx, dy = dy, -dx
                            nx, ny = cx + dx, cy + dy
                            #print("direction changed to", dx, dy)
                            # sides += 1
                        else:
                            #print("No unvisted neighbours, means reached the end")
                            reached_end = True
                            break

            #print("Sides", sides)
            #print()

            visited.add((cx, cy))
            cx, cy = nx, ny

        if area != 1:
            sides = sides * 2
        else:
            sides = 4

        print("Region", r, area, sides)

        cost += area * sides

    return cost


print(part1())
print(part2())
