from .context import get_puzzle, get_solution_script

index = 18
SAMPLE1 = """
[[1,2],[[3,4],5]]
"""[1:-1].split("\n")
SAMPLE2 = """
[[[[0,7],4],[[7,8],[6,0]]],[8,1]]
"""[1:-1].split("\n")
SAMPLE3 = """
[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]
"""[1:-1].split("\n")
SAMPLE4 = """
[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]
"""[1:-1].split("\n")
SAMPLE5 = """
[[[[4,3],4],4],[7,[[8,4],9]]]
[1,1]
"""[1:-1].split("\n")
INPUT = """
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
"""[1:-1].split("\n")

def test_d18p1():
    script = get_solution_script(index)
    assert script is not None, "script is none"

    d18p1 = script("d18p1")
    assert d18p1 is not None, "d18p1 is none"

    #load = script("load")
    #assert load is not None, "load is none"
    #step = script("step")
    #assert step is not None, "step is none"
    #magnitude = script("magnitude")
    #assert magnitude is not None, "magnitude is none"

    ###expecting = [2736, 4014, 4105, 4293, 3496, 2922, 3705, 3549, 3488]

    #demo1 = magnitude(load(SAMPLE1)[0])
    #assert demo1 == 143, f"demo1 is not 143: {demo1}"
    #demo2 = magnitude(load(SAMPLE2)[0])
    #assert demo2 == 1384, f"demo2 is not 1384: {demo2}"
    #demo3 = magnitude(load(SAMPLE3)[0])
    #assert demo3 == 3488, f"demo3 is not 3488: {demo3}"

    #Pair = script("Pair")
    #assert Pair is not None, "Pair is none"
    #process = script("process")
    #assert process is not None, "process is none"
    ###demo4 = process(SAMPLE3)
    ###depth = demo4.depth
    ###assert depth == 3, f"depth is not 3: {depth}"
    ###llll = demo4.left.left.left.left
    ###assert llll == 8, f"llll is not 8: {llll}"
    ###llrl = demo4.left.left.right.left
    ###assert llrl == 7, f"llrl is not 7: {llrl}"
    ###rlll = demo4.right.left.left.left
    ###assert rlll == 0, f"rlll is not 0: {rlll}"
    ###rlrl = demo4.right.left.right.left
    ###assert rlrl == 6, f"rlrl is not 6: {rlrl}"
    ###rrl = demo4.right.right.left
    ###assert rrl == 8, f"rrl is not 8: {rrl}"

    #pairs = load(SAMPLE5)
    #a, b = pairs[0], pairs[1]
    #pair = Pair(a, b)
    ##assert pair.depth == 4, f"depth is not 4: {pair.depth}"
    ##assert pair.max_value == 9, f"max_value is not 9: {pair.max_value}"
    ##lllll = pair.left.left.left.left.left
    ##assert lllll == 4, f"lllll = {lllll}"
    ##llllr = pair.left.left.left.left.right
    ##assert llllr == 3, f"llllr = {llllr}"

    ###print(0, pair)
    #changed, pair = step(pair)
    ###print(1, pair)
    #assert changed == True, f"nothing changed: {pair}"
    #llll = pair.left.left.left.left
    #assert llll == 0, f"llll = {llll}"
    #lllr = pair.left.left.left.right
    #assert lllr == 7, f"lllr = {lllr}"

    ###print(0, pair)
    #changed, pair = step(pair)
    ###print(1, pair)
    #assert changed == True, f"nothing changed: {pair}"
    #lrl = pair.left.right.left
    #assert lrl == 15, f"lrl = {lrl}"
    #lrrl = pair.left.right.right.left
    #assert lrrl == 0, f"lrrl = {lrrl}"
    #lrrr = pair.left.right.right.right
    #assert lrrr == 13, f"lrrr = {lrrr}"

    ###print(0, pair)
    #changed, pair = step(pair)
    ###print(1, pair)
    #assert changed == True, f"nothing changed: {pair}"
    #lrll = pair.left.right.left.left
    #assert lrll == 7, f"lrll = {lrll}"
    #lrlr = pair.left.right.left.right
    #assert lrlr == 8, f"lrlr = {lrlr}"

    ###print(0, pair)
    #changed, pair = step(pair)
    ###print(1, pair)
    #assert changed == True, f"nothing changed: {pair}"
    #lrrrl = pair.left.right.right.right.left
    #assert lrrrl == 6, f"lrrrl = {lrrrl}"
    #lrrrr = pair.left.right.right.right.right
    #assert lrrrr == 7, f"lrrrr = {lrrrr}"

    ###print(0, pair)
    #changed, pair = step(pair)
    ###print(1, pair)
    #assert changed == True, f"nothing changed: {pair}"
    #lrrl = pair.left.right.right.left
    #assert lrrl == 6, f"lrrl = {lrrl}"
    #lrrr = pair.left.right.right.right
    #assert lrrr == 0, f"lrrr = {lrrr}"
    #rl = pair.right.left
    #assert rl == 8, f"rl = {rl}"

    #add = script("add")
    #assert add is not None, "add is none"

    #pairs = load(INPUT)

    ### [[[[7,0],[7,8]],[[7,9],[0,6]]],[[[7,0],[6,6]],[[7,7],[0,9]]]]
    ##print(0, pairs)
    #pair, pairs = add(pairs)
    ##print(1, pairs)
    #assert pair.depth == 3, f"depth is not 4: {pair.depth}"
    #assert pair.max_value == 9, f"max_value is not 9: {pair.max_value}"
    ##assert pair is None, pair

    ### [[[[7,7],[7,7]],[[7,0],[7,7]]],[[[7,7],[6,7]],[[7,7],[8,9]]]]
    ##print(0, pairs)
    #pair, pairs = add(pairs)
    ##print(1, pairs)
    #assert pair.depth == 3, f"depth is not 4: {pair.depth}"
    #assert pair.max_value == 9, f"max_value is not 9: {pair.max_value}"
    #assert pair is None, pair

    # [[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]
    #final = process(INPUT)
    #print(final)
    #depth = final.depth
    #assert depth == 3, f"depth is not 3: {depth}"
    #llll = final.left.left.left.left
    #assert llll == 6, f"llll is not 6: {llll}"

    result = d18p1(INPUT)
    assert result == 4140, f"result is not 4140: {result}"

