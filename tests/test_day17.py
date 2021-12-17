from .context import get_puzzle, get_solution_script

index = 17
INPUT = """
target area: x=20..30, y=-10..-5
"""[1:-1].split("\n")


def test_d17p1():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d17p1 = script("d17p1")
    assert d17p1 is not None, "d17p1 is none"

    result = d17p1(INPUT)
    assert result == 45, f"result is not 45: {result}"

def test_d17p2():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d17p2 = script("d17p2")
    assert d17p2 is not None, "d17p2 is none"

    result = d17p2(INPUT)
    assert result == 112, f"result is not 112: {result}"
