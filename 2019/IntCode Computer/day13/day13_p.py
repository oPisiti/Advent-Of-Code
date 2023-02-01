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

import io
from contextlib import redirect_stdout
import re


class Instruction():
    def __init__(self, j: str, i: str, type: str) -> None:
        self.j = j
        self.i = i
        self.type = type


def day13_plus(input: int, path="./day13/input.txt"):
    comp = IntCodeComputer(path, input_=input, prompt_for_inputs=True)

    # First run to determine the size of the screen
    with io.StringIO() as buf, redirect_stdout(buf):
        comp.run()
        output = buf.getvalue()

    output   = output.split("\n")[:-1]
    inst_end = [Instruction(output[a], output[a+1], output[a+2]) for a in range(0, len(output), 3)]

    max_j = max([int(a.j) for a in inst_end])
    max_i = max([int(a.i) for a in inst_end])

    # TODO: Make a visualization of the game and beat it
    
    # Resetting and cheating the machine into thinking I have put quarters in
    comp.reset_memory()
    comp.opcode[0] = '2' 



if __name__ == '__main__':
    day13_plus(0)
