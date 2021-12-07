from .context import get_puzzle, get_solution_script

index = 7
INPUT = """
16,1,2,0,4,2,7,1,2,14
"""[1:-1].split("\n")

def test_d7p1():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d7p1 = script("d7p1")
    assert d7p1 is not None, "d7p1 is none"

    result = d7p1(INPUT)
    assert result == 37, f"result is not 37: {result}"

def test_d7p2():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d7p2 = script("d7p2")
    assert d7p2 is not None, "d7p2 is none"

    result = d7p2(INPUT)
    assert result == 168, f"result is not 168: {result}"
