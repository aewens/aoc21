def parse(puzzle_input):
    target = dict()
    line = puzzle_input[0]
    prefix, data = line.split(": ", 1)
    xdata, ydata = data.split(", ", 1)
    min_x, max_x = xdata[2:].split("..", 1)
    min_y, max_y = ydata[2:].split("..", 1)

    target["min_x"] = int(min_x)
    target["max_x"] = int(max_x)
    target["min_y"] = int(min_y)
    target["max_y"] = int(max_y)

    return target

def step(position, velocity, target):
    min_x = target["min_x"]
    max_x = target["max_x"]
    min_y = target["min_y"]
    max_y = target["max_y"]

    px, py = position
    vx, vy = velocity
    drag = 0
    if vx > 0:
        drag = 1

    elif vx < 0:
        drag = -1

    nx, ny = px+vx, py+vy
    new_pos = nx, ny
    new_vel = vx-drag, vy-1

    if nx < min_x:
        return new_pos, new_vel, False

    if nx > max_x:
        return new_pos, new_vel, False

    if ny < min_y:
        return new_pos, new_vel, False

    if ny > max_y:
        return new_pos, new_vel, False

    return new_pos, new_vel, True

def check(pos, vel, target, debug=False):
    max_y = 0
    min_y = target["min_y"]
    while True:
        pos, vel, reached = step(pos, vel, target)
        max_y = max(max_y, pos[1])
        if debug:
            print(pos, vel, max_y, reached)

        if pos[1] < min_y:
            return False, max_y

        if reached:
            return True, max_y

def find_x(target):
    n = 0
    dn = 1
    op = lambda a, b: a > b
    mx = target["min_x"]
    if mx < 0:
        dn = -1
        op = lambda a, b: a < b
        mx = target["max_x"]

    while True:
        x = sum(range(n+dn))
        if op(x, mx):
            return n

        n = n + dn

def find_y(target, x):
    n = 1
    dn = 1
    min_y = target["min_y"]
    max_y = sum(range(abs(min_y)))

    while True:
        y = sum(range(n+dn))
        if y > max_y and check((0, 0), (x, n-1), target)[0]:
            return n-1

        n = n + dn

def d17p1(puzzle_input):
    target = parse(puzzle_input)

    vx = find_x(target)
    vy = find_y(target, vx)

    pos = 0, 0
    vel = vx, vy
    max_y = check(pos, vel, target)[1]
    return max_y

def d17p2(puzzle_input):
    target = parse(puzzle_input)
    min_x = target["min_x"]
    max_x = target["max_x"]
    min_y = target["min_y"]
    max_y = target["max_y"]

    pos = 0, 0
    vx = find_x(target)
    vy = find_y(target, vx)

    count = (abs(max_x-min_x)+1)*(abs(max_y-min_y)+1)
    for y in range(max_y+1, vy+1):
        for x in range(max_x+1):
            if check(pos, (x, y), target)[0]:
                count = count + 1

    return count

def solve(puzzle_input):
    return d17p1(puzzle_input), d17p2(puzzle_input)
