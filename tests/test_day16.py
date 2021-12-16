from .context import get_puzzle, get_solution_script

index = 16
SAMPLE1 = """
D2FE28
"""[1:-1].split("\n")
SAMPLE2 = """
38006F45291200
"""[1:-1].split("\n")
SAMPLE3 = """
EE00D40C823060
"""[1:-1].split("\n")
SAMPLE4 = """
8A004A801A8002F478
"""[1:-1].split("\n")
SAMPLE5 = """
620080001611562C8802118E34
"""[1:-1].split("\n")
INPUT1 = """
A0016C880162017C3686B18A3D4780
"""[1:-1].split("\n")
INPUT2 = """
9C0141080250320F1802104A08
"""[1:-1].split("\n")


def test_d16p1():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d16p1 = script("d16p1")
    assert d16p1 is not None, "d16p1 is none"

    demo1 = d16p1(SAMPLE1)
    assert demo1 == 6, f"demo1 is not 6: {demo1}"

    demo2 = d16p1(SAMPLE2)
    assert demo2 == 9, f"demo2 is not 9: {demo2}"

    demo3 = d16p1(SAMPLE3)
    assert demo3 == 14, f"demo3 is not 14: {demo3}"

    demo4 = d16p1(SAMPLE4)
    assert demo4 == 16, f"demo4 is not 16: {demo4}"

    demo5 = d16p1(SAMPLE5)
    assert demo5 == 12, f"demo5 is not 16: {demo5}"

    result = d16p1(INPUT1)
    assert result == 31, f"result is not 31: {result}"

def test_d16p2():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d16p2 = script("d16p2")
    assert d16p2 is not None, "d16p2 is none"

    result = d16p2(INPUT2)
    assert result == 1, f"result is not 1: {result}"
