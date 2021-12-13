from collections import defaultdict

def parse(puzzle_input):
    mode = 0
    folds = list()
    grid = defaultdict(dict)
    width, height = 0, 0
    for line in puzzle_input:
        if len(line) == 0:
            mode = 1
            continue

        if mode == 1:
            params = line.split()
            axis, value = params[-1].split("=", 1)
            folds.append((axis, int(value)))
            continue

        rx, ry = line.split(",", 1)
        x, y = int(rx), int(ry)

        if x > width:
            width = x

        if y > height:
            height = y

        grid[y][x] = True

    return folds, grid, width, height

def fold(folds, grid, width, height):
    folded = defaultdict(dict)

    axis, value = folds[0]
    if axis == "y":
        for i in range(value):
            folded[i] = grid[i]

        for i in range(1, height-value+1):
            row = grid[value+i]

            y = value - i
            ref = grid[y]
            for x in range(width+1):
                col = row.get(x)
                folded[y][x] = col if col else ref.get(x)

        return folds[1:], folded, width, value-1

    if axis == "x":
        for y in range(height+1):
            row = grid[y]
            for i in range(value):
                folded[y][i] = row.get(i)

            for j in range(1, width-value+1):
                rx = value - j
                fx = value + j
                col = row.get(fx)
                folded[y][rx] = col if col else row.get(rx)

        return folds[1:], folded, value-1, height

def show(grid, width, height):
    line = ""
    for y in range(height+1):
        for x in range(width+1):
            char = "#" if grid[y].get(x) else " "
            line = line + char

        print(line)
        line = ""

def d13p1(puzzle_input):
    folds, grid, width, height = fold(*parse(puzzle_input))
    count = 0
    for row in grid.values():
        for col in row.values():
            if col:
                count = count + 1

    folds, grid, width, height = fold(folds, grid, width, height)
    return count

def d13p2(puzzle_input):
    folds, grid, width, height = parse(puzzle_input)
    while len(folds) > 0:
        folds, grid, width, height = fold(folds, grid, width, height)

    show(grid, width, height)
    return None

def solve(puzzle_input):
    return d13p1(puzzle_input), d13p2(puzzle_input)
