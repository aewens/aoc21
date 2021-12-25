from .context import get_puzzle, get_solution_script

index = 25
INPUT = """
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
"""[1:-1].split("\n")

def test_d25p1():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d25p1 = script("d25p1")
    assert d25p1 is not None, "d25p1 is none"

    result = d25p1(INPUT)
    assert result == 58, f"result is not 58: {result}"

#def test_d25p2():
#    script = get_solution_script(index)
#    assert script is not None, "script is none"
#
#    d25p2 = script("d25p2")
#    assert d25p2 is not None, "d25p2 is none"
#
#    result = d25p2(INPUT)
#    expecting = 2758514936282235
#
#    assert result == expecting, f"result is not {expecting}: {result}"
