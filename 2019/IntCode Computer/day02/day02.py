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

def day02(path="./day02/input.txt"):

    computer = IntCodeComputer(path)    


    computer.opcode[1] = 12
    computer.opcode[2] = 2

    computer.run()

    print(f"Position 0: {computer.opcode[0]}")
    return computer.opcode[0]


if __name__ == '__main__':
    day02()