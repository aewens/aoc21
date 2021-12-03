from .context import get_puzzle, get_solution_script

index = 2
INPUT = [
"forward 5",
"down 5",
"forward 8",
"up 3",
"down 8",
"forward 2"
]

def test_d2p1():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d2p1 = script("d2p1")
    assert d2p1 is not None, "d2p1 is none"

    result = d2p1(INPUT)
    assert result == 150, f"result is not 150: {result}"

def test_d2p2():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d2p2 = script("d2p2")
    assert d2p2 is not None, "d2p2 is none"

    result = d2p2(INPUT)
    assert result == 900, f"result is not 900: {result}"
