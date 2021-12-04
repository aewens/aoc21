from collections import defaultdict

def search(lines, find=0, index=0):
    if len(lines) == 1:
        return int(lines[0], 2)

    ones = 0
    zeros = 0
    omap = list()
    zmap = list()
    for line in lines:
        bit = line[index]
        if bit == "1":
            ones = ones + 1
            omap.append(line)

        else:
            zeros = zeros + 1
            zmap.append(line)

    if ones == zeros:
        return search(omap if find == 1 else zmap, find=find, index=index+1)

    if find == 1:
        if ones > zeros:
            return search(omap, find=find, index=index+1)

        return search(zmap, find=find, index=index+1)

    else:
        if ones < zeros:
            return search(omap, find=find, index=index+1)

        return search(zmap, find=find, index=index+1)

def d3p1(puzzle_input):
    gamma = ""
    epsilon = ""
    ones = defaultdict(lambda: 0)
    zeros = defaultdict(lambda: 0)
    for line in puzzle_input:
        for i, bit in enumerate(line):
            if bit == "1":
                ones[i] = ones[i] + 1

            else:
                zeros[i] = zeros[i] + 1

    for index in range(len(ones)):
        ocount = ones[index]
        zcount = zeros[index]
        if ocount > zcount:
            gamma = gamma + "1"
            epsilon = epsilon + "0"

        else:
            gamma = gamma + "0"
            epsilon = epsilon + "1"

    return int(gamma, 2) * int(epsilon, 2)

def d3p2(puzzle_input):
    return search(puzzle_input, find=0) * search(puzzle_input, find=1)

def solve(puzzle_input):
    return d3p1(puzzle_input), d3p2(puzzle_input)
