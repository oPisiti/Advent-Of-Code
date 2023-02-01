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


def day13(input: int, path="./day13/input.txt"):
    comp = IntCodeComputer(path, input_=input)

    with io.StringIO() as buf, redirect_stdout(buf):
        comp.run()
        output = buf.getvalue()

    output = output.split("\n")[:-1]
    inst = [Instruction(output[a], output[a+1], output[a+2]) for a in range(0, len(output), 3)]
    
    n_blocks = 0
    for _ in filter(lambda a: a.type == '2', inst): n_blocks += 1

    print(f'There are {n_blocks} blocks on the screen when the game exits')
    return n_blocks


if __name__ == '__main__':
    input()
    day13(0)