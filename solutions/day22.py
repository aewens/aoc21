from collections import namedtuple, Counter

Range = namedtuple("Range", ["min", "max"])
Block = namedtuple("Block", ["x", "y", "z"])

def parse(lines):
    rx = None
    ry = None
    rz = None
    cubes = list()

    for line in lines:
        op, block = line.split(" ", 1)
        xblock, yblock, zblock = block.split(",", 2)
        xs, xe = xblock.split("=", 1)[1].split("..", 1)
        ys, ye = yblock.split("=", 1)[1].split("..", 1)
        zs, ze = zblock.split("=", 1)[1].split("..", 1)

        xs, xe = int(xs), int(xe)
        ys, ye = int(ys), int(ye)
        zs, ze = int(zs), int(ze)

        bx = Range(xs, xe)
        by = Range(ys, ye)
        bz = Range(zs, ze)

        cube = op == "on", Block(bx, by, bz)
        cubes.append(cube)

    return cubes

def step(grid, cube, init=True):
    op, block = cube
    bx, by, bz = block
    bx = Range(max(-50, bx.min), min(bx.max, 50))
    by = Range(max(-50, by.min), min(by.max, 50))
    bz = Range(max(-50, bz.min), min(bz.max, 50))

    for z in range(bz.min, bz.max+1):
        for y in range(by.min, by.max+1):
            for x in range(bx.min, bx.max+1):
                if op:
                    grid[(z,y,x)] = True

                else:
                    grid.pop((z,y,x), None)

    return grid

def intersect(cube, block):
    cx, cy, cz = cube
    bx, by, bz = block

    nx = Range(max(cx.min, bx.min), min(cx.max, bx.max))
    ny = Range(max(cy.min, by.min), min(cy.max, by.max))
    nz = Range(max(cz.min, bz.min), min(cz.max, bz.max))

    if nx.min <= nx.max and ny.min <= ny.max and nz.min <= nz.max:
        return Block(nx, ny, nz)

    return None

def merge(cubes):
    count = Counter()
    for (op, block) in cubes:
        current = Counter()
        for other, value in count.items():
            overlap = intersect(other, block)
            if overlap is not None:
                current[overlap] = current[overlap] - value

        if op:
            current[block] = current[block] + 1

        count.update(current)

    return count

def collapse(count):
    total = 0
    for cube, value in count.items():
        cx = abs(cube.x.max-cube.x.min)+1
        cy = abs(cube.y.max-cube.y.min)+1
        cz = abs(cube.z.max-cube.z.min)+1
        c = cx * cy * cz * value
        total = total + c

    return total

def d22p1(puzzle_input):
    cubes = parse(puzzle_input)
    grid = dict()
    for cube in cubes:
        grid = step(grid, cube)

    return len(grid)

def d22p2(puzzle_input):
    cubes = merge(parse(puzzle_input))
    return collapse(cubes)

def solve(puzzle_input):
    return d22p1(puzzle_input), d22p2(puzzle_input)
