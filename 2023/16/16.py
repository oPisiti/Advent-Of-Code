"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""

import os


def hash():
    with open("input.txt") as f:
        maze = f.read().strip().split("\n")

    energized = [[False for _ in range(len(maze))] for _ in range(len(maze))]

    light_pos = [0, -1]
    light_vel = [0,  1]


    march_light(maze, energized, light_pos, light_vel)

    print_energized(energized)

    return sum(sum(pos for pos in line) for line in energized)


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


def march_light(maze: list[str], energized: list[list[bool]], pos: list[int], vel: list[int]) -> None:
    curr_pos = [pos[0] + vel[0], pos[1] + vel[1]]

    # Out of bounds
    if curr_pos[0] < 0 or curr_pos[0] >= len(maze) or curr_pos[1] < 0 or curr_pos[1] >= len(maze[0]):
        return

    # Marking tile as energized
    was_energized = energized[curr_pos[0]][curr_pos[1]]
    energized[curr_pos[0]][curr_pos[1]] = True
    
    # Next velocities
    next_vel = get_next_vel(maze, curr_pos, vel)

    # Back to the same configuration
    if was_energized:
        future_steps_taken = True

        for v in next_vel:
            try:
                if not energized[curr_pos[0] + v[0]][curr_pos[1] + v[1]]:
                    future_steps_taken = False
            except IndexError as e:
                continue
        
        if future_steps_taken: return

    # Next step
    for v in next_vel:
        march_light(maze, energized, curr_pos, v)        


def print_energized(energized: list[list[bool]]):
    # Printing energized
    for i, line in enumerate(energized):
        print(f"{i+1:03}: ", end="")
        for char in line:
            print("#" if char else ".", end="")

        print()


if __name__ == '__main__':
    print(hash())