try:
    from intCodeComputer import IntCodeComputer
except ModuleNotFoundError:
    import sys
    sys.path.append("../IntCode Computer")
    from intCodeComputer import IntCodeComputer

def main():
    comp = IntCodeComputer("./day05/input.txt", input_=1)
    comp.run()
    print(f'Output: {comp.output}')


if __name__ == '__main__':
    main()