def parse(line):
    command, amount = line.split(" ", 1)
    resolve = dict()
    resolve["forward"] = "x", 1
    resolve["down"] = "y", 1
    resolve["up"] = "y", -1

    action = resolve.get(command)
    if action is None:
        raise ValueError(f"Invalid command: {command}")

    return action, int(amount)

def d2p1(puzzle_input):
    loc = {"x": 0, "y": 0}
    for line in puzzle_input:
        action, amount = parse(line)
        coord, direction = action
        loc[coord] = loc[coord] + (direction * amount)

    return loc["x"] * loc["y"]

def d2p2(puzzle_input):
    loc = {"x": 0, "y": 0, "a": 0}
    for line in puzzle_input:
        command, amt = line.split(" ", 1)
        amount = int(amt)

        if command == "down":
            loc["a"] = loc["a"] + amount

        elif command == "up":
            loc["a"] = loc["a"] - amount

        elif command == "forward":
            loc["x"] = loc["x"] + amount
            loc["y"] = loc["y"] + (loc["a"] * amount)

    return loc["x"] * loc["y"]

def solve(puzzle_input):
    return d2p1(puzzle_input), d2p2(puzzle_input)

