try:
    from intCodeComputer import IntCodeComputer
except ModuleNotFoundError:
    import sys
    sys.path.append("../IntCode Computer")
    from intCodeComputer import IntCodeComputer

def day02_plus():
    computer = IntCodeComputer("./day02/input.txt")

    desired_output     = 19690720
    max_noun, max_verb = 99, 99
    noun, verb = computer.search_for_output(desired_output, max_noun, max_verb)

    ans = 100*noun + verb
    print(f"Answer: {ans}")
    return ans
    

if __name__ == '__main__':
    day02_plus()
