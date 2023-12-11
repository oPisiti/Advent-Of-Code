"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""

import numpy as np


def pipe_maze():
    with open("input.txt") as f:
        maze = f.read().strip().split("\n")

    # Finding S
    s_pos = None
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "S":
                s_pos = np.array([i, j], dtype=np.int64)
                break

    # Initializing distances array
    dist = np.full((len(maze), len(maze[0])), np.inf)
    dist[s_pos[0], s_pos[1]] = 0

    # Going through all 3 directions
    for direction in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        curr_pos = s_pos + direction
        last_pos = s_pos.copy()
        
        curr_distance = 0
        last_distance = 0
        
        # Going through all the pipes
        while True:
            # Out of bounds
            if curr_pos[0] < 0 or curr_pos[0] >= len(maze): break
            if curr_pos[1] < 0 or curr_pos[1] >= len(maze[0]): break

            # Came back to S or reached a dead end
            if maze[curr_pos[0]][curr_pos[1]] == "S": break
            if maze[curr_pos[0]][curr_pos[1]] == ".": break

            # Copying last iteration's info
            last_distance = curr_distance

            # Setting the distance
            curr_distance += 1 
            if dist[curr_pos[0], curr_pos[1]] == curr_distance: break
            dist[curr_pos[0], curr_pos[1]] = min(dist[curr_pos[0], curr_pos[1]], curr_distance)

            # Updating position
            try:
                curr_pos, last_pos = update_pos(maze, curr_pos, last_pos)      
            except StopIteration as e:
                # The last pipe redirected here, but with a broken connection, i.e., --F.abs
                # - should not redirect to F
                break 

    dist[dist == np.inf] = 0
    return int(np.max(dist,))


def update_pos(maze: list[str], curr_pos: np.array, last_pos: np.array) -> (np.array, np.array):
    pipe_type = maze[curr_pos[0]][curr_pos[1]]
    
    new_pos = curr_pos.copy()

    match pipe_type:
        case "|":
            if   last_pos[0] < curr_pos[0]: new_pos[0] = curr_pos[0] + 1
            elif last_pos[0] > curr_pos[0]: new_pos[0] = curr_pos[0] - 1
            else:                           raise StopIteration()
        case "-":
            if   last_pos[1] < curr_pos[1]: new_pos[1] = curr_pos[1] + 1
            elif last_pos[1] > curr_pos[1]: new_pos[1] = curr_pos[1] - 1
            else:                           raise StopIteration()
        case "F":
            if   last_pos[1] > curr_pos[1]: new_pos[0] = curr_pos[0] + 1
            elif last_pos[0] > curr_pos[0]: new_pos[1] = curr_pos[1] + 1
            else:                           raise StopIteration()
        case "7":
            if   last_pos[1] < curr_pos[1]: new_pos[0] = curr_pos[0] + 1
            elif last_pos[0] > curr_pos[0]: new_pos[1] = curr_pos[1] - 1
            else:                           raise StopIteration()
        case "J":
            if   last_pos[1] < curr_pos[1]: new_pos[0] = curr_pos[0] - 1
            elif last_pos[0] < curr_pos[0]: new_pos[1] = curr_pos[1] - 1
            else:                           raise StopIteration()
        case "L":
            if   last_pos[1] > curr_pos[1]: new_pos[0] = curr_pos[0] - 1
            elif last_pos[0] < curr_pos[0]: new_pos[1] = curr_pos[1] + 1
            else:                           raise StopIteration()

    return new_pos, curr_pos

if __name__ == '__main__':
    print(pipe_maze())