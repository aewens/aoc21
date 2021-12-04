def parse_game(lines):
    numbers = list()
    for number in lines[0].split(","):
        numbers.append(number)

    board = list()
    boards = list()
    for line in lines[2:]:
        if len(line) == 0:
            boards.append(board)
            board = list()
            continue

        board.append(line.split())

    boards.append(board)
    return numbers, boards

def check_rows(numbers, board):
    for row in board:
        found = list()
        for col in row:
            if col in numbers:
                found.append(col)

        if len(found) == len(row):
            return True

    return False

def check_cols(numbers, board):
    cols = len(board)
    for c in range(cols):
        found = list()
        for row in board:
            col = row[c]
            if col in numbers:
                found.append(col)

        if len(found) == cols:
            return True

    return False

def next_turn(numbers, boards, used=list()):
    used.append(numbers[0])
    numbers = numbers[1:]
    for board in boards:
        rows = check_rows(used, board)
        if rows:
            return True, used, numbers, board

        cols = check_cols(used, board)
        if cols:
            return True, used, numbers, board

    return False, used, numbers, None

def play_game(numbers, boards, used=list(), state=dict()):
    used.append(numbers[0])
    numbers = numbers[1:]
    for b, board in enumerate(boards):
        if state.get(b) is not None:
            continue

        rows = check_rows(used, board)
        if rows:
            state[b] = len(used)
            continue

        cols = check_cols(used, board)
        if cols:
            state[b] = len(used)
            continue

    return state, used, numbers

def get_score(used, board):
    unmarked = list()
    for row in board:
        for col in row:
            if col not in used:
                unmarked.append(int(col))

    return sum(unmarked) * int(used[-1])

def d4p1(puzzle_input):
    numbers, boards = parse_game(puzzle_input)

    won = False
    used = list()
    board = None
    while not won:
        won, used, numbers, board = next_turn(numbers, boards, used)

    if board is None:
        return None

    return get_score(used, board)

def d4p2(puzzle_input):
    numbers, boards = parse_game(puzzle_input)

    used = list()
    state = dict()
    while len(state) < len(boards):
        state, used, numbers = play_game(numbers, boards, used, state)

    last_turn = max(state.values())
    last_board = None
    for key, value in state.items():
        if value == last_turn:
            last_board = boards[key]

    return get_score(used, last_board)

def solve(puzzle_input):
    return d4p1(puzzle_input), d4p2(puzzle_input)
