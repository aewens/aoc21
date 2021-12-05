from .context import get_puzzle, get_solution_script

index = 5
INPUT = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""[1:-1].split("\n")

def test_d5p1():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d5p1 = script("d5p1")
    assert d5p1 is not None, "d5p1 is none"

    result = d5p1(INPUT)
    assert result == 5, f"result is not 5: {result}"

def test_d5p2():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d5p2 = script("d5p2")
    assert d5p2 is not None, "d5p2 is none"

    result = d5p2(INPUT)
    assert result == 12, f"result is not 12: {result}"
