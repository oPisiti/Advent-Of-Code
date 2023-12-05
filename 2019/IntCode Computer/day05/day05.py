try:
    from intCodeComputer import IntCodeComputer
except ModuleNotFoundError:
    import sys
    sys.path.append("../IntCode Computer")
    from intCodeComputer import IntCodeComputer


def day05():
    comp = IntCodeComputer("./day05/input.txt", input_=1)
    comp.run(show_outputs = False)
    print(comp.output)
    return comp.output


if __name__ == '__main__':
    day05()