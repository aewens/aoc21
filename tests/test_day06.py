from .context import get_puzzle, get_solution_script

index = 6
INPUT = """
3,4,3,1,2
"""[1:-1].split("\n")

def test_d6p1():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d6p1 = script("d6p1")
    assert d6p1 is not None, "d6p1 is none"

    result = d6p1(INPUT)
    assert result == 5934, f"result is not 5934: {result}"

def test_d6p2():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d6p2 = script("d6p2")
    assert d6p2 is not None, "d6p2 is none"

    result = d6p2(INPUT)
    assert result == 26984457539, f"result is not 26984457539: {result}"
