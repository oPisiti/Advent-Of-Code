try:
    from intCodeComputer import IntCodeComputer
except ModuleNotFoundError:
    import sys
    sys.path.append("../IntCode Computer")
    from intCodeComputer import IntCodeComputer


def day09(input: int, path="./day09/input.txt") -> int:
    comp = IntCodeComputer(path, input_=input)
    comp.run(show_outputs=True)
    return comp.output

if __name__ == '__main__':
    day09(2)
