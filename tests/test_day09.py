from .context import get_puzzle, get_solution_script

index = 9
INPUT = """
2199943210
3987894921
9856789892
8767896789
9899965678
"""[1:-1].split("\n")

def test_d9p1():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    glp = script("get_low_points")
    assert glp is not None, "get_low_points is none"

    low_points = glp(INPUT)
    assert sorted(low_points) == [0,1,5,5], f"low_points is: {low_points}"

    d9p1 = script("d9p1")
    assert d9p1 is not None, "d9p1 is none"

    result = d9p1(INPUT)
    assert result == 15, f"result is not 15: {result}"

def test_d9p2():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    parse = script("parse")
    assert parse is not None, "parse is none"

    check = script("check_neighbors")
    assert check is not None, "check_neighbors is none"

    points = parse(INPUT)
    basin, seen = check(points, 0, 0, dict())

    assert len(basin) == 3, f"basin is: {basin}"

    d9p2 = script("d9p2")
    assert d9p2 is not None, "d9p2 is none"

    result = d9p2(INPUT)
    assert result == 1134, f"result is not 1134: {result}"
