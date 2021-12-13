from .context import get_puzzle, get_solution_script
from collections import defaultdict

index = 13
INPUT = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""[1:-1].split("\n")

def test_d13p1():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d13p1 = script("d13p1")
    assert d13p1 is not None, "d13p1 is none"

    result = d13p1(INPUT)
    assert result == 17, f"result is not 17: {result}"

#def test_d13p2():
#    script = get_solution_script(index)
#    assert script is not None, "script is none"
#
#    d13p2 = script("d13p2")
#    assert d13p2 is not None, "d13p2 is none"
#
#    result = d13p2(INPUT)
#    assert result == 3509, f"result is not 3509: {result}"
