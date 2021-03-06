from math import sqrt

def parse(puzzle_input):
    subs = list()
    for sub in puzzle_input[0].split(","):
        subs.append(int(sub))

    return subs

def gauss(n):
    # Optimized sum of all 0 to n
    return int((n * (n + 1)) / 2)

def d7p1(puzzle_input):
    subs = parse(puzzle_input)
    fuel = dict()
    mean = int(sum(subs)/len(subs))
    sd = int(sqrt(sum(subs)/mean))
    start = mean-sd
    end = mean+sd+1
    for s in range(start,end):
        fuel[s] = 0
        for sub in subs:
            fuel[s] = fuel[s] + abs(s-sub)

    return min(fuel.values())

def d7p2(puzzle_input):
    subs = parse(puzzle_input)
    fuel = dict()
    mean = int(sum(subs)/len(subs))
    sd = int(sqrt(sum(subs)/mean))
    start = mean-sd
    end = mean+sd+1
    for s in range(start,end):
        fuel[s] = 0
        for sub in subs:
            fuel[s] = fuel[s] + gauss(abs(s-sub))

    return min(fuel.values())

def solve(puzzle_input):
    return d7p1(puzzle_input), d7p2(puzzle_input)
