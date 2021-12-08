def resolve(wires):
    resolved = dict()
    iresolved = dict()

    remap = dict()
    remap[2] = 1
    remap[3] = 7
    remap[4] = 4
    remap[7] = 8

    fives = list()
    sixes = list()
    common = dict()

    # First pass
    for wire in wires:
        size = len(wire)
        name = remap.get(size)
        if name is None:
            if size == 5:
                fives.append(wire)

            elif size == 6:
                sixes.append(wire)

            continue

        resolved[wire] = str(name)
        iresolved[name] = wire
        for w in wire:
            if common.get(w) is None:
                common[w] = 0

            common[w] = common[w] + 1

    side = list()
    for key, value in common.items():
        if value == 4:
            side.append(key)

    # Second pass
    middle = None
    for wire in fives:
        if side[0] in wire and side[1] in wire:
            resolved[wire] = "3"
            iresolved[3] = wire
            four = iresolved[4]
            for w in wire:
                if w in side or w not in four:
                    continue

                middle = w
                break

    # Third pass
    leg = None
    for wire in sixes:
        if middle not in wire:
            resolved[wire] = "0"
            iresolved[0] = wire
            continue

        if side[0] in wire and side[1] in wire:
            resolved[wire] = "9"
            iresolved[9] = wire
            eight = iresolved[8]
            for e in eight:
                if e not in wire:
                    leg = e
                    break

        else:
            resolved[wire] = "6"
            iresolved[6] = wire

    # Fourth pass
    three = iresolved[3]
    for wire in fives:
        if wire == three:
            continue

        if leg in wire:
            resolved[wire] = "2"
            iresolved[2] = wire

        else:
            resolved[wire] = "5"
            iresolved[5] = wire

    return resolved

def parse(puzzle_input):
    result = list()
    for line in puzzle_input:
        wires, numbers = line.split(" | ", 1)
        resolved = resolve(["".join(sorted(w)) for w in wires.split()])
        display = ""
        for number in numbers.split():
            num = "".join(sorted(number))
            display = display + resolved[num]

        result.append(int(display))

    return result

def d8p1(puzzle_input):
    count = 0
    for line in puzzle_input:
        head, tail = line.split(" | ", 1)
        for part in tail.split():
            size = len(part)
            if size in [2,3,4,7]:
                count = count + 1

    return count

def d8p2(puzzle_input):
    return sum(parse(puzzle_input))

def solve(puzzle_input):
    return d8p1(puzzle_input), d8p2(puzzle_input)

