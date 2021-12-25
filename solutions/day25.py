EAST = 1
SOUTH = 2

def parse(lines):
    width = -1
    height = -1
    easts = dict()
    souths = dict()
    for y, line in enumerate(lines):
        if len(line) == 0:
            continue

        height = max(height, y)
        for x, char in enumerate(line):
            width = max(width, x)
            yx = y, x
            if char == ".":
                continue

            if char == ">":
                easts[yx] = True
                continue

            if char == "v":
                souths[yx] = True
                continue

    return easts, souths, width+1, height+1

def move(mode, y, x, w, h):
    if mode == EAST:
        return (y, 0) if x+1 == w else (y, x+1)

    if mode == SOUTH:
        return (0, x) if y+1 == h else (y+1, x)

def step(es, ss, w, h):
    nes = dict()
    nss = dict()
    changed = False
    for (ey, ex) in es.keys():
        eyx = ey, ex
        em = move(EAST, ey, ex, w, h)
        if es.get(em) is None and ss.get(em) is None:
            nes[em] = True
            changed = True

        else:
            nes[eyx] = True

    for (sy, sx) in ss:
        syx = sy, sx
        sm = move(SOUTH, sy, sx, w, h)
        if nes.get(sm) is None and ss.get(sm) is None:
            nss[sm] = True
            changed = True

        else:
            nss[syx] = True

    return nes, nss, changed

def d25p1(puzzle_input):
    easts, souths, width, height = parse(puzzle_input)
    i = 0
    while True:
        easts, souths, changed = step(easts, souths, width, height)
        i = i + 1
        if not changed:
            break

    return i

def d25p2(puzzle_input):
    return None

def solve(puzzle_input):
    return d25p1(puzzle_input), d25p2(puzzle_input)

