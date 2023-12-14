"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""

from copy import deepcopy
from functools import cache
from math import floor


def rocks():
    with open("input.txt") as f:
        data = f.read().strip().splitlines()

    platform = [[item for item in row] for row in data]

    cached_cycles = dict()

    found_cycle = False
    curr_hash = None
    iterations = 1_000_000_000
    for a in range(iterations):

        if found_cycle:
            # Calculating final configuration based on the cache size
            it_remaining = iterations - a

            cycle_size = sum([1 for k, v in cached_cycles.items() if v[2] != 0])

            it_liquid = it_remaining - cycle_size * floor(it_remaining/cycle_size)

            # Defining the answer's hash
            for _ in range(it_liquid - 1):
                curr_hash = cached_cycles[curr_hash][1]

            break

        base_hash = hash(str(platform))
        try:
            # Current config has been cached
            platform = deepcopy(cached_cycles[base_hash][0])

            # I'm back to a previous configuration
            if cached_cycles[base_hash][2] > 0:
                found_cycle = True
                curr_hash = cached_cycles[base_hash][1]
            
            # Adding to count
            cached_cycles[base_hash][2] += 1
            continue
        except KeyError as e:
            pass

        # Tilting north
        for i in range(1, len(platform)):
            for j in range(len(platform[0])):
                # Is a moveable rock
                if platform[i][j] == "O":
                    move_rock_north_south(platform, i, j)

        # Tilting west
        for j in range(len(platform[0])):
            for i in range(len(platform)):
                # Is a moveable rock
                if platform[i][j] == "O":
                    move_rock_west_east(platform, i, j)

        # Tilting south
        for i in range(len(platform)-2, -1, -1):
            for j in range(len(platform[0])):
                # Is a moveable rock
                if platform[i][j] == "O":
                    move_rock_north_south(platform, i, j, north=False)

        # Tilting east
        for j in range(len(platform[0])-2, -1, -1):
            for i in range(len(platform)):
                # Is a moveable rock
                if platform[i][j] == "O":
                    move_rock_west_east(platform, i, j, west=False)

        cached_cycles[base_hash] = [deepcopy(platform), hash(str(platform)), 0]

    # Calculating the score
    platform = deepcopy(cached_cycles[curr_hash][0])
    score = sum([line.count("O") * (len(platform) - i) for i, line in enumerate(platform)])

    return score


def move_rock_north_south(plat: list[list[str]], i: int, j: int, north: bool = True) -> None:
    if north:
        i_target = i - 1
        delta = -1
    else:
        i_target = i + 1
        delta = 1

    edge_value = (0, len(plat) - 1)

    # Determining the end location
    while i_target >= edge_value[0] and i_target <= edge_value[1]:
        if plat[i_target][j] in ("#", "O"):
            i_target -= delta
            break

        i_target += delta

    i_target = max(i_target, 0) if north else min(i_target, len(plat) - 1)

    plat[i][j] = "."
    plat[i_target][j] = "O"


def move_rock_west_east(plat: list[list[str]], i: int, j: int, west: bool = True) -> None:
    if west:
        j_target = j - 1
        delta = -1
    else:
        j_target = j + 1
        delta = 1

    edge_value = (0, len(plat[0]) - 1)

    # Determining the end location
    while j_target >= edge_value[0] and j_target <= edge_value[1]:
        if plat[i][j_target] in ("#", "O"):
            j_target -= delta
            break

        j_target += delta

    j_target = max(j_target, edge_value[0]) if west else min(j_target, edge_value[1])

    plat[i][j] = "."
    plat[i][j_target] = "O"


if __name__ == '__main__':
    print(rocks())