from .context import get_puzzle, get_solution_script

index = 3
INPUT = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""[1:-1].split("\n")

def test_d3p1():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d3p1 = script("d3p1")
    assert d3p1 is not None, "d3p1 is none"

    result = d3p1(INPUT)
    assert result == 198, f"result is not 198: {result}"

def test_d3p2():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d3p2 = script("d3p2")
    assert d3p2 is not None, "d3p2 is none"

    result = d3p2(INPUT)
    assert result == 230, f"result is not 230: {result}"
