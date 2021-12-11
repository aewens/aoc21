from .context import get_puzzle, get_solution_script
from collections import defaultdict

index = 11
SAMPLE = """
11111
19991
19191
19991
11111
"""[1:-1].split("\n")

INPUT = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""[1:-1].split("\n")

def checksum(grid):
    count = defaultdict(lambda: 0)
    for energy in grid.values():
        count[energy] = count[energy] + 1

    result = list()
    for i in range(10):
        result.append(f"{i}:{count[i]}")

    return ",".join(result)

def test_d11p1():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    parse = script("parse")
    assert parse is not None, "parse is none"

    step = script("step")
    assert step is not None, "step is none"

    checks = [
        "0:9,1:0,2:0,3:4,4:8,5:4,6:0,7:0,8:0,9:0",
        "0:0,1:9,2:0,3:0,4:4,5:8,6:4,7:0,8:0,9:0"
    ]

    grid, flashed = step(parse(SAMPLE))
    check = checksum(grid)
    assert flashed == 9, f"flashed is not 9: {flashed}"
    assert check == checks[0], f"check is not {checks[0]}: {check}"

    grid, flashed = step(grid)
    check = checksum(grid)
    assert flashed == 0, f"flashed is not 0: {flashed}"
    assert check == checks[1], f"check is not {checks[1]}: {check}"

    d11p1 = script("d11p1")
    assert d11p1 is not None, "d11p1 is none"

    result = d11p1(INPUT)
    assert result == 1656, f"result is not 1656: {result}"

def test_d11p2():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d11p2 = script("d11p2")
    assert d11p2 is not None, "d11p2 is none"

    result = d11p2(INPUT)
    assert result == 195, f"result is not 195: {result}"
