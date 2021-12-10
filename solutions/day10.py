from collections import defaultdict

ANGLE = 0
CURLY = 1
ROUND = 3
SQUARE = 4

remap = dict()
remap["<"] = ANGLE
remap[">"] = ANGLE
remap["{"] = CURLY
remap["}"] = CURLY
remap["("] = ROUND
remap[")"] = ROUND
remap["["] = SQUARE
remap["]"] = SQUARE

closes = dict()
closes[ANGLE] = ">"
closes[CURLY] = "}"
closes[ROUND] = ")"
closes[SQUARE] = "]"

def validate(puzzle_input):
    invalids = defaultdict(lambda: 0)
    completes = list()
    for line in puzzle_input:
        opened = list()
        state = defaultdict(lambda: 0)
        complete = ""
        invalid = False
        for bracket in line:
            if bracket in "<{([":
                resolved = remap[bracket]
                opened.append(resolved)
                state[resolved] = state[resolved] + 1

            if bracket in ">})]":
                last = opened.pop()
                resolved = remap[bracket]
                if last != resolved:
                    invalids[resolved] = invalids[resolved] + 1
                    invalid = True
                    break

                if state[last] == 0:
                    invalids[resolved] = invalids[resolved] + 1
                    invalid = True
                    break

                state[last] = state[last] - 1

        if invalid:
            continue

        for i in range(len(opened)):
            last = opened.pop()
            close = closes[last]
            complete = complete + close

        if len(complete) > 0:
            completes.append(complete)

    return invalids, completes

def d10p1(puzzle_input):
    scores = dict()
    scores[ROUND] = 3
    scores[SQUARE] = 57
    scores[CURLY] = 1197
    scores[ANGLE] = 25137

    invalids, _ = validate(puzzle_input)
    return sum(scores[key] * value for key, value in invalids.items())

def d10p2(puzzle_input):
    scores = dict()
    scores[")"] = 1
    scores["]"] = 2
    scores["}"] = 3
    scores[">"] = 4

    _, completes = validate(puzzle_input)
    tallys = list()
    for brackets in completes:
        tally = 0
        for bracket in brackets:
            tally = tally * 5 + scores[bracket]

        tallys.append(tally)

    return sorted(tallys)[(len(tallys)//2)]

def solve(puzzle_input):
    return d10p1(puzzle_input), d10p2(puzzle_input)
