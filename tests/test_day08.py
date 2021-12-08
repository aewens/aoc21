from .context import get_puzzle, get_solution_script

index = 8
INPUT = """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""[1:-1].split("\n")

SAMPLE = [" | ".join([
    "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab",
    "cdfeb fcadb cdfeb cdbaf"
])]

def test_d8p1():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d8p1 = script("d8p1")
    assert d8p1 is not None, "d8p1 is none"

    result = d8p1(INPUT)
    assert result == 26, f"result is not 26: {result}"

def test_d8p2():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d8p2 = script("d8p2")
    assert d8p2 is not None, "d8p2 is none"

    sample = d8p2(SAMPLE)
    assert sample == 5353, f"sample is not 5353: {sample}"

    result = d8p2(INPUT)
    assert result == 61229, f"result is not 61229: {result}"
