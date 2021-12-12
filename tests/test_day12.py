from .context import get_puzzle, get_solution_script
from collections import defaultdict

index = 12
SAMPLE1 = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""[1:-1].split("\n")

SAMPLE2 = """
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""[1:-1].split("\n")

INPUT = """
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""[1:-1].split("\n")

def test_d12p1():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d12p1 = script("d12p1")
    assert d12p1 is not None, "d12p1 is none"

    demo1 = d12p1(SAMPLE1)
    assert demo1 == 10, f"demo1 is not 10: {demo1}"

    demo2 = d12p1(SAMPLE2)
    assert demo2 == 19, f"demo2 is not 19: {demo2}"

    result = d12p1(INPUT)
    assert result == 226, f"result is not 226: {result}"

def test_d12p2():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d12p2 = script("d12p2")
    assert d12p2 is not None, "d12p2 is none"

    demo1 = d12p2(SAMPLE1)
    assert demo1 == 36, f"demo1 is not 36: {demo1}"

    demo2 = d12p2(SAMPLE2)
    assert demo2 == 103, f"demo2 is not 103: {demo2}"

    result = d12p2(INPUT)
    assert result == 3509, f"result is not 3509: {result}"