#def test_d18p2():
#    script = get_solution_script(index)
#    assert script is not None, "script is none"
#
#    d18p2 = script("d18p2")
#    assert d18p2 is not None, "d18p2 is none"
#
#    result = d18p2(INPUT)
#    assert result == 112, f"result is not 112: {result}"

"""
Pair(
    Pair(
        Pair(
            Pair(
                0,
                Pair(5,8,0),
                1
            ),
            Pair(
                Pair(1,7,0),
                Pair(9,6,0),
                1
            ),
            2
        ),
        Pair(
            Pair(
                4,
                Pair(1,2,0),
                1
            ),
            Pair(
                Pair(1,4,0),
                2,
                1
            ),
            2
        ),
        3
    ),
    Pair(
        Pair(
            Pair(
                5,
                Pair(2,8,0),
                1
            ),
            4,
            2
        ),
        Pair(
            5,
            Pair(
                Pair(9,9,0),
                0,
                1
            ),
            2
        ),
        3
    ),
    4
)

Pair(
    Pair(
        Pair(
            Pair(5,5,0),
            Pair(0,10,0),
            1
        ),
        Pair(
            Pair(3,0,-1),
            Pair(17,3,0),
            1
        ),
        3
    ),
    Pair(
        Pair(
            Pair(0,18,0),
            Pair(2,5,0),
            1
        ),
        Pair(
            Pair(8,13,-1),
            Pair(10,0,-1),
            0
        ),
        2
    ),
    4
)
"""
