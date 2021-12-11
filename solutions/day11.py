def parse(puzzle_input):
    grid = dict()
    y = 0
    for line in puzzle_input:
        for x, energy in enumerate(line):
            grid[(y,x)] = int(energy)

        y = y + 1

    return grid

def reset(grid):
    for coords in grid.keys():
        energy = grid[coords]
        if energy > 9:
            grid[coords] = 0

    return grid

def flash(grid, coords, flashed):
    if grid.get(coords) is None:
        return grid, flashed

    if grid.get(coords) <= 9 or flashed.get(coords) is not None:
        return grid, flashed

    flashed[coords] = True
    y, x = coords
    adjacents = [
        (y-1, x-1),
        (y-1, x+0),
        (y-1, x+1),
        (y+0, x-1),
        (y+0, x+1),
        (y+1, x-1),
        (y+1, x+0),
        (y+1, x+1)
    ]
    for adjacent in adjacents:
        energy = grid.get(adjacent)
        if energy is None:
            continue

        energy = energy + 1
        grid[adjacent] = energy
        grid, flashed = flash(grid, adjacent, flashed)

    return grid, flashed

def step(grid):
    for coords, energy in grid.items():
        grid[coords] = energy + 1

    flashed = dict()
    for coords in grid.keys():
        grid, flashed = flash(grid, coords, flashed)

    # Reset flashed octopi
    grid = reset(grid)

    return grid, len(flashed)

def d11p1(puzzle_input):
    total = 0
    grid = parse(puzzle_input)
    for i in range(100):
        grid, count = step(grid)
        total = total + count

    return total

def d11p2(puzzle_input):
    i = 1
    grid = parse(puzzle_input)
    while True:
        grid, count = step(grid)
        if count == 100:
            return i

        i = i + 1

def solve(puzzle_input):
    return d11p1(puzzle_input), d11p2(puzzle_input)
