from .context import get_puzzle, get_solution_script

index = 10
INPUT = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""[1:-1].split("\n")

def test_d10p1():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d10p1 = script("d10p1")
    assert d10p1 is not None, "d10p1 is none"

    result = d10p1(INPUT)
    assert result == 26397, f"result is not 26397: {result}"

def test_d10p2():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d10p2 = script("d10p2")
    assert d10p2 is not None, "d10p2 is none"

    result = d10p2(INPUT)
    assert result == 288957, f"result is not 288957: {result}"
