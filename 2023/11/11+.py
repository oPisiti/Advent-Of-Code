"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""

import re


def cosmic_expansion():
    with open("input.txt") as f:
        uni_raw = f.read().strip().split("\n")

    uni = [re.findall(".", line) for line in uni_raw]

    expansion_rate = 1_000_000
    i_expanded, j_expanded = expand(uni)

    # Getting '#' positions
    galaxies_indexes = []
    for i in range(len(uni)):
        for j in range(len(uni[0])):
            if uni[i][j] == "#": galaxies_indexes.append((i, j))

    # Defining the pairs
    pairs = []
    for f in range(len(galaxies_indexes)):
        for s in range(f+1, len(galaxies_indexes)):
            pairs.append((galaxies_indexes[f], galaxies_indexes[s]))

    # Calculating all the distances
    dist_sum = 0
    for f, s in pairs:
        dist_base = abs(f[0] - s[0]) + abs(f[1] - s[1])
        
        i_inside_count = 0
        for i_ex in i_expanded:
            if i_ex > min(f[0], s[0]) and i_ex < max(f[0], s[0]):
                i_inside_count += 1

        j_inside_count = 0
        for j_ex in j_expanded:
            if j_ex > min(f[1], s[1]) and j_ex < max(f[1], s[1]):
                j_inside_count += 1

        dist_expanded = (i_inside_count + j_inside_count) * (expansion_rate - 1)

        dist_sum += dist_base + dist_expanded

    return dist_sum


def expand(uni: list[list[str]]) -> (list[int], list[int]):
    """ Returns rows and column indexes where the universe expanded """

    # Vertical expansion
    j_add_list = []
    for j in range(len(uni[0])):
        clean = True
        for i in range(len(uni)):
            if uni[i][j] == "#":
                clean = False
                break
        
        if clean: j_add_list.append(j)

    # Horizontal expansion
    i_add_list = []
    for i in range(len(uni)):
        for j in range(len(uni[0])):
            clean = True
            if uni[i][j] == "#":
                clean = False
                break
        
        if clean: i_add_list.append(i)

    return i_add_list, j_add_list


if __name__ == '__main__':
    print(cosmic_expansion())