"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""

import os


def hash():
    with open("input.txt") as f:
        maze = f.read().strip().split("\n")

    energized = [[[] for _ in range(len(maze))] for _ in range(len(maze))]

    light_pos = [0, -1]
    light_vel = [0,  1]

    # Parameters for function calls
    call_stack = [[light_pos, light_vel]]
    while call_stack:
        march_light(call_stack, maze, energized, call_stack[0][0], call_stack[0][1])
        call_stack.pop(0)

    print_energized(energized)

    return sum(sum(1 if len(pos) > 0 else 0 for pos in line) for line in energized)


def get_next_vel(maze: list[str], curr_pos: list[int], curr_vel: list[int]) -> list[list]:
    """ Sets the vel based on the current tile """
    
    match maze[curr_pos[0]][curr_pos[1]]:
        case "\\":
            if   curr_vel == [ 0,  1]: return [[ 1,  0], ]
            elif curr_vel == [ 0, -1]: return [[-1,  0], ]
            elif curr_vel == [ 1,  0]: return [[ 0,  1], ]
            elif curr_vel == [-1,  0]: return [[ 0, -1], ]

        case "/":
            if   curr_vel == [ 0,  1]: return [[-1,  0], ]
            elif curr_vel == [ 0, -1]: return [[ 1,  0], ]
            elif curr_vel == [ 1,  0]: return [[ 0, -1], ]
            elif curr_vel == [-1,  0]: return [[ 0,  1], ]

        case "-":
            if curr_vel in ([ 1,  0], [-1,  0]):
                return [[0,  1], [0, -1]]

        case "|":
            if curr_vel in ([ 0,  1], [ 0,  -1]):
                return [[ 1, 0], [-1, 0]]

    return [curr_vel, ]


def march_light(call_stack: list[list[int]], maze: list[str], energized: list[list[bool]], pos: list[int], vel: list[int]) -> None:
    curr_pos = [pos[0] + vel[0], pos[1] + vel[1]]

    # Out of bounds
    if curr_pos[0] < 0 or curr_pos[0] >= len(maze) or curr_pos[1] < 0 or curr_pos[1] >= len(maze[0]):
        return

    # Back to the same configuration
    if vel in energized[curr_pos[0]][curr_pos[1]]: return

    # Marking current position
    energized[curr_pos[0]][curr_pos[1]].append(vel)

    # Skipping "." - Reduces the number of recursion calls
    if maze[curr_pos[0]][curr_pos[1]] == ".":
        call_stack.append([curr_pos, vel])
        return
    
    # Next velocities
    next_vel = get_next_vel(maze, curr_pos, vel)

    # Next step
    for v in next_vel:
        call_stack.append([curr_pos, v])       


def print_energized(energized: list[list[bool]]):
    # Printing energized
    for i, line in enumerate(energized):
        print(f"{i+1:03}: ", end="")
        for char in line:
            print("#" if char else ".", end="")

        print()


if __name__ == '__main__':
    print(hash())