from pathlib import Path
from importlib import import_module
from collections import defaultdict

def noop(*args, **kwargs):
    pass

def get_puzzle(day, nostrip=False, nolines=False):
    target = Path.cwd() / "inputs" / f"day{day:02}.txt"
    if not target.exists():
        return None

    text = target.read_text()
    if not nostrip:
        text = text.strip()

    if nolines:
        return text

    lines = text.split("\n")
    if not nostrip:
        return lines

    newlines = list()
    for line in lines:
        newlines.append(line.strip())

    return newlines

def get_solutions():
    solutions = defaultdict(lambda: noop)
    path = Path.cwd() / "solutions"
    if not path.exists():
        return solutions

    for module in path.glob("*.py"):
        name = module.name
        if not module.is_file() or name.startswith("_"):
            continue

        package = name.replace(".py", "")
        day = int(package[-2:])

        # equivalent of "import <path>.<package>"
        script = import_module(f".{package}", path.name)
        solutions[day] = getattr(script, "solve", noop)

    return solutions
