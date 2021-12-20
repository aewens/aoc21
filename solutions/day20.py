def parse(lines):
    resolve = lambda x: x == "#"

    image = dict()
    algo = [resolve(char) for char in lines[0]]
    ax, zx = None, None
    ay, zy = None, None
    for y, row in enumerate(lines[2:]):
        for x, col in enumerate(row):
            if col == "#":
                image[(y,x)] = True
                if ay is None or y < ay:
                    ay = y

                if ax is None or x < ax:
                    ax = x

                if zy is None or y > zy:
                    zy = y

                if zx is None or x > zx:
                    zx = x

    return algo, image, ax, zx, ay, zy

def step(algo, image, point, default):
    y, x = point
    resolve = dict()
    resolve[True] = "1"
    resolve[False] = "0"
    resolve[None] = default

    line = ""
    for oy in range(-1, 2):
        for ox in range(-1, 2):
            opoint = y+oy, x+ox
            char = resolve[image.get(opoint)]
            line = line + char

    #print(point, line, default)
    index = int(line, 2)
    return algo[index]

def show(image, ax, zx, ay, zy):
    for y in range(ay, zy+1):
        line = ""
        for x in range(ax, zx+1):
            char = "#" if image.get((y,x)) is not None else "."
            line = line + char

        print(line)

def enhance(puzzle_input, cycles):
    algo, image, ax, zx, ay, zy = parse(puzzle_input)
    #show(image, ax, zx, ay, zy)

    i = 0
    default = "0"
    keep = algo[0] is False
    new_image = dict()
    while i < cycles:
        b = 2 * (i+1)
        #print("Y", ay-b, ay+b+1)
        #print("X", ax-b, zx+b+1)
        for y in range(ay-b, zy+b+1):
            for x in range(ax-b, zx+b+1):
                point = y, x
                lit = step(algo, image, point, default)
                #print(i, point, lit, keep)
                if lit == keep:
                    new_image[point] = lit

        #print(i, len(new_image))
        i = i + 1
        image = new_image
        new_image = dict()
        if keep:
            default = "0"
            keep = algo[0] is False

        else:
            default = "1"
            keep = algo[-1] is False


    return image

def d20p1(puzzle_input):
    return len(enhance(puzzle_input, 2))

def d20p2(puzzle_input):
    return len(enhance(puzzle_input, 50))

def solve(puzzle_input):
    return d20p1(puzzle_input), d20p2(puzzle_input)
