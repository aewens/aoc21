from .context import get_puzzle, get_solution_script

index = 21
INPUT = """
Player 1 starting position: 4
Player 2 starting position: 8
"""[1:-1].split("\n")

def test_d21p1():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d21p1 = script("d21p1")
    assert d21p1 is not None, "d21p1 is none"

    result = d21p1(INPUT)
    assert result == 739785, f"result is not 739785: {result}"

def test_d21p2():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d21p2 = script("d21p2")
    assert d21p2 is not None, "d21p2 is none"

    result = d21p2(INPUT)
    assert result == 444356092776315, f"result is not 444356092776315: {result}"
