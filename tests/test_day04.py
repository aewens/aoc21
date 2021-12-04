from .context import get_puzzle, get_solution_script

index = 4
INPUT = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""[1:-1].split("\n")

def test_d4p1():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d4p1 = script("d4p1")
    assert d4p1 is not None, "d4p1 is none"

    result = d4p1(INPUT)
    assert result == 4512, f"result is not 4512: {result}"

def test_d4p2():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d4p2 = script("d4p2")
    assert d4p2 is not None, "d4p2 is none"

    result = d4p2(INPUT)
    assert result == 1924, f"result is not 1924: {result}"
