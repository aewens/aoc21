from .context import get_puzzle, get_solution_script

index = 1

def test_d1p2():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d1p2 = script("d1p2")
    assert d1p2 is not None, "d1p2 is none"

    puzzle = "199 200 208 210 200 207 240 269 260 263".split()
    result = d1p2(puzzle)
    assert result == 5, f"result is not 5: {result}"
