"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""

import re


def sand_map():
    with open("input.txt") as f:
        instructions, _map = f.read().strip().split("\n\n")

    splits = [inst for inst in _map.split("\n")]

    _map = dict()
    for inst in splits:
        tokens = re.findall("\w+", inst)
        _map[tokens[0]] =  [tokens[1], tokens[2]]

    goal_location = "ZZZ"

    # Traversing the map
    count = 0
    curr_loc = "AAA"
    inst_index = 0
    while True:
        if instructions[inst_index] == "L":
            curr_loc = _map[curr_loc][0]
        else:
            curr_loc = _map[curr_loc][1]

        if curr_loc == goal_location: break

        count += 1
        inst_index += 1
        if inst_index >= len(instructions): inst_index = 0

    return count + 1


if __name__ == '__main__':
    print(sand_map())