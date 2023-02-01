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


def day11(input: int, path="./day11/input.txt"):
    comp = IntCodeComputer(path, input_=input)

    with io.StringIO() as buf, redirect_stdout(buf):
        comp.run(show_outputs=True)
        output = buf.getvalue()

    print(f'{output}')

if __name__ == '__main__':
    day11(1)
