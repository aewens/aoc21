from math import floor, ceil
from json import loads
from functools import reduce
from itertools import permutations

def apply_left(pair, value):
    if value is None:
        return pair

    if isinstance(pair, int):
        #print(pair, value)
        return pair + value

    return [apply_left(pair[0], value), pair[1]]

def apply_right(pair, value):
    if value is None:
        return pair

    if isinstance(pair, int):
        return pair + value

    return [pair[0], apply_right(pair[1], value)]

def explode(value, level=4):
    if isinstance(value, int):
        return False, value, None, None

    if level == 0:
        return True, 0, value[0], value[1]

    changed, new_left, left, right = explode(value[0], level-1)
    if changed:
        return True, [new_left, apply_left(value[1], right)], left, None

    changed, new_right, left, right = explode(value[1], level-1)
    if changed:
        return True, [apply_right(new_left, left), new_right], None, right

    return False, value, None, None

def split(value):
    if isinstance(value, int):
        if value >= 10:
            return True, [floor(value / 2), ceil(value / 2)]

        return False, value

    changed, left = split(value[0])
    if changed:
        return True, [left, value[1]]

    changed, right = split(value[1])
    return changed, [left, right]

def merge(a, b):
    pair = [a, b]
    while True:
        #changed = False
        #if pair.depth >= 4:
        changed, pair, left, right = explode(pair)
        if changed:
            continue

        #if pair.max_value >= 10:
        changed, pair = split(pair)

        if not changed:
            break

    return pair

def add(prev, curr):
    return merge(prev, curr)

def load(puzzle_input):
    pairs = list()
    for line in puzzle_input:
        if len(line) == 0:
            continue

        pairs.append(loads(line))

    return pairs

def process(puzzle_input):
    pairs = load(puzzle_input)
    return reduce(add, pairs)

def magnitude(value):
    if isinstance(value, int):
        return value

    left = 3 * magnitude(value[0])
    right = 2 * magnitude(value[1])
    return left + right

def d18p1(puzzle_input):
    return magnitude(process(puzzle_input))

def d18p2(puzzle_input):
    pairs = load(puzzle_input)
    return max(magnitude(add(a, b)) for a, b in permutations(pairs, 2))

def solve(puzzle_input):
    return d18p1(puzzle_input), d18p2(puzzle_input)
