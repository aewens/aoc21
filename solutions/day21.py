def parse(lines):
    player1 = int(lines[0].split(": ", 1)[1])-1
    player2 = int(lines[1].split(": ", 1)[1])-1
    return player1, player2

def d21p1(puzzle_input):
    p1, p2 = parse(puzzle_input)
    dice = 1
    rolls = 0
    scores = 0, 0
    turn = 0
    while scores[0] < 1000 and scores[1] < 1000:
        rolls = rolls+3
        move = dice*3+3
        dice = dice+3
        if turn == 0:
            p1 = (p1 + move) % 10
            scores = scores[0]+p1+1, scores[1]

        else:
            p2 = (p2 + move) % 10
            scores = scores[0], scores[1]+p2+1

        turn = (turn + 1) % 2

    return rolls * min(scores)

def quantum(p1, s1, p2, s2, e, memo=dict()):
    if s1 >= e:
        return 1, 0

    if s2 >= e:
        return 0, 1

    w1s, w2s = 0, 0
    for a in range(3):
        for b in range(3):
            for c in range(3):
                move = a+1 + b+1 + c+1

                p = (p1 + move) % 10
                s = s1 + p + 1

                args = p2, s2, p, s, e
                result = memo.get(args)
                if result is None:
                    result = quantum(*args, memo)
                    memo[args] = result

                w2, w1 = result
                w2s = w2s + w2
                w1s = w1s + w1

    return w1s, w2s

def d21p2(puzzle_input):
    p1, p2 = parse(puzzle_input)
    return max(quantum(p1, 0, p2, 0, 21))

def solve(puzzle_input):
    return d21p1(puzzle_input), d21p2(puzzle_input)
