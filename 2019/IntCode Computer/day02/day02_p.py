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


def day02_plus():
    computer = IntCodeComputer("./day02/input.txt")

    desired_output     = 19690720
    max_noun, max_verb = 99, 99
    noun, verb = computer.search_for_output(desired_output, max_noun, max_verb)

    ans = 100*noun + verb
    print(f"Answer: {ans}")
    return ans
    

if __name__ == '__main__':
    day02_plus()