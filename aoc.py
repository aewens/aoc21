from utils import get_puzzle, get_solutions

from time import perf_counter

def main():
    divider = "-" * 80
    print("AOC 2021 Solutions:")
    print(divider)
    solutions = get_solutions()
    for index, solution in get_solutions().items():
        start = perf_counter()
        day = f"Day {index:02}"
        puzzle = get_puzzle(index)
        result = solution(puzzle)
        if result is None:
            print(day, "ERROR")
            continue

        a, b = result
        print(day + "a", a)
        print(day + "b", b)
        print(f"~ {perf_counter()-start:.05f}s")
        print(divider)

if __name__ == "__main__":
    main()
