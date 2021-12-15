from .context import get_puzzle, get_solution_script
from collections import defaultdict

index = 15
INPUT = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""[1:-1].split("\n")

def test_d15p1():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d15p1 = script("d15p1")
    assert d15p1 is not None, "d15p1 is none"

    result = d15p1(INPUT)
    assert result == 40, f"result is not 40: {result}"

def test_d16p2():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d15p2 = script("d15p2")
    assert d15p2 is not None, "d15p2 is none"

    result = d15p2(INPUT)
    assert result == 315, f"result is not 315: {result}"
