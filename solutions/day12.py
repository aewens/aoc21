from collections import defaultdict

def parse(puzzle_input):
    links = defaultdict(list)
    for line in puzzle_input:
        head, tail = line.split("-", 1)
        links[head].append(tail)
        links[tail].append(head)

    return links

def is_big(cave):
    return 65 <= ord(cave[0]) <= 90

def walk(links, point, seen):
    if point == "end":
        return 1

    if not is_big(point) and seen.get(point, False):
        return 0

    ends = 0
    seen[point] = True
    for path in links[point]:
        ended = walk(links, path, {k: v for k, v in seen.items()})
        ends = ends + ended

    return ends

def check(point, seen):
    twice = seen.get("_twice", False)
    if point == "start" and seen.get(point, False):
        return False

    if not is_big(point) and seen.get(point, False):
        if not twice:
            seen["_twice"] = True
            return True

        return False

    return True

def traverse(links, point, seen):
    if point == "end":
        return 1

    if not check(point, seen):
        return 0

    ends = 0
    seen[point] = True
    for path in links[point]:
        ended = traverse(links, path, {k: v for k, v in seen.items()})
        ends = ends + ended

    return ends

def d12p1(puzzle_input):
    seen = dict()
    links = parse(puzzle_input)
    return walk(links, "start", seen)

def d12p2(puzzle_input):
    seen = dict()
    links = parse(puzzle_input)
    return traverse(links, "start", seen)

def solve(puzzle_input):
    return d12p1(puzzle_input), d12p2(puzzle_input)
