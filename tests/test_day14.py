from .context import get_puzzle, get_solution_script
from collections import defaultdict

index = 14
INPUT = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""[1:-1].split("\n")

def test_d14p1():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d14p1 = script("d14p1")
    assert d14p1 is not None, "d14p1 is none"

    result = d14p1(INPUT)
    assert result == 1588, f"result is not 1588: {result}"

def test_d14p2():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d14p2 = script("d14p2")
    assert d14p2 is not None, "d14p2 is none"

    result = d14p2(INPUT)
    assert result == 2188189693529, f"result is not 2188189693529: {result}"
