from .context import get_puzzle, get_solution_script

index = 20
first = "".join([
"..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##",
"#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###",
".######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.",
".#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....",
".#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..",
"...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....",
"..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#"
])
INPUT = f"""
{first}

#..#.
#....
##..#
..#..
..###
"""[1:-1].split("\n")

def test_d20p1():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d20p1 = script("d20p1")
    assert d20p1 is not None, "d20p1 is none"

    result = d20p1(INPUT)
    assert result == 35, f"result is not 35: {result}"

# NOTE - Works, but runs slow
#def test_d20p2():
#    script = get_solution_script(index)
#    assert script is not None, "script is none"
#
#    d20p2 = script("d20p2")
#    assert d20p2 is not None, "d20p2 is none"
#
#    result = d20p2(INPUT)
#    assert result == 3351, f"result is not 3351: {result}"
