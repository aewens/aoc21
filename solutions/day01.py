def d1p2(puzzle_input):
    window = list()
    score = 0
    prev = None
    for depth in puzzle_input:
        window.append(int(depth))
        if len(window) < 3:
            continue

        curr = sum(window)
        if prev is not None and curr > prev:
            score = score + 1

        prev = curr
        window.pop(0)

    return score

def solve(puzzle_input):
    prev = None
    score = 0
    for depth in puzzle_input:
        curr = int(depth)
        if prev is not None and curr > prev:
            score = score + 1

        prev = curr

    return score, d1p2(puzzle_input)

