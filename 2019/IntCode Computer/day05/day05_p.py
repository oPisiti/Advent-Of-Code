try:
    from intCodeComputer import IntCodeComputer
except ModuleNotFoundError:
    import sys
    sys.path.append("../IntCode Computer")
    from intCodeComputer import IntCodeComputer


def day05_plus(input: int, path="./day05/input.txt") -> int:
    comp = IntCodeComputer(path, input_=input)
    comp.run(show_outputs=True)
    print(comp.output)
    return comp.output


if __name__ == '__main__':
    day05_plus(5)
