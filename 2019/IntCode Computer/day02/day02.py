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

    ans = computer.get_output()
    print(f"Position 0: {ans}")
    return ans


if __name__ == '__main__':
    day02()
