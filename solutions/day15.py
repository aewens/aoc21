from heapq import heappop, heappush

infinity = float("inf")

def parse(puzzle_input):
    y = 0
    width = 0
    height = 0
    maze = dict()
    for row in puzzle_input:
        width = len(row)
        for x, risk in enumerate(row):
            maze[(y,x)] = int(risk)

        y = y + 1

    height = y
    return maze, width, height

def expand(tile, w, h):
    width = 0
    height = 0
    maze = dict()
    for (y, x), risk in tile.items():
        for i in range(5):
            for j in range(5):
                new_risk = risk + i + j
                if new_risk > 9:
                    new_risk = new_risk % 9

                ty = i * h + y
                tx = j * w + x
                maze[(ty, tx)] = new_risk
                width = max(tx, width)
                height = max(ty, height)

    return maze, width, height

def get_neighbors(maze, point):
    neighbors = dict()
    y, x = point

    others = [
        (y-1, x),
        (y+1, x),
        (y, x-1),
        (y, x+1)
    ]

    for other in others:
        neighbor = maze.get(other)
        if neighbor is None:
            continue

        neighbors[other] = neighbor

    return neighbors

def dijkstra(maze, start, end):
    seen = dict()
    points = [(0, start)]
    distances = {start: 0}
    while len(points) > 0:

        distance, point = heappop(points)
        if point == end:
            return distance

        if seen.get(point) is not None:
            continue

        seen[point] = True
        neighbors = get_neighbors(maze, point)
        for neighbor, risk in neighbors.items():
            route = distance + risk
            dist = distances.get(neighbor)
            if dist is None or route < dist:
                distances[neighbor] = route
                heappush(points, (route, neighbor))

    return infinity

def d15p1(puzzle_input):
    maze, width, height = parse(puzzle_input)
    count = dijkstra(maze, (0, 0), (height-1, width-1))
    return count

def d15p2(puzzle_input):
    maze, width, height = expand(*parse(puzzle_input))
    count = dijkstra(maze, (0, 0), (height, width))
    return count

def solve(puzzle_input):
    return d15p1(puzzle_input), d15p2(puzzle_input)
