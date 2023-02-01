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


def day05():
    comp = IntCodeComputer("./day05/input.txt", input_=1)
    comp.run(show_outputs = False)
    print(comp.output)
    return comp.output


if __name__ == '__main__':
    day05()