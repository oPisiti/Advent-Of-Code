"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""

from math import lcm
import re


def sand_map():
    with open("input.txt") as f:
        instructions, _map = f.read().strip().split("\n\n")

    splits = [inst for inst in _map.split("\n")]

    _map = dict()
    for inst in splits:
        tokens = re.findall("\w+", inst)
        _map[tokens[0]] =  [tokens[1], tokens[2]]

    starting_nodes = [node for node in _map.keys() if node[-1] == "A"]

    # Parameters: (first_occurrence, loop_size)
    parameters = []
    for node in starting_nodes:
        parameters.append(get_parameters(_map, node, instructions))

    # First common occurence
    answer = 1
    for p in parameters:
        answer = lcm(answer, p[0])

    return answer

def get_parameters(_map: dict(), starting_loc: str, instructions: str) -> tuple[int, int]:
    goal_location = "Z"

    # Traversing the map
    count = 0
    curr_loc = starting_loc
    inst_index = 0
    
    for i in range(2):
        # Finding the first occurrence of Z
        while True:
            if instructions[inst_index] == "L":
                curr_loc = _map[curr_loc][0]
            else:
                curr_loc = _map[curr_loc][1]

            count += 1
            inst_index += 1
            if inst_index >= len(instructions): inst_index = 0
            
            if curr_loc[-1] == goal_location: break
        
        if i == 0: first_occ_count = count
        else:      loop_size = count - first_occ_count


    return first_occ_count, loop_size


if __name__ == '__main__':
    print(sand_map())