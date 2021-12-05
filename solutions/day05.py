from collections import defaultdict

def parse(puzzle_input, diagonals=False):
    points = defaultdict(lambda: 0)
    for line in puzzle_input:
        start, end = line.split(" -> ", 1)
        sx, sy = start.split(",")
        ex, ey = end.split(",")

        sx, sy = int(sx), int(sy)
        ex, ey = int(ex), int(ey)

        if not diagonals and sx != ex and sy != ey:
            continue

        if sx == ex:
            min_y = min([sy, ey])
            max_y = max([sy, ey])
            for oy in range(max_y-min_y+1):
                points[(min_y+oy, sx)] = points[(min_y+oy, sx)] + 1

        elif sy == ey:
            min_x = min([sx, ex])
            max_x = max([sx, ex])
            for ox in range(max_x-min_x+1):
                points[(sy, min_x+ox)] = points[(sy, min_x+ox)] + 1

        else:
            ox = 1 if sx < ex else -1
            oy = 1 if sy < ey else -1
            for o in range(abs(sy-ey)+1):
                index = sy + (o * oy), sx + (o * ox)
                points[index] = points[index] + 1

    return points

def d5p1(puzzle_input):
    points = parse(puzzle_input)
    count = 0
    for value in points.values():
        if value > 1:
            count = count + 1

    return count

def d5p2(puzzle_input):
    points = parse(puzzle_input, diagonals=True)
    count = 0
    for value in points.values():
        if value > 1:
            count = count + 1

    return count

def solve(puzzle_input):
    return d5p1(puzzle_input), d5p2(puzzle_input)

