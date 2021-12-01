import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).absolute().parent.parent))

from utils import get_puzzle, get_solutions, get_solution_script

solutions = get_solutions()
