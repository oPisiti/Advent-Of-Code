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
    loop = np.full((len(maze), len(maze[0])), np.inf)
    loop[s_pos[0], s_pos[1]] = 1

    # Going through all 4 directions
    best_direction = tuple()
    for direction in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        best_direction = direction
        curr_pos = s_pos + direction
        last_pos = s_pos.copy()

        found_loop = False
        
        # Going through all the pipes
        while True:
            # Out of bounds
            if curr_pos[0] < 0 or curr_pos[0] >= len(maze): break
            if curr_pos[1] < 0 or curr_pos[1] >= len(maze[0]): break

            # Came back to S or reached a dead end
            if maze[curr_pos[0]][curr_pos[1]] == "S": 
                found_loop = True
                break
            if maze[curr_pos[0]][curr_pos[1]] == ".": break

            # Setting the distance
            loop[curr_pos[0], curr_pos[1]] = 1

            # Updating position
            try:
                curr_pos, last_pos, _ = update_pos(maze, curr_pos, last_pos)      
            except StopIteration as e:
                # The last pipe redirected here, but with a broken connection, i.e., --F.abs
                # - should not redirect to F
                break 

        # Resetting of the loop was not found
        if not found_loop: 
            loop.fill(np.inf)
            loop[s_pos[0], s_pos[1]] = 1
            continue
        else:
            break

    # Going through the loop and filling each side with a value
    # 2: left
    # 3: right
    curr_pos = s_pos + best_direction
    last_pos = s_pos.copy()
    sentido = best_direction
    while True:
        # Came back to S - done
        if maze[curr_pos[0]][curr_pos[1]] == "S": break

        # Setting values for left and right
        match sentido:
            case (-1,  0):
                set_value(loop, curr_pos + ( 0, -1), 2)
                set_value(loop, curr_pos + ( 0,  1), 3)
            case ( 0, -1):
                set_value(loop, curr_pos + ( 1,  0), 2)
                set_value(loop, curr_pos + (-1,  0), 3)
            case ( 1,  0):
                set_value(loop, curr_pos + ( 0,  1), 2)
                set_value(loop, curr_pos + ( 0, -1), 3)
            case ( 0,  1):
                set_value(loop, curr_pos + (-1,  0), 2)
                set_value(loop, curr_pos + ( 1,  0), 3)

        # Updating position
        try:
            curr_pos, last_pos, sentido = update_pos(maze, curr_pos, last_pos, sentido)      
        except StopIteration as e:
            # The last pipe redirected here, but with a broken connection, i.e., --F.abs
            # - should not redirect to F
            break 

    # Filling in the remaining inf values
    for i in range(len(loop)):
        for j in range(len(loop[0])):
            if loop[i][j] != np.inf: continue

            filled = False

            for delta in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                curr_pos_i = i
                curr_pos_j = j

                while True:
                    try:
                        loop[curr_pos_i, curr_pos_j]
                    except IndexError as e:
                        break

                    if loop[curr_pos_i, curr_pos_j] == 1:
                        break
                    
                    if loop[curr_pos_i, curr_pos_j] != np.inf:
                        loop[i, j] = loop[curr_pos_i, curr_pos_j]
                        filled = True
                        break

                    curr_pos_i += delta[0]
                    curr_pos_j += delta[1]

                if filled: break


    return f"2: {len(loop[loop == 2])}\n3: {len(loop[loop == 3])}"


def set_value(loop: np.array, pos: np.array, value) -> np.array:
    """ Ignores IndexErrors, wrap arounds and other values other than np.inf"""

    if pos[0] < 0 or pos[0] >= len(loop):    return loop
    if pos[1] < 0 or pos[1] >= len(loop[0]): return loop

    try:
        if loop[pos[0]][pos[1]] == np.inf:
            loop[pos[0]][pos[1]] = value
    except IndexError as e:
        pass

    return

def update_pos(maze: list[str], curr_pos: np.array, last_pos: np.array, sentido: tuple = (0, 0)) -> (np.array, np.array, tuple):
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
            if   last_pos[1] > curr_pos[1]: 
                new_pos[0] = curr_pos[0] + 1
                sentido = (1, 0)
            elif last_pos[0] > curr_pos[0]: 
                new_pos[1] = curr_pos[1] + 1
                sentido = (0, 1)
            else:                           raise StopIteration()
        case "7":
            if   last_pos[1] < curr_pos[1]: 
                new_pos[0] = curr_pos[0] + 1
                sentido = (1, 0)
            elif last_pos[0] > curr_pos[0]: 
                new_pos[1] = curr_pos[1] - 1
                sentido = (0, -1)
            else:                           raise StopIteration()
        case "J":
            if   last_pos[1] < curr_pos[1]: 
                new_pos[0] = curr_pos[0] - 1
                sentido = (-1, 0)
            elif last_pos[0] < curr_pos[0]: 
                new_pos[1] = curr_pos[1] - 1
                sentido = (0, -1)
            else:                           raise StopIteration()
        case "L":
            if   last_pos[1] > curr_pos[1]: 
                new_pos[0] = curr_pos[0] - 1
                sentido = (-1, 0)
            elif last_pos[0] < curr_pos[0]: 
                new_pos[1] = curr_pos[1] + 1
                sentido = (0, 1)
            else:                           raise StopIteration()

    return new_pos, curr_pos, sentido

if __name__ == '__main__':
    print(pipe_maze())