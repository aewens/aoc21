from collections import defaultdict

def parse(puzzle_input):
    mode = 0
    rules = dict()
    polymer = defaultdict(lambda: 0)
    count = defaultdict(lambda: 0)

    for line in puzzle_input:
        if len(line) == 0:
            mode = 1
            continue

        if mode == 0:
            for i in range(len(line)-1):
                pair = line[i:i+2]
                polymer[pair] = polymer[pair] + 1

            for char in line:
                count[char] = count[char] + 1

            continue

        head, tail = line.split(" -> ", 1)
        rules[head] = [f"{head[0]}{tail}", f"{tail}{head[1]}"]

    return polymer, count, rules

def step(polymer, count, rules):
    new_polymer = defaultdict(lambda: 0)
    for pair, amount in polymer.items():
        insert = rules.get(pair)
        if not insert:
            new_polymer[pair] = new_polymer[pair] + amount
            continue

        middle = insert[0][1]
        count[middle] = count[middle] + amount
        for ipair in insert:
            new_polymer[ipair] = new_polymer[ipair] + amount

    return new_polymer, count

def d14p1(puzzle_input):
    polymer, count, rules = parse(puzzle_input)
    for i in range(10):
        polymer, count = step(polymer, count, rules)

    return max(count.values()) - min(count.values())

def d14p2(puzzle_input):
    polymer, count, rules = parse(puzzle_input)
    for i in range(40):
        polymer, count = step(polymer, count, rules)

    return max(count.values()) - min(count.values())

def solve(puzzle_input):
    return d14p1(puzzle_input), d14p2(puzzle_input)
