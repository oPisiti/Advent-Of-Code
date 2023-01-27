try:
    from intCodeComputer import IntCodeComputer
except ModuleNotFoundError:
    import sys
    sys.path.append("../IntCode Computer")
    from intCodeComputer import IntCodeComputer

def day02():
    computer = IntCodeComputer("./day02/input.txt")
    computer.opcode[1] = 12
    computer.opcode[2] = 2

    computer.run()

    print(f"Position 0: {computer.opcode[0]}")
    return computer.opcode[0]


if __name__ == '__main__':
    day02()
