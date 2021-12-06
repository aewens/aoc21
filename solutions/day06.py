from collections import defaultdict

def parse(puzzle_input):
    counts = defaultdict(lambda: 0)
    for count in puzzle_input[0].split(","):
        counts[int(count)] = counts[int(count)] + 1

    return counts

def step(counts):
    next_counts = defaultdict(lambda: 0)
    for key, value in counts.items():
        if key == 0:
            next_counts[6] = next_counts[6] + value
            next_counts[8] = next_counts[8] + value
            continue

        next_counts[key-1] = next_counts[key-1] + value

    return next_counts

def d6p1(puzzle_input):
    counts = parse(puzzle_input)
    for i in range(80):
        counts = step(counts)

    return sum(counts.values())

def d6p2(puzzle_input):
    counts = parse(puzzle_input)
    for i in range(256):
        counts = step(counts)

    return sum(counts.values())

def solve(puzzle_input):
    return d6p1(puzzle_input), d6p2(puzzle_input)

