# --- Making sure it is able to import intCodeComputer module ---
# In case cwd is parent directory (i.e. in an editor)
import sys
sys.path.append("../IntCode Computer")

# In case cwd is the dir in which this file is located
import os
file_dir   = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(file_dir)
os.chdir(parent_dir)
from intCodeComputer import IntCodeComputer


def day09(input: int, path="./day09/input.txt") -> int:
    comp = IntCodeComputer(path, input_=input)
    comp.run(show_outputs=True)
    return comp.output

if __name__ == '__main__':
    day09(2)
