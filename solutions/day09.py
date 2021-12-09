from collections import defaultdict

def parse(puzzle_input):
    y = 0
    points = defaultdict(lambda: defaultdict(lambda: 9))
    for line in puzzle_input:
        for x, point in enumerate(line):
            points[y][x] = int(point)

        y = y + 1

    return points

def get_neighbors(points, y, x):
    return [
        points[y-1][x],
        points[y+1][x],
        points[y][x-1],
        points[y][x+1]
    ]

def get_low_points(puzzle_input):
    points = parse(puzzle_input)

    h = len(points)
    w = len(points[0])
    low_points = list()
    for y in range(h):
        for x in range(w):
            point = points[y][x]
            if point < min(get_neighbors(points, y, x)):
                low_points.append(point)

    return low_points

def check_neighbors(points, y, x, seen):
    basin = dict()
    if (y, x) in seen:
        return basin, seen

    seen[(y, x)] = True
    point = points[y][x]
    if point == 9:
        return basin, seen

    basin[(y,x)] = True
    neighbors = [
        (y-1, x),
        (y+1, x),
        (y, x-1),
        (y, x+1)
    ]
    for (ny, nx) in neighbors:
        if (ny, nx) in seen:
            continue

        others, oseen = check_neighbors(points, ny, nx, seen)
        seen.update(oseen)
        basin.update(others)

    return basin, seen

def get_basins(puzzle_input):
    points = parse(puzzle_input)

    h = len(points)
    w = len(points[0])
    seen = dict()
    basins = list()
    for y in range(h):
        for x in range(w):
            if (y, x) in seen:
                continue

            basin, bseen = check_neighbors(points, y, x, seen)
            seen.update(bseen)
            basins.append(len(basin))

    return basins

def d9p1(puzzle_input):
    return sum([lp+1 for lp in get_low_points(puzzle_input)])

def d9p2(puzzle_input):
    basins = sorted(get_basins(puzzle_input))[-3:]
    return basins[0] * basins[1] * basins[2]

def solve(puzzle_input):
    return d9p1(puzzle_input), d9p2(puzzle_input)

